from utils import generate_key_pair, sign_transaction, verify_signature
from transaction import Transaction

class Wallet:
    def __init__(self):
        self.private_key, self.public_key = generate_key_pair()
        self.balance = 0
    
    def create_transaction(self, receiver, amount):
        transaction = Transaction(sender=self.public_key, receiver=receiver, amount=amount)
        transaction.signature = sign_transaction(self.private_key, transaction.to_json())
        return transaction
    
    def verify_transaction(self, transaction):
        return verify_signature(transaction.sender, transaction.to_json(), transaction.signature)
