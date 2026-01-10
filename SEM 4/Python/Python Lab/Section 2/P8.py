class InvalidInputError(Exception):
    """Custom exception raised when input is not a list."""
    pass

class ListElementTypeError(Exception):
    """Custom exception raised when list elements are of invalid type (not int or float)."""
    pass

class StringInputError(Exception):
    """Custom exception raised when the user inputs a string instead of a number in the list."""
    pass

def merge_lists(list1, list2):
    # Ensure that both inputs are lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise InvalidInputError("Both inputs must be lists.")
    
    # Ensure that list elements are of valid type (e.g., integers or floats)
    if not all(isinstance(item, (int, float)) for item in list1):
        raise ListElementTypeError("All elements in list1 must be numbers (int or float).")
    if not all(isinstance(item, (int, float)) for item in list2):
        raise ListElementTypeError("All elements in list2 must be numbers (int or float).")

    # Merge the lists
    list1.extend(list2)
    print("Updated List1:", list1)

def get_valid_list_input(prompt):
    while True:
        try:
            list_input = input(prompt).split()
            
            # Check for invalid string inputs
            for item in list_input:
                if not item.replace('.', '', 1).isdigit():  # This checks if the input is a valid number (allowing decimal point)
                    raise StringInputError(f"Invalid input: '{item}' is not a number.")
            
            # Convert the valid input to a list of numbers
            return [float(x) if '.' in x else int(x) for x in list_input]
        
        except StringInputError as e:
            print(f"Error: {e}")
            print("Please enter the list again.")

# Main program execution
while True:
    try:
        # Get user input for the first list
        list1 = get_valid_list_input("Enter the first list of numbers separated by spaces: ")

        # Get user input for the second list
        list2 = get_valid_list_input("Enter the second list of numbers separated by spaces: ")

        # Calling the merge function
        merge_lists(list1, list2)
        break  # Exit the loop if everything is successful

    except (InvalidInputError, ListElementTypeError, ValueError, StringInputError) as e:
        print(f"Error: {e}")
        print("Please try again.")
