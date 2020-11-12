import random
from posix import urandom
from base64 import b64encode

random_bytes = urandom(512)
token = b64encode(random_bytes).decode('utf-8')
print(token)
