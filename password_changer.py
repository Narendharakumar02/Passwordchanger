import os
import hashlib


def salt_gen():
    return os.urandom(16)

def hashing(password,salt):
    hashed =  hashlib.sha256(password.encode() + salt).hexdigest()
    return hashed 

def changer():
    passwd = 