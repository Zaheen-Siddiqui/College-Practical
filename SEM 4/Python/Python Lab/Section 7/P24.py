def extract_errors(log_file, error_file):
    count = 0
    try:
        with open(log_file, 'r') as f1, open(error_file, 'w') as f2:
            lines = f1.readlines()
            for i, line in enumerate(lines, start=1):
                if 'error' in line.lower():
                    f2.write(f"Line {i}: {line}")
                    count += 1

        print(f"\nTotal 'error' occurrences: {count}")
        print(f"Errors saved into: {error_file}")

    except FileNotFoundError:
        print(f"Error: The file '{log_file}' was not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
log_filename = "server.txt"
error_filename = "error.txt"

extract_errors(log_filename, error_filename)
