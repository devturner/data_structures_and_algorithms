from .client import ChatClient
import threading
import socket
import sys

PORT = 5000

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
            self.server.bind((self.host, self.host))
        except socket.error:
            print('Bind failed{}'.format(socket.error))
            sys.exit()
        
        self.server.listen(1)

    def parser(self, id, nick, conn, message):
        if message.startswith('@'):
            data = message.split(maxsplit=1)
            conn.sendall(b'You have left the chatroom\n')
            reply = nick.encode() + b' has left the channel\n'
            [c.conn.sendall(reply) for c in self.client_pool if len(self.client_pool)]
            self.client_pool = [c for c in self.client_pool if c.id != id]
            conn.close()

            if data[0] == '@quit':
                pass

            else:
                conn.sendall(b'Invalid command, please try again. \n')
        else:
            reply = nick.encode() + b': ' + message.encode()
            [c.conn.sendall(reply) for c in self.client_pool if len(self.client_pool)]

    def run_thread(client):
        print('{} connected with {}:{}'.format(
            client.nick, client.addr[0], str(client.addr[1])))
        message = ''

        try:
            while True:
                data = client.conn.recv(4096)
                message += data.decode()
                if len(data) < 4096:
                    break

        except (ConnectionResetError, BrokenPipeError, OSError):
            client.conn.close()

        self.parser(client.id, client.nick, client.conn, message)
        # for cl in self.client_pool:
        #     cl.conn.sendall(message.encode())

    # build this out::: 
        def run(self):
            print('Server is running on {}'.format(self.port))
            while True: 
            conn, addr = self.server.accept()
            client = ChatClient(conn, addr)
            self.client_pool.append(client)
            threading.Thread(
                target=self.run_thread,
                # add to this
                args=(client,),
                daemon = True
            ).start()

        def exit(self):
            self.server.close()        

    if __name__ == '__main__':
        server = ChatServer(PORT)
        try:
            server.run()
        except KeyboardInterrupt:
            server.exit()
