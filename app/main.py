import socket


def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    connection, address = server_socket.accept()
    response = "HTTP/1.1 200 OK\r\n\r\n"
    connection.send(response.encode())
    connection.close()

if __name__ == "__main__":
    main()
