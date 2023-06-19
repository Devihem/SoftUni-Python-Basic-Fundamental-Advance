from canvas import frame
from hashlib import sha256

def clean_screen():
    frame.delete('all')


def get_password_hash(password):
    hash_object = sha256(password.encode())

    return str(hash_object.hexdigest())

print(get_password_hash("dian1234"))