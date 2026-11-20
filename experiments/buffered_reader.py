def read_headers(conn):
    buffer = b""
    delimiter = b"\r\n\r\n"

    while True:
        chunk = conn.recv(1024)

        if not chunk:
            raise ConnectionError("Connection closed before headers completed")

        buffer += chunk

        if delimiter in buffer:
            headers, separator, leftover = buffer.partition(delimiter)
            headers += separator

            return (headers, leftover)


class FakeConnection:
    def __init__(self, chunks):
        self.chunks = iter(chunks)

    def recv(self, size):
        return next(self.chunks, b"")


if __name__ == "__main__":

    # Test 1: Complete headers in one read
    conn = FakeConnection([
        b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    ])

    headers, leftover = read_headers(conn)

    assert headers == b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    assert leftover == b""

    print("Test 1: Passed")

    # Test 2: Fragmented headers
    conn = FakeConnection([
        b"GET /hello HT",
        b"TP/1.1\r\nHost: local",
        b"host\r\n\r\n"
    ])

    headers, leftover = read_headers(conn)

    assert headers == b"GET /hello HTTP/1.1\r\nHost: localhost\r\n\r\n"
    assert leftover == b""

    print("Test 2: Passed")

    # Test 3: Client disconnects before completing headers
    conn = FakeConnection([
        b"GET / HTTP/1.1\r\nHost:",
        b""
    ])

    try:
        read_headers(conn)
    except ConnectionError:
        print("Test 3: Passed")
    else:
        raise AssertionError("Expected ConnectionError")

    # Test 4: Headers and body arrive together
    conn = FakeConnection([
        b"POST /data HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"Content-Length: 5\r\n"
        b"\r\n"
        b"hello"
    ])

    headers, leftover = read_headers(conn)

    assert headers.endswith(b"\r\n\r\n")
    assert leftover == b"hello"

    print("Test 4: Passed")

    # Test 5: Delimiter split across multiple reads
    conn = FakeConnection([
        b"GET / HTTP/1.1\r\nHost: localhost\r",
        b"\n\r",
        b"\nEXTRA"
    ])

    headers, leftover = read_headers(conn)

    assert headers == b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    assert leftover == b"EXTRA"

    print("Test 5: Passed")
