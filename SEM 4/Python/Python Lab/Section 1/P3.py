# Function to reverse a number
def reverse_number():
    while True:
        try:
            # Prompt user to input a number
            num = int(input("Enter a number: "))

            # Check if the number is negative
            is_negative = num < 0

            # Work with the absolute value of the number for reversing
            num = abs(num)
            reversed_num = 0  # Variable to hold the reversed number

            # Reverse the digits of the number
            while num > 0:
                digit = num % 10  # Get the last digit of the number
                reversed_num = reversed_num * 10 + digit  # Build the reversed number
                num = num // 10  # Remove the last digit from the number

            # If the original number was negative, make the reversed number negative
            if is_negative:
                reversed_num = -reversed_num

            # Output the reversed number
            print(f"Reversed Number: {reversed_num}")
            break  # Exit the loop once a valid input is processed
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter an integer.")

# Run the reverse_number function
reverse_number()
