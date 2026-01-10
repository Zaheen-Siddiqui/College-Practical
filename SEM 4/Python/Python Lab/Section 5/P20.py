class Vehicle:
    def __init__(self, brand):
        try:
            if not isinstance(brand, str) or not brand:
                raise ValueError("Brand must be a non-empty string.")
            self.brand = brand
        except ValueError as e:
            print(f"Error: {e}")
            self.brand = "Unknown"  # Default value

    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):  # Single Level Inheritance
    def __init__(self, brand, model):
        try:
            super().__init__(brand)
            if not isinstance(model, str) or not model:
                raise ValueError("Model must be a non-empty string.")
            self.model = model
        except ValueError as e:
            print(f"Error: {e}")
            self.model = "Unknown"  # Default value

    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Multilevel Inheritance Example:
class Person:
    def __init__(self, name):
        try:
            if not isinstance(name, str) or not name:
                raise ValueError("Name must be a non-empty string.")
            self.name = name
        except ValueError as e:
            print(f"Error: {e}")
            self.name = "Unknown"  # Default value

    def show_name(self):
        print(f"Name: {self.name}")

class Employee(Person):
    def __init__(self, name, emp_id):
        try:
            super().__init__(name)
            if not isinstance(emp_id, int) or emp_id <= 0:
                raise ValueError("Employee ID must be a positive integer.")
            self.emp_id = emp_id
        except ValueError as e:
            print(f"Error: {e}")
            self.emp_id = 0  # Default value

    def show_emp_id(self):
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):  # Multilevel Inheritance
    def __init__(self, name, emp_id, department):
        try:
            super().__init__(name, emp_id)
            if not isinstance(department, str) or not department:
                raise ValueError("Department must be a non-empty string.")
            self.department = department
        except ValueError as e:
            print(f"Error: {e}")
            self.department = "Unknown"  # Default value

    def show_department(self):
        print(f"Department: {self.department}")

# Sample Output:
print("\n--- Single Level Inheritance ---")
car = Car("Toyota", "Innova")
car.show_details()

print("\n--- Multilevel Inheritance ---")
manager = Manager("John", 101, "Sales")
manager.show_name()
manager.show_emp_id()
manager.show_department()

# Testing Invalid Input:
print("\n--- Testing Invalid Input ---")
invalid_car = Car("", 123)  # Invalid model
invalid_car.show_details()

invalid_manager = Manager("", -5, "")  # Invalid name, emp_id, and department
invalid_manager.show_name()
invalid_manager.show_emp_id()
invalid_manager.show_department()
