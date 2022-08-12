# Module 1 - Create a Blockchain

# Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1- Building a Blockchain
class Blockchain:
	def __init__(self):
    	self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
    	block = {'index' : len(self.chain) + 1,
    			'timestamp' : str(datetime.datetime.now()),
    			'proof' : proof,
        		'previous_hash' : previous_hash}
        self.chain.append(block)
        return block

	def get_previous_block(self):
    	return self.chain[-1]

	def proof_of_work(self, previous_proof):
    	new_proof = 1
        check_proof = False
        while check_proof is False:
        	hash_operation = hashlib.sha256(str(new_proof**2 + previous_proof**2).encode()).hexdigest(
            if hash_operation[:4] == '0000':
            	check_proof = True
            else:
            	new_proof += 1

	def is_chain_valid(self, chain):
    	previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
        	block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
            	return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 + previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
            	return False
            privouse_block = block
            block_index += 1
        return True

# Part 2 - Mining our Blockchain

# Creating a web App
app = Flask(__name__)

# Creaging a Blockchain
Blockchain = Blockchain()

# Mining a new block
@app.route("/mine_block")