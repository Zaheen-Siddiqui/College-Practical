# autokey.py
import string
ALPH = string.ascii_uppercase


def autokey_encrypt(pt, key):
    pt = ''.join([c for c in pt.upper() if c in ALPH])
    key = key.upper()
    keystream = list(key)
    i = 0
    while len(keystream) < len(pt):
        keystream.append(pt[i])
        i += 1
    ct = []
    for p,k in zip(pt, keystream):
        ct.append(ALPH[(ALPH.index(p) + ALPH.index(k)) % 26])
    return ''.join(ct)


def autokey_decrypt(ct, key):
    ct = ''.join([c for c in ct.upper() if c in ALPH])
    key = key.upper()
    keystream = list(key)
    pt = []
    for c in ct:
        k = keystream.pop(0)
        p = ALPH[(ALPH.index(c) - ALPH.index(k)) % 26]
        pt.append(p)
        keystream.append(p)
    return ''.join(pt)


if __name__ == '__main__':
    c = autokey_encrypt('ATTACKATDAWN', 'QUEEN')
    print(c)
    print(autokey_decrypt(c, 'QUEEN'))