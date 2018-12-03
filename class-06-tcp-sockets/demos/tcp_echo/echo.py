import socket


def run():
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP,
    )
    server.bind(('127.0.0.1', 4444))
    server.listen(1)
    return server, server.accept()


if __name__ == '__main__':
    server, (conn, addr) = run()
    print(f'Received connection for { addr }')

    buffer_length = 16
    message_complete = False

    message = ''

    while not message_complete:
        part = conn.recv(buffer_length)

        print(part.decode())

        message += part.decode()

        if len(part) < buffer_length:
            message_complete = True

    # message = 'The server received your message.'
    conn.sendall(message.encode())

    conn.close()
    server.close()
