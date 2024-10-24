# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
	celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
	return celsius


# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
	fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
	return fahrenheit


# Main function to handle user input and perform the conversion
def main():
	try:
		temperature = float(input("Enter the temperature to convert: "))
	except ValueError:
		raise ValueError("Invalid temperature. Please enter a numeric value.")
	
	unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
	
	if unit == 'C':
		converted = convert_to_fahrenheit(temperature)
		print(f"{temperature}°C is {converted}°F")
	elif unit == 'F':
		converted = convert_to_celsius(temperature)
		print(f"{temperature}°F is {converted}°C")
	else:
		print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# Run the program
if __name__ == "__main__":
	main()
