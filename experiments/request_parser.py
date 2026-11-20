def parse_request_line(line: bytes):
    if not line.endswith(b"\r\n"):
        raise ValueError

    clean_line = line.removesuffix(b"\r\n")
    result = clean_line.split(b" ")

    if len(result) != 3 or any(not part for part in result):
        raise ValueError

    result = [s.decode("ascii") for s in result]
    return tuple(result)


def parse_headers(header_lines: list[bytes]) -> dict[str, str]:
    """
    Parse HTTP header lines into a dictionary.

    Example:
        Input:
            [b"Host: localhost", b"Content-Length: 5"]

        Output:
            {"host": "localhost", "content-length": "5"}

    Assumptions for this exercise:
        - Header lines do not include trailing CRLF.
        - Field names and values are ASCII.
        - Duplicate field names are rejected.
    """

    headers = {}

    for line in header_lines:
        # TODO 1: Check whether the line contains b":"
        # Raise ValueError if it doesn't.
        if b":" not in line:
            raise ValueError

        # TODO 2: Split at the FIRST colon.
        # Hint: line.split(b":", 1)
        field_name, field_value = line.split(b":", 1)

        # TODO 3: Reject empty field names.
        if not field_name:
            raise ValueError

        if field_name.endswith((b" ", b"\t")):
            raise ValueError

        # TODO 4: Decode the field name and convert it to lowercase.
        name = field_name.decode("ascii").lower()

        # TODO 5: Decode the value and remove surrounding
        # spaces and tabs.
        value = field_value.decode("ascii").strip(" \t") 

        # TODO 6: Reject duplicate normalized field names.
        # Hint: Check whether the key already exists in headers.
        if name in headers:
            raise ValueError

        # TODO 7: Store the normalized name and value
        # in the headers dictionary.
        headers[name] = value


    return headers


def run_test(name, parser, input_data, expected=None, expected_error=None):
    try:
        result = parser(input_data)

        if expected_error is not None:
            print(f"FAIL: {name} - Expected {expected_error.__name__}")
            return

        assert result == expected, (
            f"Expected {expected!r}, got {result!r}"
        )

        print(f"PASS: {name}")

    except Exception as exc:
        if expected_error is not None and isinstance(exc, expected_error):
            print(f"PASS: {name}")
        else:
            print(f"FAIL: {name} - {type(exc).__name__}: {exc}")


if __name__ == "__main__":

    print("\n=== REQUEST LINE TESTS ===")

    run_test(
        "Test 1: Basic GET",
        parse_request_line,
        b"GET / HTTP/1.1\r\n",
        expected=("GET", "/", "HTTP/1.1"),
    )

    run_test(
        "Test 2: POST request",
        parse_request_line,
        b"POST /data HTTP/1.1\r\n",
        expected=("POST", "/data", "HTTP/1.1"),
    )

    run_test(
        "Test 3: Missing version",
        parse_request_line,
        b"GET /hello\r\n",
        expected_error=ValueError,
    )

    run_test(
        "Test 4: Extra whitespace",
        parse_request_line,
        b"GET  /hello HTTP/1.1\r\n",
        expected_error=ValueError,
    )

    run_test(
        "Test 5: Missing CRLF",
        parse_request_line,
        b"GET / HTTP/1.1",
        expected_error=ValueError,
    )

    run_test(
        "Test 6: Empty method",
        parse_request_line,
        b" /hello HTTP/1.1\r\n",
        expected_error=ValueError,
    )

    run_test(
        "Test 7: Invalid ASCII",
        parse_request_line,
        b"GET /\xff HTTP/1.1\r\n",
        expected_error=ValueError,
    )

    print("\n=== HEADER PARSING TESTS ===")

    run_test(
        "Test 8: Basic headers",
        parse_headers,
        [
            b"Host: localhost",
            b"Content-Length: 5",
        ],
        expected={
            "host": "localhost",
            "content-length": "5",
        },
    )

    run_test(
        "Test 9: Case-insensitive field names",
        parse_headers,
        [
            b"HOST: localhost",
            b"User-Agent: curl",
        ],
        expected={
            "host": "localhost",
            "user-agent": "curl",
        },
    )

    run_test(
        "Test 10: Surrounding whitespace",
        parse_headers,
        [
            b"Host:   localhost  ",
            b"Accept:\ttext/html\t",
        ],
        expected={
            "host": "localhost",
            "accept": "text/html",
        },
    )

    run_test(
        "Test 11: Colon in field value",
        parse_headers,
        [
            b"Referer: http://example.com:8080/page",
        ],
        expected={
            "referer": "http://example.com:8080/page",
        },
    )

    run_test(
        "Test 12: Missing colon",
        parse_headers,
        [
            b"Host localhost",
        ],
        expected_error=ValueError,
    )

    run_test(
        "Test 13: Empty field name",
        parse_headers,
        [
            b": localhost",
        ],
        expected_error=ValueError,
    )

    run_test(
        "Test 14: Duplicate field name",
        parse_headers,
        [
            b"Host: localhost",
            b"host: example.com",
        ],
        expected_error=ValueError,
    )

    run_test(
        "Test 15: Empty header list",
        parse_headers,
        [],
        expected={},
    )
    run_test(
        "Test 16: Whitespace before colon",
        parse_headers,
        [b"Host : localhost"],
        expected_error=ValueError,
    )

    run_test(
        "Test 17: Tab before colon",
        parse_headers,
        [b"Host\t: localhost"],
        expected_error=ValueError,
    )

    run_test(
        "Test 18: Empty header value",
        parse_headers,
        [b"X-Custom:"],
        expected={"x-custom": ""},
    )
