from fastapi import FastAPI
from blockchain import BlockChain

app = FastAPI()

blockchain = BlockChain()

@app.get('/')
def mine(data):
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    return blockchain.create_block(proof, blockchain.hash(previous_block), data)

@app.get('/chain')
def get_chain():
    return blockchain.chain

@app.get('/is_chain_valid')
def is_chain_valid():
    return blockchain.is_chain_valid()
