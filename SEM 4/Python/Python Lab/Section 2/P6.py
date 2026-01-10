class ValueNotFoundError(Exception):
    """Custom exception raised when the value is not found in the list."""
    pass

class InvalidInputError(Exception):
    """Custom exception raised when there is invalid input (non-numeric) for list or value."""
    pass

def find_value(my_list, value):
    if not isinstance(my_list, list):
        raise TypeError("The first argument must be a list.")
    if not my_list:
        raise ValueError("The list is empty.")

    count = my_list.count(value)
    if count == 0:
        raise ValueNotFoundError(f"Value '{value}' not found in the list.")

    indexes = [i for i, x in enumerate(my_list) if x == value]
    print(f"Value '{value}' occurs {count} times at positions: {indexes}")

def get_valid_list_input():
    while True:
        try:
            # Input for the list
            my_list_input = input("Enter a list of numbers separated by spaces: ").split()

            # Check if all inputs are numeric
            if not all(x.isdigit() for x in my_list_input):
                raise InvalidInputError("All elements in the list must be numbers.")

            return [int(x) for x in my_list_input]  # Convert each input to an integer
        except InvalidInputError as e:
            print(f"Error: {e}")
            print("Please try again.")

def get_valid_value_input():
    while True:
        try:
            # Input for the value to find
            value_to_find = input("Enter the value you want to find: ")

            # Check if the value is numeric
            if not value_to_find.isdigit():
                raise InvalidInputError("The value to find must be a number.")
            
            return int(value_to_find)
        except InvalidInputError as e:
            print(f"Error: {e}")
            print("Please try again.")

# Main program execution
while True:
    try:
        # Get valid list input
        my_list = get_valid_list_input()

        # Get valid value input
        value_to_find = get_valid_value_input()

        # Calling the function
        find_value(my_list, value_to_find)
        break  # Exit the loop if everything works correctly

    except (TypeError, ValueError, ValueNotFoundError, InvalidInputError) as e:
        print(f"Error: {e}")
        print("Please try again.")
