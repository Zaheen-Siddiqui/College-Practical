# rsa_impl.py
import random
from math import gcd

def is_probable_prime(n, k=8):
    # Miller-Rabin primality test (k rounds)
    if n < 2:
        return False
    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    # write n-1 as d * 2^s
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    def trial(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if not trial(a):
            return False
    return True

def gen_prime(bits):
    while True:
        candidate = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_probable_prime(candidate):
            return candidate

def egcd(a, b):
    if b == 0:
        return (1, 0, a)
    x, y, g = egcd(b, a % b)
    return (y, x - (a // b) * y, g)

def modinv(a, m):
    x, y, g = egcd(a, m)
    if g != 1:
        return None
    return x % m

def generate_rsa_keys(bits=512):
    # For demo, default 512 bits; use >=2048 in real life.
    p = gen_prime(bits // 2)
    q = gen_prime(bits // 2)
    while q == p:
        q = gen_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = modinv(e, phi)
    if d is None:
        raise Exception("Failed to compute modular inverse for e")
    return {'public': (e, n), 'private': (d, n), 'p': p, 'q': q}

def rsa_encrypt(m_int, pub):
    e, n = pub
    if m_int < 0 or m_int >= n:
        raise ValueError("Message integer out of range")
    return pow(m_int, e, n)

def rsa_decrypt(c_int, priv):
    d, n = priv
    return pow(c_int, d, n)

# convenience helpers for small messages -> integer
def str_to_int(msg: bytes) -> int:
    return int.from_bytes(msg, byteorder='big')

def int_to_str(i: int) -> bytes:
    length = (i.bit_length() + 7) // 8
    return i.to_bytes(length, byteorder='big')

if __name__ == '__main__':
    # Demo (small message). Warning: This demo uses small bit sizes for speed.
    keys = generate_rsa_keys(bits=512)   # try 1024/2048 for more realistic tests (slow)
    pub = keys['public']
    priv = keys['private']
    print("Public key (e,n) bitlen n:", pub[1].bit_length())
    msg = b'Hello'
    m_int = str_to_int(msg)
    c = rsa_encrypt(m_int, pub)
    print(c)
    m2 = rsa_decrypt(c, priv)
    print("Original:", msg)
    print("Recovered:", int_to_str(m2))