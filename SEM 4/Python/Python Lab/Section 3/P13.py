def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get valid input for number of terms
while True:
    try:
        terms = int(input("Enter number of Fibonacci terms: "))
        if terms <= 0:
            print("Please enter a positive integer greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Print the Fibonacci sequence
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")
