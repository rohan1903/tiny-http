import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))

print("Socket listening...")
s.listen()

try:
    while True:
        conn, addr = s.accept()
        print('Connection accepted.')

        try:
            data = conn.recv(1024)

            if not data:
                conn.close()
                continue

            rt = data.decode('utf-8')
            rline = rt.split("\r\n")[0]

            method, path, version = rline.split(" ") 

            if path == "/":
                body = b"Welcome to TinyHTTP"
                status = "200 OK"
            elif path == '/hello':
                body = b"Hello"
                status = "200 OK"
            else:
                body = b"Resource not found"
                status = "404 Not Found"

            headers = (
                    "HTTP/1.1 "
                    f"{status}"
                    "\r\n"
                    "Content-Type: text/plain\r\n"
                    f"Content-Length: {len(body)}\r\n"
                    "\r\n" #separator for body
            )

            response = headers.encode("ascii") + body
            conn.sendall(response)
        finally:
            conn.close()

finally:
    s.close()

