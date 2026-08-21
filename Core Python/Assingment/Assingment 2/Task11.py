### Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# Take Input from user
amount = int(input("Enter the amount: "))

# Define the denominations of notes
denominations = [100, 50, 20, 10, 5, 2, 1]

# Calculate the minimum number of notes needed
total_notes = 0
for denomination in denominations:
    notes_needed = amount // denomination
    total_notes += notes_needed
    amount -= notes_needed * denomination

print(f"Minimum number of notes needed: {total_notes}")