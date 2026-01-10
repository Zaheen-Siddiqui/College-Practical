# RSA Implementation in Python

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Step 1: Generate RSA key pair
key = RSA.generate(2048)

public_key = key.publickey()
private_key = key

# Step 2: Prepare plaintext
plaintext = ("This is a sample plaintext message to be encrypted and decrypted using RSA.\n")

# Step 3: Encrypt using public key
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(plaintext.encode())

print("Encrypted Ciphertext (Base64):", ciphertext.hex())

# Step 4: Decrypt using private key
decipher = PKCS1_OAEP.new(private_key)
decrypted = decipher.decrypt(ciphertext).decode()

print("\nDecrypted Plaintext:\n", decrypted)
