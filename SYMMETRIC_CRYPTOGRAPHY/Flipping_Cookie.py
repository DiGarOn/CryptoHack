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

# crypto{4u7h3n71c4710n_15_3553n714l}

# inline solution:
# [print(requests.get(f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie[32:]}/{bytes.fromhex(cookie[:32])[:len('admin=')].hex() + ''.join([hex(bytes.fromhex(cookie[:32])[len('admin='):len('admin=') + len('True;')][i]^[b'True;'[i] ^ b'False'[i] for i in range(len(b'True;'))][i])[2:].zfill(2) for i in range(len(bytes.fromhex(cookie[:32])[len('admin='):len('admin=') + len('True;')]))]) + bytes.fromhex(cookie[:32])[len('admin=') + len('True;'):].hex()}").json()["flag"]) for cookie in [requests.get('https://aes.cryptohack.org/flipping_cookie/get_cookie/').json()['cookie']]]
