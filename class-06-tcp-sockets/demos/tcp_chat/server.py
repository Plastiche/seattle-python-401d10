from client import Client
import threading
import socket
import sys


PORT = 9876


class ChatServer(threading.Thread):
    def __init__(self, port, host='localhost'):
        super().__init__(daemon=True)
        self.port = port
        self.host = host
        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_TCP,
        )
        self.client_pool = []

        try:
            self.server.bind((self.host, self.port))
        except socket.error:
            print(f'Bind failed. { socket.error }')
            sys.exit()

        self.server.listen(10)

    def run_thread(self, id, nick, conn, addr):
        """
        """
        print(f'{nick} connected at { addr[0] }{ addr[1] }')

        while True:
            data = conn.recv(4096)

            # if len(self.client_pool):
            #     for c in self.client_pool:
            #         c.conn.sendall(data)

            [c.conn.sendall(data) for c in self.client_pool if len(self.client_pool)]

            # TODO: Rather than a list comprehension, call a Parse() method that handles all of the message parsing and client communications.

    def run(self):
        """
        """
        print(f'Server running on { self.host }{ self.port }.')

        while True:
            conn, addr = self.server.accept()
            client = Client(conn=conn, addr=addr)
            self.client_pool.append(client)
            threading.Thread(
                target=self.run_thread,
                args=(client.id, client.nick, client.conn, client.addr),
                daemon=True,
            ).start()


if __name__ == '__main__':
    server = ChatServer(PORT)

    try:
        server.run()
    except KeyboardInterrupt:
        [c.conn.close() for c in server.client_pool if len(server.client_pool)]
        sys.exit()
