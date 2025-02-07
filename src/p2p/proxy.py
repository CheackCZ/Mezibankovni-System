import socket
from src.config import config

class Proxy:

    def proxy_request(command, args, target_ip):
        active_port = Proxy._find_port(target_ip)

        print(f"{command}, {args}, {target_ip}")

        if active_port is None:
            return f"ER No active port for bank {target_ip}."

        try:
            print(args)
            with socket.create_connection((target_ip, active_port), timeout=config.PROXY_TIMEOUT) as proxy_socket:
                proxy_socket.sendall(f"{command} {' '.join(args)}".encode(config.FORMAT))

                response = proxy_socket.recv(1024).decode(config.FORMAT)
                return response
        
        except Exception as e:
            return f"ER Nelze se spojit s bankou {target_ip}: {e}"
        

    def _find_port(target_ip):
        for port in range(65525, 65535):
            try:
                with socket.create_connection((target_ip, port), timeout=1) as sock:
                    return port 
                
            except (socket.timeout, ConnectionRefusedError):
                continue

        return None