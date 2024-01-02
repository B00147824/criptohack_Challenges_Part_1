N_ROUNDS = 10

def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    return bytes(sum(matrix, []))

def expand_key(master_key):
   
    pass

def decrypt(key, ciphertext):
    round_keys = expand_key(key)
    state = bytes2matrix(ciphertext)  

    return plaintext

key = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'
plaintext = decrypt(key, ciphertext)
print(plaintext)
