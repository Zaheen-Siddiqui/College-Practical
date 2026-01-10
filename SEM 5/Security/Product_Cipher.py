S_BOX = [
    [14, 4, 13, 1],
    [10, 15, 7, 6],
    [9, 5, 3, 2],
    [8, 11, 12, 0]
]

# D-Box (Permutation) Example
D_BOX = [3, 1, 4, 2]

# Key Expansion - Split the 8-bit key into two 4-bit parts
def expand_key(key):
    round_keys = [key[:4], key[4:]]
    return round_keys

# S-box substitution
def s_box_substitution(block):
    row = block[0] * 2 + block[1]      # First 2 bits represent row
    col = block[2] * 2 + block[3]      # Last 2 bits represent column
    return [int(x) for x in f"{S_BOX[row][col]:04b}"]  # Convert to 4-bit binary

# D-box permutation
def d_box_permutation(block):
    return [block[D_BOX[i] - 1] for i in range(len(D_BOX))]

# XOR function (XOR two lists of bits)
def xor_block(block, round_key):
    return [block[i] ^ round_key[i] for i in range(len(block))]

# Round function: S-box substitution -> D-box permutation -> XOR with round key
def round_function(block, round_key):
    substituted = s_box_substitution(block)
    permuted = d_box_permutation(substituted)
    return xor_block(permuted, round_key)

# Product cipher encryption (main function)
def product_cipher_encrypt(block, key):
    round_keys = expand_key(key)
    block = block[:4]  # Assume input block is 4 bits
    for round_key in round_keys:
        block = round_function(block, round_key)
    return block

# Test with a 4-bit block and an 8-bit key
key = [1, 0, 1, 0, 1, 1, 0, 1]      # Example 8-bit key
input_block = [0, 1, 1, 0]          # Example 4-bit input block

# Encrypt the input block
ciphertext = product_cipher_encrypt(input_block, key)
print("Ciphertext:", ciphertext)
