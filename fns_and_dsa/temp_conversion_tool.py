# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_CELSIUS = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the global conversion factor
    celsius = (fahrenheit - FREEZING_POINT_CELSIUS) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the global conversion factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_CELSIUS
    return fahrenheit

# Main program to interact with the user
def main():
    try:
        # Prompt the user for temperature and unit
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the appropriate conversion based on user input
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
