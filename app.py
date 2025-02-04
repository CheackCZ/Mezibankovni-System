import os 

from src.p2p.node import Node

if __name__ == "__main__":
    node = Node(os.getenv('HOST'), int(os.getenv('PORT')))
    node.start()