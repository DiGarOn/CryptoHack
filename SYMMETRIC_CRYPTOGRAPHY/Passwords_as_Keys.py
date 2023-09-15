# It is essential that keys in symmetric-key algorithms are random bytes, instead of passwords or other predictable data. The random bytes should be generated using a cryptographically-secure pseudorandom number generator (CSPRNG). If the keys are predictable in any way, then the security level of the cipher is reduced and it may be possible for an attacker who gets access to the ciphertext to decrypt it.
#
# Just because a key looks like it is formed of random bytes, does not mean that it necessarily is. In this case the key has been derived from a simple password using a hashing function, which makes the ciphertext crackable.
#
# For this challenge you may script your HTTP requests to the endpoints, or alternatively attack the ciphertext offline. Good luck!
#
# Play at https://aes.cryptohack.org/passwords_as_keys

from Crypto.Cipher import AES
import hashlib
import random


FLAG =  "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


def brute(ciphertext):
    for word in open("../words.txt", 'r'):
        word = word.replace("\n", "")

        word = hashlib.md5(word.encode()).hexdigest()
        # print(decrypt(FLAG, word))
        # print(word?)
        tmp = decrypt(FLAG, word)
        # print(bytes.fromhex(tmp['plaintext']))
        # print(bytes("crypto{", encoding="utf-8"))
        if bytes("crypto{", encoding='utf-8') in bytes.fromhex(tmp['plaintext']):
            print(word)
            print(bytes.fromhex(tmp['plaintext']))
            # print(tmp)

brute(FLAG)

# crypto{k3y5__r__n07__p455w0rdz?}
