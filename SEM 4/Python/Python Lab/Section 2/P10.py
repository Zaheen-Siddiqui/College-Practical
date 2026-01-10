def analyze_string(text):
    vowels = consonants = spaces = digits = symbols = 0

    for char in text:
        if char.lower() in 'aeiou':
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            symbols += 1

    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Spaces: {spaces}")
    print(f"Digits: {digits}")
    print(f"Special Symbols: {symbols}")

# Get input from the user
input_text = input("Enter a string: ")
analyze_string(input_text)
