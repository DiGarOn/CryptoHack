# Let a and b be positive integers.
#
# The extended Euclidean algorithm is an efficient way to find integers u,v such that
#
# a * u + b * v = gcd(a,b)
#
#  Later, when we learn to decrypt RSA, we will need this algorithm to calculate the modular inverse of the public exponent.
#
#
# Using the two primes p = 26513, q = 32321, find the integers u,v such that
#
# p * u + q * v = gcd(p,q)
#
# Enter whichever of u and v is the lower number as the flag.
#
#  Knowing that p,q are prime, what would you expect gcd(p,q) to be? For more details on the extended Euclidean algorithm, check out this page.

def extended_gcd(a, b):
    if not b:
        return (1, 0, a)

    y, x, g = extended_gcd(b, a % b)
    return (x, y - (a//b)*x, g)

print(min(extended_gcd(26513, 32321)[0], extended_gcd(26513, 32321)[1]))

# -8404