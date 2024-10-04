# Define global conversion factors
F = 5 / 9
C = 9 / 5


def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature converted to Celsius.
    """
    return (fahrenheit - 32) * F


def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature converted to Fahrenheit.
    """
    return (celsius * C) + 32


def main():
    """Prompts user for temperature, converts it based on unit, and displays the result."""
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            if unit not in ("C", "F"):
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

            if unit == "C":
                converted_temp = convert_to_fahrenheit(temperature)
                unit_label = "Celsius"
            else:
                converted_temp = convert_to_celsius(temperature)
                unit_label = "Fahrenheit"

            print(f"{temperature:.1f}°{unit_label} is {converted_temp:.2f}°F" if unit == "C" else f"{temperature:.1f}°{unit_label} is {converted_temp:.2f}°C")
            break
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()