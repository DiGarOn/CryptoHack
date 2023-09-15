# The previous set of challenges showed how AES performs a keyed permutation on a block of data. In practice, we need to encrypt messages much longer than a single block. A mode of operation describes how to use a cipher like AES on longer messages.
#
# All modes have serious weaknesses when used incorrectly. The challenges in this category take you to a different section of the website where you can interact with APIs and exploit those weaknesses. Get yourself acquainted with the interface and use it to take your next flag!
#
# Play at https://aes.cryptohack.org/block_cipher_starter

from Crypto.Cipher import AES
import requests
import string


KEY = ''
# FLAG = ?
enc_flag = "403d017e3d4291a7f2105b4296f3656eaa5b794236ef53697c860af50e7eb1c3"


def decrypt(KEY, ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}


# crypto{bl0ck_c1ph3r5_4r3_f457_!}