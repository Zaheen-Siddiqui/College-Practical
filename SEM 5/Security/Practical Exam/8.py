    # railfence.py


def railfence_encrypt(pt, rails):
    if rails <= 1:
        return pt
    pt = pt.replace(' ', '')
    fence = ['' for _ in range(rails)]
    row = 0
    step = 1
    for ch in pt:
        fence[row] += ch
        row += step
        if row == 0 or row == rails - 1:
            step *= -1
    return ''.join(fence)


def railfence_decrypt(ct, rails):
    if rails <= 1:
        return ct
    n = len(ct)
    # Determine pattern lengths
    pattern = [0]*rails
    row = 0
    step = 1
    for i in range(n):
        pattern[row] += 1
        row += step
        if row == 0 or row == rails-1:
            step *= -1
    # slice ct according to pattern
    parts = []
    idx = 0
    for p in pattern:
        parts.append(ct[idx:idx+p])
        idx += p
    # reconstruct
    res = []
    pointers = [0]*rails
    row = 0
    step = 1
    for i in range(n):
        res.append(parts[row][pointers[row]])
        pointers[row] += 1
        row += step
        if row == 0 or row == rails-1:
            step *= -1
    return ''.join(res)


if __name__ == '__main__':
    c = railfence_encrypt('WEAREDISCOVERED', 3)
    print(c)
    print(railfence_decrypt(c, 3))