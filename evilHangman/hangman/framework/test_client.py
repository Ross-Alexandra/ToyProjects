from multiprocessing.pool import ThreadPool
import socket


class HangmanClient:

    def __init__(self, server_location: str="localhost", server_port: int=34360):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server_location
        self.port = server_port

        self.connected = False

    def connect_IO(self):
        self.connect()

        pool = ThreadPool(1)
        pool.apply_async(self.listen)

        while self.connected:
            msg = str(input())
            if self.connected:
                self.send_msg(msg)

    def listen(self):
        while self.connected:
            msg = self.receive_msg()
            if msg == "terminate_connection" or not msg:
                self.disconnect()

            print(msg)

    def connect(self):
        self.connected = True
        self.socket.connect((self.server, self.port))

    def send_msg(self, msg):
        self.socket.send(msg.encode())

    def receive_msg(self):
        return self.socket.recv(1024).decode()

    def disconnect(self):
        self.connected = False
        self.socket.close()

if __name__ == "__main__":
    client = HangmanClient()

    client.connect_IO()