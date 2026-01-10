# multiplicative.py
import string

ALPH = string.ascii_uppercase

from math import gcd

def modinv(a, m=26):
    # brute-force modular inverse
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def multiplicative_encrypt(pt, a):
    pt = pt.upper()
    if gcd(a, 26) != 1:
        raise ValueError('a must be coprime with 26')
    out = []
    for ch in pt:
        if ch in ALPH:
            out.append(ALPH[(a * ALPH.index(ch)) % 26])
        else:
            out.append(ch)
    return ''.join(out)


def multiplicative_decrypt(ct, a):
    inv = modinv(a, 26)
    if inv is None:
        raise ValueError('No modular inverse')
    ct = ct.upper()
    out = []
    for ch in ct:
        if ch in ALPH:
            out.append(ALPH[(inv * ALPH.index(ch)) % 26])
        else:
            out.append(ch)
    return ''.join(out)


if __name__ == '__main__':
    c = multiplicative_encrypt('HELLO', 5)
    print(c)
    print(multiplicative_decrypt(c, 5))