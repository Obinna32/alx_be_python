def safe_divide(numerator, denominator):
    try:
        x = float(numerator) / float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    else:
        return f"The result of the division is {x}"
