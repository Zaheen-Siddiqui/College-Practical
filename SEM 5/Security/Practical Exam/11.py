# playfair_impl.py
import string

ALPH = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J merged into I

def generate_table(key):
    key = ''.join([c for c in key.upper() if c.isalpha()])
    seen = []
    for ch in key:
        ch = 'I' if ch == 'J' else ch
        if ch not in seen:
            seen.append(ch)
    for ch in ALPH:
        if ch not in seen:
            seen.append(ch)
    table = [seen[i*5:(i+1)*5] for i in range(5)]
    return table

def find_pos(table, ch):
    ch = 'I' if ch == 'J' else ch
    for r in range(5):
        for c in range(5):
            if table[r][c] == ch:
                return r, c
    raise ValueError("Character not in table: " + ch)

def prepare_text_encrypt(pt):
    # remove non-alpha, uppercase, replace J with I, create digraphs with X padding
    pt = ''.join([c for c in pt.upper() if c.isalpha()])
    pt = pt.replace('J', 'I')
    res = []
    i = 0
    while i < len(pt):
        a = pt[i]
        b = pt[i+1] if i+1 < len(pt) else ''
        if b == '':
            res.append(a + 'X')
            i += 1
        elif a == b:
            res.append(a + 'X')
            i += 1
        else:
            res.append(a + b)
            i += 2
    return ''.join(res)

def prepare_text_decrypt(ct):
    # For decrypt, ciphertext should be even-length; we assume correct formatting
    return ''.join([c for c in ct.upper() if c.isalpha()])

def playfair_encrypt(plaintext, key):
    table = generate_table(key)
    txt = prepare_text_encrypt(plaintext)
    ct = []
    for i in range(0, len(txt), 2):
        a, b = txt[i], txt[i+1]
        ra, ca = find_pos(table, a)
        rb, cb = find_pos(table, b)
        if ra == rb:  # same row -> shift right
            ct.append(table[ra][(ca + 1) % 5])
            ct.append(table[rb][(cb + 1) % 5])
        elif ca == cb:  # same column -> shift down
            ct.append(table[(ra + 1) % 5][ca])
            ct.append(table[(rb + 1) % 5][cb])
        else:  # rectangle -> swap columns
            ct.append(table[ra][cb])
            ct.append(table[rb][ca])
    return ''.join(ct)

def playfair_decrypt(ciphertext, key):
    table = generate_table(key)
    txt = prepare_text_decrypt(ciphertext)
    pt = []
    for i in range(0, len(txt), 2):
        a, b = txt[i], txt[i+1]
        ra, ca = find_pos(table, a)
        rb, cb = find_pos(table, b)
        if ra == rb:  # same row -> shift left
            pt.append(table[ra][(ca - 1) % 5])
            pt.append(table[rb][(cb - 1) % 5])
        elif ca == cb:  # same column -> shift up
            pt.append(table[(ra - 1) % 5][ca])
            pt.append(table[(rb - 1) % 5][cb])
        else:  # rectangle -> swap columns
            pt.append(table[ra][cb])
            pt.append(table[rb][ca])
    return ''.join(pt)

if __name__ == '__main__':
    key = "PLAYFAIREXAMPLE"
    plaintext = "HIDE THE GOLD IN THE TREE STUMP"
    ct = playfair_encrypt(plaintext, key)
    print("Ciphertext:", ct)                # expected Labeled style string
    pt = playfair_decrypt(ct, key)
    print("Decrypted (raw):", pt)           # note: may contain X filler chars
