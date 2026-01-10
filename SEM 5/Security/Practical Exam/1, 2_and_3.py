# caesar.py
import string


ALPH = string.ascii_uppercase


def caesar_encrypt(plaintext, k):
    res = []
    plaintext = plaintext.upper()
    for ch in plaintext:
        if ch in ALPH:
            res.append(ALPH[(ALPH.index(ch) + k) % 26])
        else:
            res.append(ch)
    return ''.join(res)

def caesar_decrypt(ciphertext, k):
    return caesar_encrypt(ciphertext, -k % 26)

if __name__ == '__main__':
    print(caesar_encrypt('HELLO WORLD', 3)) # KHOOR ZRUOG
    print(caesar_decrypt('KHOOR ZRUOG', 3))