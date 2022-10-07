from datetime import datetime
import json
import hashlib

class BlockChain:
    def __init__(self):
        """Initializing chain and creating the genesis block."""

        self.chain = []
        self.create_block(proof=1, previous_hash='0', data='First Block')

    def create_block(self, proof, previous_hash, data):
        """Creates a block which contains index, timestamp, proof, 
        previous hash, data, connects it to the chain and returns the block."""

        block = {
            'index': len(self.chain)+1,
            'timestamp': str(datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'data': data,
        }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        """Returns the previous block."""

        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """Takes in the previous proof and returns a new proof."""

        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        """Returns the hash of a block using SHA256."""

        block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block).hexdigest()

    def is_chain_valid(self):
        """Validates if the chain is not manipulated."""

        previous_block = self.chain[0]

        for block in self.chain[1:]:
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            if self.proof_of_work(previous_block['proof']) != block['proof']:
                return False
            
            previous_block = block

        return True
