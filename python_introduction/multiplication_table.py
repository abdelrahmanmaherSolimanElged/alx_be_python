def main():
  """Prompts user for a number and prints its multiplication table."""

  # Get user input for the number
  number = int(input("Enter a number to see its multiplication table: "))

  # Print the multiplication table header
  print("Multiplication Table for:", number)

  # Use for loop to generate and print the table
  for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

if __name__ == "__main__":
  main()