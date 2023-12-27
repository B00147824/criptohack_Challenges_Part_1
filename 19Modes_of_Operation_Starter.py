import requests


r = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
res = r.json()['ciphertext']



endpointdec = 'http://aes.cryptohack.org/block_cipher_starter/decrypt/' + res
dec = requests.get(endpointdec)
res1 = dec.json()['plaintext']


by = bytes.fromhex(res1)
finalres = by.decode()
print(finalres)
