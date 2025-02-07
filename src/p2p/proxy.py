import socket
import logging

from src.config import config


logger = logging.getLogger("P2P")

class Proxy:
    """
    A utility class for handling proxy communication between bank nodes in a P2P network.
    """

    def proxy_request(command, args, target_ip):
        """
        Proxies a request to another bank node in the network. Attempts to connect to a target bank node, forwards a command, and returns the response.

        :param command (str): The command to be executed on the remote bank node.
        :param args (list): A list of arguments required for the command.
        :param target_ip (str): The IP address of the target bank node.

        :return: response from the remote bank node or an error message if the connection fails.
        """
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
        """
        Finds an active port on the target bank node ip address.

        :param target_ip (str): The IP address of the target bank node.
        """
        for port in range(65525, 65535):
            try:
                with socket.create_connection((target_ip, port), timeout=1) as sock:
                    return port 
                
            except (socket.timeout, ConnectionRefusedError):
                continue

        return None