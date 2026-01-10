# Function to print number pattern
def number_pattern():
    while True:
        try:
            # Get the number of rows from user
            n = int(input("Enter number of rows for number pattern: "))

            # Raise an exception if the number is negative
            if n < 0:
                raise ValueError("Number of rows cannot be negative.")
            
            print("\nNumber Pattern:")
            # Print number pattern
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print(j, end=" ")
                print()  # Move to the next line for the next row
            break  # Exit loop after successful input
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

# Function to print star pattern
def star_pattern():
    while True:
        try:
            # Get the number of rows from user
            n = int(input("Enter number of rows for star pattern: "))

            # Raise an exception if the number is negative
            if n < 0:
                raise ValueError("Number of rows cannot be negative.")
            
            print("\nStar Pattern:")
            # Print star pattern
            for i in range(1, n + 1):
                print('*' * i)  # Print stars, increasing count with each row
            break  # Exit loop after successful input
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

# Run both pattern functions
number_pattern()
star_pattern()
