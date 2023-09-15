# DESCRIPTION
# Here you can encrypt in CBC but only decrypt in ECB. That shouldn't be a weakness because they're different modes... right?
#

# HELP
# This page offers a convenient way for you to interact with the challenge functions. You can also use GET requests to send and receive data directly from the listed routes/endpoints if you wish. For more information see the FAQ.
#
# Your aim is to recover the FLAG value. Once you have it, submit it on the CryptoHack Symmetric Ciphers page.

#
# from Crypto.Cipher import AES
#
#
# # KEY = ?
# # FLAG = ?
#
#
# # @chal.route('/ecbcbcwtf/decrypt/<ciphertext>/')
# def decrypt(ciphertext):
#     ciphertext = bytes.fromhex(ciphertext)
#
#     cipher = AES.new(KEY, AES.MODE_ECB)
#     try:
#         decrypted = cipher.decrypt(ciphertext)
#     except ValueError as e:
#         return {"error": str(e)}
#
#     return {"plaintext": decrypted.hex()}
#
#
# @chal.route('/ecbcbcwtf/encrypt_flag/')
# def encrypt_flag():
#     iv = os.urandom(16)
#
#     cipher = AES.new(KEY, AES.MODE_CBC, iv)
#     encrypted = cipher.encrypt(FLAG.encode())
#     ciphertext = iv.hex() + encrypted.hex()
#
#     return {"ciphertext": ciphertext}

import requests

ciphertext = "0b11099b5ff3da63a90a08fe9b68e1e75f48ad178f6b63a31e5ca8c1b4527bcc547ecf1de3a044500ff7dd616e7b1748"
# print(len(ciphertext))

url_0 = "https://aes.cryptohack.org/ecbcbcwtf/decrypt/"
res = ''

for i in range(32, len(ciphertext) - 32 + 1, 32):
    resp = requests.get((url_0 + ciphertext[i:i+32])).json()['plaintext']
    res += hex(int(resp, 16) ^ int(ciphertext[i-32:i],16))[2:]

print(bytes.fromhex(res))