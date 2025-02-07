import socket
import logging

from src.config import config


logger = logging.getLogger("P2P")

class Proxy:

    def proxy_request(command, args, target_ip):
        logger.info(f"Proxying request: {command} {args} → {target_ip}")
        
        active_port = Proxy._find_port(target_ip)

        if active_port is None:
            logger.warning(f"Failed to find active port for bank {target_ip}")
            return f"ER No active port for bank {target_ip}."

        try:
            print(args)
            with socket.create_connection((target_ip, active_port), timeout=config.PROXY_TIMEOUT) as proxy_socket:
                proxy_socket.sendall(f"{command} {' '.join(args)}".encode(config.FORMAT))
                logger.info(f"Sent command: {command} to {target_ip}:{active_port}")

                response = proxy_socket.recv(1024).decode(config.FORMAT)
                logger.info(f"Received response: {response} from {target_ip}:{active_port}")
                return response
        
        except Exception as e:
            logger.error(f"Error connecting to bank {target_ip}:{active_port} → {e}")
            return f"ER Nelze se spojit s bankou {target_ip}: {e}"
        

    def _find_port(target_ip):
        for port in range(65525, 65535):
            try:
                with socket.create_connection((target_ip, port), timeout=1) as sock:
                    return port 
                
            except (socket.timeout, ConnectionRefusedError):
                continue

        return None