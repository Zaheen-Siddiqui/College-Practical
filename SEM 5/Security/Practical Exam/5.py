# affine.py
import string
ALPH = string.ascii_uppercase

def modinv(a, m=26):
    # brute-force modular inverse
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(pt, a, b):
    pt = pt.upper()
    if modinv(a,26) is None:
        raise ValueError('a must be coprime with 26')
    out = []
    for ch in pt:
        if ch in ALPH:
            x = ALPH.index(ch)
            out.append(ALPH[(a*x + b) % 26])
        else:
         out.append(ch)
    return ''.join(out)


def affine_decrypt(ct, a, b):
    inv = modinv(a, 26)
    out = []
    for ch in ct.upper():
        if ch in ALPH:
            y = ALPH.index(ch)
            out.append(ALPH[(inv * (y - b)) % 26])
        else:
            out.append(ch)
    return ''.join(out)


if __name__ == '__main__':
    c = affine_encrypt('HELLO', 5, 8)
    print(c)
    print(affine_decrypt(c, 5, 8))