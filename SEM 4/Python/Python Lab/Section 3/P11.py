def calculate_fine(days_late, condition):
    fine = 0
    if days_late > 0:
        fine += days_late * 2  # ₹2 per day late
    if condition.lower() != 'good':
        fine += 100  # ₹100 penalty for bad condition
    return fine

# Get valid number of days late
while True:
    try:
        days = int(input("Enter number of days late: "))
        if days < 0:
            print("Days late cannot be negative. Please enter again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for days late.")

# Get valid book condition
while True:
    cond = input("Enter book condition (Good/Bad): ").strip().lower()
    if cond in ['good', 'bad']:
        break
    else:
        print("Invalid condition. Please enter 'Good' or 'Bad'.")

# Calculate and display the fine
total_fine = calculate_fine(days, cond)
print(f"Total fine: ₹{total_fine}")
