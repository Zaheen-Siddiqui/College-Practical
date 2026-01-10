def calculate_grade():
    # List of subjects
    subjects = ["Python", "Computer Network", "Automata Theory", "Operating System", "Computer Organization and Architecture"]
    marks = []  # List to store marks for each subject

    # Loop through each subject to get valid marks input from user
    for subject in subjects:
        while True:
            try:
                # Prompt user for marks and convert to float
                m = float(input(f"Enter marks for {subject} (Out of 100): "))

                # Check for valid mark range
                if m < 0:
                    raise ValueError("Marks cannot be negative.")
                elif m > 100:
                    raise ValueError("Marks cannot exceed 100.")
                
                # Add valid mark to the list
                marks.append(m)
                break  # Exit the loop if input is valid
            except ValueError as e:
                # Show error message and prompt again
                print(f"Invalid input: {e}. Please enter a valid number between 0 and 100.")
    
    # Calculate average marks
    average = sum(marks) / len(subjects)

    # Determine grade based on average
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Display the average and grade
    print(f"\nAverage Marks = {average}")
    print(f"Grade = {grade}")

# Call the function to execute grade calculation
calculate_grade()
