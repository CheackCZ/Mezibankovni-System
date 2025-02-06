from src.config import config
from src.p2p.node import Node

if __name__ == "__main__":
    try:
        node = Node(config.HOST, config.PORT)
        node.start()
    except ValueError as ve:
        print(f"{ve}")