# Main Program

import mymodule

def menu():
    while True:
        print("\nMenu:")
        print("1. Find Factorial")
        print("2. Check Prime Number")
        print("3. Power Calculation")
        print("4. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                try:
                    num = int(input("Enter number: "))
                    print("Factorial:", mymodule.factorial(num))
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 2:
                try:
                    num = int(input("Enter number: "))
                    if mymodule.primeNumber(num):
                        print(f"{num} is a Prime Number.")
                    else:
                        print(f"{num} is NOT a Prime Number.")
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 3:
                try:
                    base = int(input("Enter base: "))
                    exp = int(input("Enter exponent: "))
                    print("Result:", mymodule.powNumber(base, exp))
                except ValueError as e:
                    print(f"Error: {e}")

            elif choice == 4:
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please enter a valid number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

menu()
