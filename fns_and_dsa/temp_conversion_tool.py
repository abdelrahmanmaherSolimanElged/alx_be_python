# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32  # Offset for Fahrenheit to Celsius conversion

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    # Using the global variable for the conversion factor
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    # Using the global variable for the conversion factor
    fahrenheit = (celsius *  CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

def main():
    try:
        # User input for temperature and unit
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            # Convert to Celsius
            celsius_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius_temp}°C")
        elif unit == 'C':
            # Convert to Fahrenheit
            fahrenheit_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit_temp}°F")
        else:
            raise ValueError("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Invalid temperature. Please enter a numeric value. Error: {e}")

if __name__ == "__main__":
    main()
