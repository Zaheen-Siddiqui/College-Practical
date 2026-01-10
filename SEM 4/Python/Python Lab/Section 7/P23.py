def write_file(filename):
    try:
        content = input("Enter content to write into the file:\n")
        with open(filename, 'w') as f:
            f.write(content)
        print("Content written successfully!")
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def read_method1(filename):
    print("\n--- Method 1: read() ---")
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def read_method2(filename):
    print("\n--- Method 2: readline() ---")
    try:
        with open(filename, 'r') as f:
            line = f.readline()
            while line:
                print(line.strip())
                line = f.readline()
    except FileNotFoundError:
        print("File not found.")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def read_method3(filename):
    print("\n--- Method 3: readlines() ---")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run all functions
file_name = "sample.txt"
write_file(file_name)
read_method1(file_name)
read_method2(file_name)
read_method3(file_name)
