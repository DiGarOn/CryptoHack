import requests

cookie = requests.get('https://aes.cryptohack.org/flipping_cookie/get_cookie/').json()['cookie']
check_admin = lambda ciphertext, iv: requests.get(f'https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}/').json()

iv, cookie = bytes.fromhex(cookie[:32]), cookie[32:]

tmp = [b'True;'[i] ^ b'False'[i] for i in range(len(b'True;'))]

def checnge_centre(c, tmp):
    m = c[len('admin='):len('admin=') + len('True;')]
    l = ''.join([hex(m[i]^tmp[i])[2:].zfill(2) for i in range(len(m))])
    return c[:len('admin=')].hex() + l + c[len('admin=') + len('True;'):].hex()

iv = checnge_centre(iv, tmp)
print(requests.get(f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}").json()["flag"])
