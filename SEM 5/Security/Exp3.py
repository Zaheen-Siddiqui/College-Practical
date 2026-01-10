# Function to print the Playfair matrix
def print_matrix(matrix):
    print("Playfair Cipher Matrix:")
    for row in matrix:
        print("[", ' '.join(row), "]")

def generate_key_matrix(key):
    key = key.upper().replace("J", "I").replace(" ", "")
    result = []
    for char in key:
        if char not in result:
            result.append(char)

    # Fill remaining letters (A-Z, excluding J)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in result:
            result.append(char)

    # Create 5x5 matrix
    matrix = [result[i:i+5] for i in range(0, 25, 5)]
    return matrix


def preprocess_text(text, for_encryption=True):
    text = text.upper().replace("J", "I").replace(" ", "")
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = 'X'
        if i+1 < len(text):
            b = text[i+1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            i += 1
        digraphs.append(a + b)
    return digraphs


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_encrypt(plain_text, key):
    matrix = generate_key_matrix(key)
    digraphs = preprocess_text(plain_text)
    cipher_text = ""
    for pair in digraphs:
        cipher_text += encrypt_pair(matrix, pair[0], pair[1])
    return cipher_text


def playfair_decrypt(cipher_text, key):
    matrix = generate_key_matrix(key)
    digraphs = preprocess_text(cipher_text, for_encryption=False)
    plain_text = ""
    for pair in digraphs:
        plain_text += decrypt_pair(matrix, pair[0], pair[1])
    return plain_text


# ==== MAIN PROGRAM ====
if __name__ == "__main__":
    key = input("Enter key: ")
    message = input("Enter message to encrypt: ")

    matrix = generate_key_matrix(key)
    print_matrix(matrix)

    encrypted = playfair_encrypt(message, key)
    print("Encrypted Text:", encrypted)

    decrypted = playfair_decrypt(encrypted, key)
    print("Decrypted Text:", decrypted)
    
    