def login_system():
    users = {
        "user1": "pass123",
        "admin": "adminpass"
    }
    attempts = 0

    while attempts < 3:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")

            # Check for empty inputs
            if not username or not password:
                raise ValueError("Username or password cannot be empty.")
            
            if username not in users:
                raise KeyError("User doesn't exist.")
            elif users[username] != password:
                raise PermissionError("Incorrect password.")
            else:
                print("Login Successful!")
                break

        except KeyError as ke:
            print(ke)
        except PermissionError as pe:
            print(pe)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"General Error: {e}")

        attempts += 1

    if attempts == 3:
        print("Too many attempts! Try again later.")


login_system()
