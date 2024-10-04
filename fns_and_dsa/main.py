# main.py

from arithmetic_operations import perform_operation


def main():
	"""
	Main function to interact with the user and perform arithmetic operations.
	"""
	print("Arithmetic Operations")
	

	# Taking user input for two numbers
	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))
	
	# Taking user input for the desired operation
	operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
	
	# Perform the operation using the imported function
	result = perform_operation(num1, num2, operation)
	
	# Display the result
	print(f"Result: {result}")


if __name__ == "__main__":
	main()
