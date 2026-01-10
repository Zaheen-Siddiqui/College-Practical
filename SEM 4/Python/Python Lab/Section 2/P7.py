class InvalidChoiceError(Exception):
    """Custom exception for an invalid choice when sorting."""
    pass

class InvalidInputError(Exception):
    """Custom exception for invalid input types."""
    pass

def sort_list(my_list):
    # Ensure the list contains only numbers (or valid comparable types)
    if not all(isinstance(item, (int, float)) for item in my_list):
        raise InvalidInputError("All elements in the list must be numbers.")
    
    while True:
        print("Press 1 for Ascending Order")
        print("Press 2 for Descending Order")
        
        try:
            choice = int(input("Enter choice: "))
            
            if choice == 1:
                my_list.sort()
                print("Ascending Order:", my_list)
                break  # Exit the loop once sorted
            elif choice == 2:
                my_list.sort(reverse=True)
                print("Descending Order:", my_list)
                break  # Exit the loop once sorted
            else:
                raise InvalidChoiceError("Invalid choice! Please press 1 or 2.")
        
        except ValueError:
            print("Error: Please enter a valid number for the choice (1 or 2).")
        except InvalidChoiceError as e:
            print(f"Error: {e}")

def get_valid_list_input():
    while True:
        try:
            user_input = input("Enter a list of numbers separated by spaces: ").split()
            my_list = [float(x) if '.' in x else int(x) for x in user_input]  # Convert input to numbers (int or float)
            return my_list
        except ValueError:
            print("Error: Please enter valid numbers separated by spaces.")

# Main program execution
while True:
    try:
        # Get a valid list of numbers
        my_list = get_valid_list_input()
        
        # Call the sorting function
        sort_list(my_list)
        break  # Exit the loop if everything works correctly

    except InvalidInputError as e:
        print(f"Error: {e}")
        print("Please try again.")
