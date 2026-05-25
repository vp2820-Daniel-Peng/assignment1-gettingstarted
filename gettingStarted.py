from socket import *
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            with open(filename[1:], "rb") as f:
                body = f.read()

            header = (
                "HTTP/1.1 200 OK\r\n"
                "Server: DanielWebServer\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                f"Content-Length: {len(body)}\r\n"
                "Connection: close\r\n"
                "\r\n"
            ).encode()

            connectionSocket.sendall(header + body)
            connectionSocket.close()

        except Exception:
            body = b"<html><body><h1>404 Not Found</h1></body></html>"

            header = (
                "HTTP/1.1 404 Not Found\r\n"
                "Server: DanielWebServer\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                f"Content-Length: {len(body)}\r\n"
                "Connection: close\r\n"
                "\r\n"
            ).encode()

            connectionSocket.sendall(header + body)
            connectionSocket.close()

if __name__ == "__main__":
    webServer(13331)