cipher_text = "slaz tlla avupnoa ha aol whyr"
def caesar_decrypt(cipher, shift):
    result = ""
    for char in cipher:
        if char.isalpha():
            # shift preserving lowercase
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Try all 26 shifts
for s in range(26):
    print(f"Shift {s}: {caesar_decrypt(cipher_text, s)}")




