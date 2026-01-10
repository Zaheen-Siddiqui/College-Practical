# vigenere.py
import string
ALPH = string.ascii_uppercase


def vigenere_encrypt(pt, key):
    pt = ''.join([c for c in pt.upper() if c in ALPH])
    key = ''.join([c for c in key.upper() if c in ALPH])
    ct = []
    for i, ch in enumerate(pt):
        k = key[i % len(key)]
        ct.append(ALPH[(ALPH.index(ch) + ALPH.index(k)) % 26])
    return ''.join(ct)


def vigenere_decrypt(ct, key):
    key = ''.join([c for c in key.upper() if c in ALPH])
    pt = []
    for i, ch in enumerate(ct.upper()):
        k = key[i % len(key)]
        pt.append(ALPH[(ALPH.index(ch) - ALPH.index(k)) % 26])
    return ''.join(pt)


if __name__ == '__main__':
    print(vigenere_encrypt('ATTACKATDAWN', 'LEMON'))
    print(vigenere_decrypt('LXFOPVEFRNHR', 'LEMON'))