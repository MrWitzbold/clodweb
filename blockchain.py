import time
from block import Block
from utils import sha256
from transaction import Transaction

class Blockchain:
    difficulty = 2

    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()
    
    def create_genesis_block(self):
        genesis_block = Block(0, "0", [])
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)
    
    def proof_of_work(self, block):
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash
    
    def add_block(self, block, proof):
        previous_hash = self.get_last_block().hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
    
    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())
    
    def mine(self):
        if not self.pending_transactions:
            return False
        
        last_block = self.get_last_block()
        new_block = Block(index=last_block.index + 1,
                          previous_hash=last_block.hash,
                          transactions=self.pending_transactions)
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.pending_transactions = []
        return new_block
