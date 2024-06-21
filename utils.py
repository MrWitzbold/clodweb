import hashlib
import json
import time
import binascii
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return binascii.hexlify(private_key).decode('ascii'), binascii.hexlify(public_key).decode('ascii')

def sign_transaction(private_key, transaction_data):
    key = RSA.import_key(binascii.unhexlify(private_key))
    h = SHA256.new(transaction_data.encode())
    signature = pkcs1_15.new(key).sign(h)
    return binascii.hexlify(signature).decode('ascii')

def verify_signature(public_key, transaction_data, signature):
    key = RSA.import_key(binascii.unhexlify(public_key))
    h = SHA256.new(transaction_data.encode())
    try:
        pkcs1_15.new(key).verify(h, binascii.unhexlify(signature))
        return True
    except (ValueError, TypeError):
        return False
