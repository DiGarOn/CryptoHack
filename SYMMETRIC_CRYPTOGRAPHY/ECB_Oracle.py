# ECB is the most simple mode, with each plaintext block encrypted entirely independently. In this case, your input is prepended to the secret flag and encrypted and that's it. We don't even provide a decrypt function. Perhaps you don't need a padding oracle when you have an "ECB oracle"?
#
# Play at https://aes.cryptohack.org/ecb_oracle

import requests
from string import printable

url_0 = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'


def broot(fil, res):
    flag = True
    count = len(fil)
    while ('}' not in res):
        if count >= 0:
            for i in printable:
                print(i)
                if flag:
                    url = url_0 + (fil + res + i + fil).encode('ascii').hex()
                    resp = requests.get(url)
                    if resp.json()['ciphertext'][:32] == resp.json()['ciphertext'][32:64]:
                        print(resp.json()['ciphertext'][:32] + '\n' + resp.json()['ciphertext'][32:64] + '\n' + '______________________')
                        res += i
                        print(res)
                        if count:
                            fil = fil[:-1]
                        count -= 1
                        print(len(fil))
                        break
                else:
                    url = url_0 + (res[16-len(fil):] + i + fil).encode('ascii').hex()
                    resp = requests.get(url)
                    if resp.json()['ciphertext'][:32] == resp.json()['ciphertext'][64:96]:
                        print(resp.json()['ciphertext'][:32] + '\n' + resp.json()['ciphertext'][64:96] + '\n' + '______________________')
                        res += i
                        print(res)
                        if count:
                            fil = fil[:-1]
                        count -= 1
                        print(len(fil))
                        break
        else:
            flag = False
            fil = '0' * 15
            count = len(fil)
    return res

res = ''
fil = '0'*15
res += broot(fil, res)

print(res)

# crypto{p3n6u1n5_h473_3cb}
