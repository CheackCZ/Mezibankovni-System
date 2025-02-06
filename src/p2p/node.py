import socket
import multiprocessing

from src.config import config
from src.controllers.command_controller import CommandController
from src.logger import setup_logger

class Node:
    """
    Represents a node in a P2P network, responsible for establishing connections, listening for incoming requests, and handling client communication.
    """

    logger = setup_logger()

    def __init__(self, host: str, port: int):
        """
        Initializes a P2P node.

        :param host (str): The IP address or hostname where the node will run.
        :param port (int): The port number for incoming connections.
        """
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = [] 

        self.command_controller = CommandController()

        self.logger.info("Node was instantiated successfully on %s:%d.", host, port)


    def start(self):
        """
        Starts the node's listener process in a separate process.
        """
        process = multiprocessing.Process(target=self.listen)
        process.run()


    def connect(self, host: str, port: int):
        """
        Connects to another P2P node.

        :param host (str): The IP address or hostname of the target node.
        :param port (int): The port number of the target node.
        """
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.settimeout(config.TIMEOUT)
            connection.connect((host, port))
            
            self.connections.append(connection)

            self.logger.info("Connected to node %s:%d", host, port)

        except socket.timeout:
            self.logger.warning(f"Connection to {host}:{port} timed out after {config.TIMEOUT} seconds.")
            raise TimeoutError(f"Connection to {host}:{port} timed out after {config.TIMEOUT} seconds.")

        except Exception as e:
            self.logger.error("Error connecting to %s:%d: %s", host, port, e)
            raise TimeoutError(f"Connection to {host}:{port} timed out after {config.TIMEOUT} seconds.")

    def listen(self):
        """
        Listens for incoming connections and spawns a new process to handle each client.
        """
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
        """
        Handles communication with a connected client.

        :param conn (socket.socket): The client's socket connection.
        :param addr (tuple): The client's (IP, port) tuple.
        """
        self.welcome_message(conn, addr)       

        conn.settimeout(config.TIMEOUT) 

        while True:
            try:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break  

                data_stripped = data.strip()

                if not data_stripped:  
                    conn.sendall(b"\r> ")  
                    continue

                parts = data_stripped.split()
                command = parts[0]
                args = parts[1:]

                response = self.command_controller.execute(command, args)

                formatted_response = response.strip() + "\r\n\r\n> "
                conn.sendall(formatted_response.encode('utf-8'))

            except Exception as e:
                self.logger.error(f"Error handling client {addr}: {e}")
                conn.sendall(f"\r\nER: {e}".encode('utf-8'))
                break

        conn.close()
        self.connections.remove(conn)
        self.logger.info("Connection closed on node: %s:%d", addr[0], addr[1])

    def welcome_message(self, conn, addr):
        """
        Sends a welcome message to a newly connected client.

        :param conn (socket.socket): The client's socket connection.
        :param addr (tuple): The client's (IP, port) tuple.
        """
        try:
            welcome_message = "Welcome to the P2P Node! Enter your command below:\r\n> "
            conn.sendall(welcome_message.encode('utf-8'))

        except Exception as e:
            self.logger.error("Error sending welcome message to client %s: %s", addr, e)
            conn.close()
            return