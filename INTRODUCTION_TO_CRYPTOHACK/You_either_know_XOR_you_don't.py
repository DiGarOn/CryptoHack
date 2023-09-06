# I've encrypted the flag with my secret key, you'll never be able to guess it.
#
# Remember the flag format and how it might help you in this challenge!
#
#
# 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

from pwn import xor
from string import printable

start = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

print(xor(start, xor(b'crypto{', start[:len('crypto{')]) + b'y').decode('utf-8'))

# crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}