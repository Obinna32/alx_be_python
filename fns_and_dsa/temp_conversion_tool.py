FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    temp_input = input("Enter the temperature to convert: ")

    if not is_float(temp_input):
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temp_value = float(temp_input)

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result}°F")

    elif unit == "F":
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {result}°C")

    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
