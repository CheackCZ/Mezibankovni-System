import socket
import multiprocessing

from src.controllers.command_controller import CommandController
from src.logger import setup_logger

class Node:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connections = [] 

        self.command_controller = CommandController()

        self.logger = setup_logger()
        self.logger.info("Node was instantiated successfully on %s:%d.", host, port)


    def start(self):
        process = multiprocessing.Process(target=self.listen)
        process.run()


    def connect(self, host: str, port: int):
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((host, port))
            
            self.connections.append(connection)

            self.logger.info("Connected to node %s:%d", host, port)

        except Exception as e:
            self.logger.error("Error connecting to %s:%d: %s", host, port, e)

    def listen(self):
        self.sock.bind((self.host, self.port))        
        self.sock.listen(5)
        self.logger.info("Listening on %s:%d", self.host, self.port)

        while True:
            conn, addr = self.sock.accept()
            self.connections.append(conn)

            self.logger.info("Connected to %s:%d", addr[0], addr[1])

            process = multiprocessing.Process(target=self.handle_client, args=(conn, addr), daemon=True)
            process.start()


    def handle_client(self, conn, addr):
        self.welcome_message(conn, addr)        

        while True:
            try:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break  

                data = data.strip()
                if not data:
                    continue

                parts = data.split()
                if not parts:
                    continue

                parts = data.strip().split()
                command = parts[0]
                args = parts[1:]

                response = self.command_controller.execute(command, args)
                conn.sendall(response.encode('utf-8'))

            except Exception as e:
                self.logger.error(f"Error handling client {addr}: {e}")
                conn.sendall(f"ER: {e}".encode('utf-8'))
                break

        conn.close()
        self.connections.remove(conn)
        self.logger.info("Connection closed on node: %s:%d", addr[0], addr[1])


    def welcome_message(self, conn, addr):
        try:
            welcome_message = "Welcome to the P2P Node! Enter your command below:\r\n> "
            conn.sendall(welcome_message.encode('utf-8'))

        except Exception as e:
            self.logger.error("Error sending welcome message to client %s: %s", addr, e)
            conn.close()
            return