import hashlib
import sys

key = sys.stdin.read().strip()

hash = ''
i = 0

while True:
    hash = hashlib.md5(f"{key}{i}".encode('utf-8')).hexdigest()
    if hash[0:5] == '00000':
        print( f"*1: {i}" )
        break
    i = i+1

while True:
    hash = hashlib.md5(f"{key}{i}".encode('utf-8')).hexdigest()
    if hash[0:6] == '000000':
        print( f"*2: {i}" )
        break
    i = i+1
