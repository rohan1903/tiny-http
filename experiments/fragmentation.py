chunks = [
    b"GET /hello HT",
    b"TP/1.1\r\nHost: local",
    b"host\r\n\r\n",
]

buffer = b""

for chunk in chunks:
    buffer += chunk

    print(f"Received: {chunk!r}")
    print(f"Buffer: {buffer!r}")
    print(f"Headers complete: {b'\r\n\r\n' in buffer}")
    print("---")
