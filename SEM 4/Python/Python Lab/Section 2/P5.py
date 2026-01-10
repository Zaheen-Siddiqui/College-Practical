def count_data_types(my_list):
    # Initialize counters for each data type
    int_count = float_count = str_count = other_count = 0

    for elem in my_list:
        if type(elem) == int:
            int_count += 1
        elif type(elem) == float:
            float_count += 1
        elif type(elem) == str:
            str_count += 1
        else:
            other_count += 1

    print(f"Integers: {int_count}, Floats: {float_count}, Strings: {str_count}, Others: {other_count}")

def get_user_input():
    while True:
        try:
            user_input = input("Enter a list of items (separate by commas, e.g., 1, 'Hello', 3.5): ")
            # Split the input by commas
            items = user_input.split(",")
            parsed_items = []

            for item in items:
                item = item.strip()  # Remove any leading/trailing whitespace
                if item.isdigit():  # Check if it's an integer
                    parsed_items.append(int(item))
                elif item.replace(".", "", 1).isdigit() and item.count('.') < 2:  # Check if it's a float
                    parsed_items.append(float(item))
                elif item.startswith("'") and item.endswith("'"):  # Handle string literals
                    parsed_items.append(item[1:-1])  # Remove the single quotes
                else:
                    parsed_items.append(item)  # Anything else is treated as a string

            count_data_types(parsed_items)  # Call function to count data types in the list
            break  # Break loop when everything is valid

        except Exception as e:
            print(f"Invalid input: {e}. Please enter a valid list.")

get_user_input()
