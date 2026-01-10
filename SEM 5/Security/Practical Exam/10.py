# hill.py
import numpy as np
import string
ALPH = string.ascii_uppercase


def egcd(a,b):
    if b==0:
       return (1,0,a)
    x,y,g = egcd(b, a%b)
    return (y, x - (a//b)*y, g)


def modinv(a,m):
    x,y,g = egcd(a,m)
    if g != 1:
        return None
    return x % m


def matrix_mod_inv(matrix, mod=26):
    det = int(round(np.linalg.det(matrix)))
    inv_det = modinv(det % mod, mod)
    if inv_det is None:
        return None
    # adjugate
    adj = np.array([[matrix[1,1], -matrix[0,1]], [-matrix[1,0], matrix[0,0]]])
    inv = (inv_det * adj) % mod
    return inv.astype(int)


def hill_encrypt(pt, K):
    pt = ''.join([c for c in pt.upper() if c in ALPH])
    if len(pt) % 2 == 1:
        pt += 'X'
    ct = ''
    for i in range(0, len(pt), 2):
        vec = np.array([ALPH.index(pt[i]), ALPH.index(pt[i+1])])
        prod = K.dot(vec) % 26
        ct += ALPH[prod[0]] + ALPH[prod[1]]
    return ct


def hill_decrypt(ct, K):
    invK = matrix_mod_inv(K)
    if invK is None:
        raise ValueError('Key matrix not invertible mod 26')
    pt = ''
    for i in range(0, len(ct), 2):
        vec = np.array([ALPH.index(ct[i]), ALPH.index(ct[i+1])])
        prod = invK.dot(vec) % 26
        pt += ALPH[prod[0]] + ALPH[prod[1]]
    return pt


if __name__ == '__main__':
    K = np.array([[3,3],[2,5]])
    c = hill_encrypt('HELP', K)
    print(c)
    print(hill_decrypt(c, K))