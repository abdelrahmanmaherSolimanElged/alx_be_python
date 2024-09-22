# pattern_drawing.py

# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Use a while loop to control the rows
while row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")  # Print asterisks without a new line
    print()  # Move to the next line after each row
    row += 1