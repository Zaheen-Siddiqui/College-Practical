class Student:
    def __init__(self, name="Unknown", roll_no=0):
        try:
            # If no name or roll_no is provided, prompt the user for input
            if name == "Unknown":
                name = input("Enter student's name: ")
            if roll_no == 0:
                roll_no = int(input("Enter student's roll number: "))

            # Validate name (it should be a non-empty string)
            if not isinstance(name, str) or not name:
                raise ValueError("Name must be a non-empty string.")

            # Validate roll_no (it should be a positive integer)
            if not isinstance(roll_no, int) or roll_no <= 0:
                raise ValueError("Roll number must be a positive integer.")

            self.name = name
            self.roll_no = roll_no

        except ValueError as ve:
            print(f"Error in initialization: {ve}")
            # Assign default values in case of error
            self.name = "Unknown"
            self.roll_no = 0
        except Exception as e:
            print(f"Unexpected error: {e}")
            # Assign default values in case of unexpected error
            self.name = "Unknown"
            self.roll_no = 0

    def display(self):
        try:
            # Ensure attributes are properly set before displaying
            if not isinstance(self.name, str) or not isinstance(self.roll_no, int):
                raise TypeError("Invalid data type for name or roll number.")
            print(f"Name: {self.name}, Roll No: {self.roll_no}")
        except TypeError as te:
            print(f"Error during display: {te}")
        except Exception as e:
            print(f"Unexpected error during display: {e}")

# Default constructor - prompt user for input
student1 = Student()
student1.display()

# Parameterized constructor - prompt user for input
student2 = Student("Alice", 23)
student2.display()

# Testing invalid data (this part can also prompt user input)
student3 = Student("", -5)  # Invalid name and roll_no
student3.display()
