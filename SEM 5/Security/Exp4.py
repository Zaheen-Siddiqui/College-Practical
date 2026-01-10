# Define a simple S-Box (4-bit input, 4-bit output)
S_BOX = {
    "0000": "1110",
    "0001": "0100",
    "0010": "1101",
    "0011": "0001",
    "0100": "0010",
    "0101": "1111",
    "0110": "1011",
    "0111": "1000",
    "1000": "0011",
    "1001": "1010",
    "1010": "0110",
    "1011": "1100",
    "1100": "0101",
    "1101": "1001",
    "1110": "0000",
    "1111": "0111",
}

# Define a simple D-Box (Permutation box) for 8-bit block
D_BOX = [1, 3, 0, 2, 5, 7, 4, 6]


# Substitution function using S-Box
def substitute(block):
    left = block[:4]
    right = block[4:]
    return S_BOX[left] + S_BOX[right]


# Permutation function using D-Box
def permute(block):
    return "".join(block[i] for i in D_BOX)


# XOR with key for key mixing
def xor_with_key(block, key):
    return "".join("1" if block[i] != key[i] else "0" for i in range(len(block)))


# Main function to perform 2 rounds of Product Cipher
def product_cipher_encrypt(plaintext, key, rounds=2):
    block = plaintext
    for round in range(rounds):
        print(f"\n🔁 Round {round + 1}")
        block = substitute(block)
        print("After Substitution :", block)
        block = permute(block)
        print("After Permutation  :", block)
        block = xor_with_key(block, key)
        print("After XOR with Key :", block)
    return block


# Sample input (8-bit binary strings)
plaintext = "11010111"
key = "10101010"

print("Plaintext:", plaintext)
print("Key      :", key)

ciphertext = product_cipher_encrypt(plaintext, key)
print("\n🔐 Final Ciphertext:", ciphertext)