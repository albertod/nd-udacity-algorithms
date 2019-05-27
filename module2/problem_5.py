import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        # Add timestamp to create unique hash
        sha.update(str(self.timestamp).encode('utf-8'))
        # Add also data
        sha.update(str(self.data).encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        return f'Block(hash={self.hash} previous_hash={self.previous_hash} data={self.data} timestamp={self.timestamp}'
        
class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.block_dic = {}

    def add_block(self, data):
        if self.head == None:
            block = self.create_block(data, 0)
            self.head = block
            self.tail = block
            self.block_dic[block.hash] = block
        else:
            block = self.create_block(data, self.tail.hash)
            self.tail = block
            self.block_dic[block.hash] = block

    def __str__(self):
        if self.tail == None:
            return "None"
        cursor = self.tail
        s = '\n\n'
        while cursor is not None and cursor.previous_hash is not 0:
           s += str(cursor)
           s += "\n"
           s += "^\n"
           s += "|\n"
           cursor = self.block_dic[cursor.previous_hash]
        s+=str(cursor)
        s+=str('\n')
        return s

    def create_block(self, data, previous_hash):
        timestamp = time.asctime()
        return Block(timestamp, data, previous_hash)

print("Sample Blockchain")
blockchain = BlockChain()
blockchain.add_block('alberto')
blockchain.add_block('ashley')
blockchain.add_block('omar')
blockchain.add_block('pedro')
print(blockchain)

print("Sample Blockchain 2")
blockchain = BlockChain()
blockchain.add_block('pedro')
print(blockchain)

print("Empty Blockchain")
blockchain = BlockChain()
print(blockchain)
