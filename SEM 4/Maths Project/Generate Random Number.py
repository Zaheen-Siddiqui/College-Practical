import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function to generate 100 one-digit numbers randomly
def generate_and_count(n):
    count_2 = 0  # Count for 2
    count_4 = 0  # Count for 4
    count_6 = 0  # Count for 6
    all_counts = []  # List to store counts of 2, 4, 6 for each trial
    trial_data = []   # List to store data for each trial

    # Perform n trials
    for trial in range(1, n + 1):
        trial_numbers = []  # Store numbers for the current trial
        trial_count = 0    # Count of 2, 4, and 6 for this trial
        for _ in range(100):
            num = random.randint(0, 9)  # Generate a random number between 0 and 9
            trial_numbers.append(num)
            
            if num == 2:
                count_2 += 1
                trial_count += 1
            elif num == 4:
                count_4 += 1
                trial_count += 1
            elif num == 6:
                count_6 += 1
                trial_count += 1
        
        # Add trial count and the generated numbers to the data
        trial_data.append({'Trial': trial, 'Numbers': trial_numbers, 'Count_2_4_6': trial_count})
        all_counts.append(trial_count)
        
    # Return the counts and all trial data
    total_count = count_2 + count_4 + count_6
    return count_2, count_4, count_6, total_count, all_counts, trial_data

# Function to generate 100 one-digit numbers and count frequency of all digits (0-9)
def generate_and_count_all_digits():
    # Initialize a dictionary to store the count of each digit (0-9)
    digit_counts = {str(i): 0 for i in range(10)}

    # Generate 100 random one-digit numbers
    for _ in range(100):
        num = random.randint(0, 9)  # Generate a random number between 0 and 9
        digit_counts[str(num)] += 1  # Increment the count for the generated number

    return digit_counts


# Generate and plot the frequency graph of all digits (0-9)
digit_counts = generate_and_count_all_digits()

# Plot the frequency graph of all digits (0-9)
plt.figure(figsize=(8, 6))
plt.bar(digit_counts.keys(), digit_counts.values(), color='skyblue', edgecolor='black')

# Adding labels and title
plt.title("Frequency of Digits (0-9) in 100 Random Numbers")
plt.xlabel("Digits")
plt.ylabel("Frequency")
plt.xticks(rotation=0)

# Show the plot
plt.tight_layout()
plt.show()

# Get user input for how many trials to perform
n = int(input("Enter the number of trials: "))  # Define how many trials you want to run

# Get the counts of 2, 4, and 6 and the list of counts for each trial
count_2, count_4, count_6, total_count, all_counts, trial_data = generate_and_count(n)

# Output the results for counts of 2, 4, and 6
print(f"\nIn {n} trials of generating 100 one-digit numbers:")
print(f"Count of 2: {count_2}")
print(f"Count of 4: {count_4}")
print(f"Count of 6: {count_6}")
print(f"Total Count of 2, 4 and 6: {total_count}")

# Plot the frequency graph of counts for 2, 4, and 6 across all trials
plt.figure(figsize=(12, 6))

# Plot histogram for the frequency of counts across all trials
plt.hist(all_counts, bins=range(min(all_counts), max(all_counts) + 1), edgecolor='black')
plt.title(f'Frequency of Counts of 2, 4, and 6 Across {n} Trials')
plt.xlabel('Count of 2, 4 and 6 in each trial')
plt.ylabel('Frequency')

# Show the plot
plt.tight_layout()
plt.show()

# Convert trial data to a DataFrame
df_trial_data = pd.DataFrame(trial_data)

# Create a DataFrame for the summary results
df_summary = pd.DataFrame({
    'Count of 2': [count_2],
    'Count of 4': [count_4],
    'Count of 6': [count_6],
    'Total Count of 2, 4 and 6': [total_count]
})


# Save the trial data and summary to an Excel file
output_filename = "275 Sets of Numbers.xlsx"
with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
    df_trial_data.to_excel(writer, sheet_name='Trial Data', index=False)
    df_summary.to_excel(writer, sheet_name='Summary', index=False)

print(f"\nResults have been saved to {output_filename}")
