import socket
import threading

class Node:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connections = []        


    def start(self):
        thread = threading.Thread(target=self.listen)
        thread.start()


    def connect(self, host: str, port: int):
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((host, port))
            
            self.connections.append(connection)

            print(f"Connected to {host}:{port}")

        except Exception as e:
            print(f"Error connecting to {host}:{port}: {e}")

    def listen(self):
        self.sock.bind((self.host, self.port))        
        self.sock.listen(5)
        print(f"Listening on {self.host}:{self.port}")

        while True:
            conn, addr = self.sock.accept()
            self.connections.append(conn)

            print(f"Connected to {addr[0]}:{addr[1]}")

            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

    def handle_client(self, conn, addr):
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break  

                message = data.decode('utf-8')
                self.handle_message(message, conn, addr)

            except:
                break

        conn.close()
        self.connections.remove(conn)
        print(f"Connection closed: {addr[0]}:{addr[1]}")