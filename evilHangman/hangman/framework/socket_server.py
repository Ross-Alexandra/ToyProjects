import socket
from multiprocessing.pool import ThreadPool

from hangman.hangman import play_game

class HangmanServer:

    def __init__(self, port: int=34360, concurrent_users: int=5, timeout=60):
        self.server_port = port
        self.concurrent_users = concurrent_users

        self.thread_pool = ThreadPool(concurrent_users)
        self.threads_in_use = 0

        self.server = socket.socket()
        self.server.bind(('', self.server_port))

    def increase_used_threads(self):
        self.threads_in_use += 1

    def decrease_used_threads(self, junk):
        print("Closing down thread after successful run.")
        self.threads_in_use -= 1

    def listen(self):
        self.server.listen(self.concurrent_users)

        while True:
            if self.threads_in_use < self.concurrent_users:
                print(f"{self.concurrent_users - self.threads_in_use} threads available. Spinning up new process.")
                self.increase_used_threads()
                self.thread_pool.apply_async(func=self.accept_connection, args=(self.server,), callback=self.decrease_used_threads)

        self.thread_pool.close()
        self.thread_pool.join()

    def handle_user(self, connection, address):
        try:
            print("Getting attempt number")
            self.send(connection, "How many attempts?")
            attempts = int(self.receive(connection))
            print("Getting letter count")
            self.send(connection, "How many letters?")
            letter_count = int(self.receive(connection))
            print("Prompting for print-type")
            self.send(connection, "(if you're a robot) What is the robot password?")
            minimal = str(self.receive(connection)) == "true"

            print(f"Setup a game with the followig parameters: attempts={attempts}, letter_count={letter_count}, minimal={minimal}")

            play_game(lambda x: self.send(connection, x), lambda: self.receive(connection), attempts, letter_count, "hangman/hangman/res/dictionary.txt", minimal)

        except Exception as e:
            connection.send(str(e))
        finally:
            connection.send("terminate_connection")
            connection.close()

    def accept_connection(self, server):
        print("New thread: awaiting connection")
        connection, address = server.accept()
        print(f"Recieved connection from {address}: connection information {connection}")
        try:
            self.handle_user(connection, address)
        except Exception as e:
            print(e)
        
        return

    @staticmethod
    def send(connection, msg):
        connection.send(msg.encode())

    @staticmethod
    def receive(connection):

        received_bytes = connection.recv(1024)
        print(f"Received bytes: {received_bytes}")

        return received_bytes.decode()

if __name__ == "__main__":
    server = HangmanServer()

    server.listen()