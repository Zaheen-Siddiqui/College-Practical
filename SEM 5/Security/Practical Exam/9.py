# columnar_transposition.py
import math


def columnar_encrypt(pt, key):
    pt = pt.replace(' ', '')
    key = key.upper()

    cols = len(key)
    rows = math.ceil(len(pt) / cols)

    # Fill the table row by row
    table = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(pt):
                table[r][c] = pt[idx]
                idx += 1
            else:
                table[r][c] = 'X'   # padding

    # Determine column order based on sorted key
    order = sorted([(char, i) for i, char in enumerate(key)])

    # Read columns in sorted-key order
    ct = ''
    for _, col in order:
        for r in range(rows):
            ct += table[r][col]

    return ct


def columnar_decrypt(ct, key):
    ct = ct.replace(' ', '')
    key = key.upper()

    cols = len(key)
    rows = math.ceil(len(ct) / cols)

    # Determine column order
    order = sorted([(char, i) for i, char in enumerate(key)])

    # Prepare empty table
    table = [['' for _ in range(cols)] for _ in range(rows)]

    # Fill columns according to sorted-key order
    idx = 0
    for _, col in order:
        for r in range(rows):
            if idx < len(ct):
                table[r][col] = ct[idx]
                idx += 1

    # Read table row by row to reconstruct plaintext
    pt = ''
    for r in range(rows):
        for c in range(cols):
            pt += table[r][c]

    return pt.rstrip('X')   # remove padding


if __name__ == '__main__':
    ciphertext = columnar_encrypt('WEAREDISCOVERED', 'ZEBRAS')
    print("Encrypted:", ciphertext)

    plaintext = columnar_decrypt(ciphertext, 'ZEBRAS')
    print("Decrypted:", plaintext)
