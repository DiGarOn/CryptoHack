# For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.
#
# I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.
#
# 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

from pwn import xor

start = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
# if b'crypto' in xor(start, i)
print([xor(start, i).decode('utf-8') for i in range(256) if b'CRYPTO{' in xor(start, i) or b'crypto{' in xor(start, i)][0])

# crypto{0x10_15_my_f4v0ur173_by7e}