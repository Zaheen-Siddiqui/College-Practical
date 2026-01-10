def square_list(numbers):
    try:
        return [x**2 for x in numbers]
    except TypeError:
        print("Error: All elements must be numbers.")
        return []

# Get user-defined list input
while True:
    try:
        user_input = input("Enter numbers separated by spaces: ")
        my_numbers = [float(num) for num in user_input.strip().split()]
        break
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")

squared_numbers = square_list(my_numbers)

print("Original List:", my_numbers)
print("Squared List:", squared_numbers)
