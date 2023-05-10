import hashlib
import json
from time import time
from flask import Flask, jsonify, request
import requests


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, [], time(), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
    def print_blockchain(self):
        for block in self.chain:
            print("Block index:", block.index)
            print("Block hash:", block.hash)
            print("Block timestamp:", block.timestamp)
            print("Block transactions:", block.transactions)
            print("Block previous hash:", block.previous_hash)
            print("\n")

# Create a new blockchain
#blockchain = Blockchain()

# Add some blocks to the chain
#blockchain.add_block(Block(1, ["Baseline equals"], time(), blockchain.get_latest_block().hash))
#blockchain.add_block(Block(2, ["Naive Bayes equals "], time(), blockchain.get_latest_block().hash))
#blockchain.add_block(Block(3, ["SVM equals"], time(), blockchain.get_latest_block().hash))

# Print the blockchain
#blockchain.print_blockchain()

app = Flask(__name__)
blockchain = Blockchain()

@app.route("/blockchain", methods=["GET"])
def get_blockchain():
    blockchain_data = []
    for block in blockchain.chain:
        block_data = {
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": block.transactions,
            "hash": block.hash,
            "previous_hash": block.previous_hash
        }
        blockchain_data.append(block_data)
    return jsonify(blockchain_data), 200

@app.route("/blockchain/add_block", methods=["POST"])
def add_block():
    request_data = request.get_json()
    transactions = request_data["transactions"]
    new_block = Block(len(blockchain.chain), transactions, time(), "")
    blockchain.add_block(new_block)
    response = {"message": "Block added successfully"}
    return jsonify(response), 201

if __name__ == "__main__":
    app.run(debug=True)



