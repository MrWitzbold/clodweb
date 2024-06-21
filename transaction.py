import json

class Transaction:
    def __init__(self, sender, receiver, amount, signature=""):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
    
    def to_dict(self):
        return self.__dict__
    
    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=True)