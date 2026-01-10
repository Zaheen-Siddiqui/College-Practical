def handle_exceptions():
    try:
        # Simulate a NameError
        print("Attempting to use an undefined variable:")
        print(undefined_variable)
    
    except NameError as e:
        print(f"NameError occurred: {e}")

    try:
        # Simulate an IndexError
        print("\nAttempting to access an out-of-bounds index:")
        my_list = [1, 2, 3]
        print(my_list[5])
    
    except IndexError as e:
        print(f"IndexError occurred: {e}")

    try:
        # Simulate a ZeroDivisionError
        print("\nAttempting to divide by zero:")
        result = 10 / 0
    
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError occurred: {e}")

# Call the function
handle_exceptions()
