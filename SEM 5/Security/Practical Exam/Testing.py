# railfence using pycipher
from pycipher.railfence import Railfence
cipher = Railfence(key=3)
ciphertext = cipher.encipher("WEAREDISCOVEREDFLEEATONCE")
print("Ciphertext:", ciphertext)
plaintext = cipher.decipher(ciphertext)
print("Plaintext:", plaintext)      