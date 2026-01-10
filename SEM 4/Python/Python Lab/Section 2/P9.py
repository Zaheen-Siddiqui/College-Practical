def get_valid_range_input(prompt):
    while True:
        try:
            # Prompt the user for the range of the list
            user_input = input(prompt)
            start, end = map(int, user_input.split())  # Expect two numbers, separated by space
            if start >= end:
                raise ValueError("The start of the range must be less than the end.")
            return start, end
        except ValueError as e:
            print(f"Error: {e}. Please enter two valid numbers, with the start less than the end.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")

def generate_squares(start, end):
    try:
        squares = [x**2 for x in range(start, end + 1)]  # Range is inclusive of 'end'
        print("Squares:", squares)
    except Exception as e:
        print(f"Error generating squares: {e}")

def generate_evens(start, end):
    try:
        evens = [x for x in range(start, end + 1) if x % 2 == 0]
        print("Even numbers:", evens)
    except Exception as e:
        print(f"Error generating even numbers: {e}")

# Main program
while True:
    try:
        # Get valid range input for squares
        start_square, end_square = get_valid_range_input("Enter the range (start end) for squares: ")

        # Generate and print the squares list
        generate_squares(start_square, end_square)

        # Get valid range input for even numbers
        start_even, end_even = get_valid_range_input("Enter the range (start end) for even numbers: ")

        # Generate and print the even numbers list
        generate_evens(start_even, end_even)
        
        break  # Exit the loop after successful execution
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
