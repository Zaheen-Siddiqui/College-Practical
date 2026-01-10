# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to square root of the number
        if num % i == 0:
            return False  # Not a prime number if divisible by any number in the range
    return True  # Prime number

# Function to get user input and print prime numbers within a given range
def prime_numbers_in_range():
    while True:
        try:
            # Get starting and ending numbers from user
            start = int(input("Enter starting number (positive integer): "))
            end = int(input("Enter ending number (positive integer): "))
            
            # Input validation
            if start < 0 or end < 0:
                raise ValueError("Numbers must be non-negative.")
            if end < start:
                raise ValueError("Ending number must be greater than or equal to starting number.")
            break  # Exit loop if inputs are valid
        except ValueError as e:
            print(f"Invalid input: {e}")  # Show error and re-prompt

    # Display prime numbers in the given range
    print(f"\nPrime numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")

# Run the prime number range function
prime_numbers_in_range()