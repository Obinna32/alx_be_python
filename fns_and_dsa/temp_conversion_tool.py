fahrenheit_to_celsius_factor = 5/9
celsius_to_fahrenheit_factor = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * fahrenheit_to_celsius_factor

def convert_to_fahrenheit(celsius):
    return (celsius_to_fahrenheit_factor * celsius) + 32

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

    # Ask for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Perform conversion based on input
    if unit == "C":
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result}°F")

    elif unit == "F":
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {result}°C")

    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
