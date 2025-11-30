def safe_divide(numerator, denominator):
    try:
        x = float(numerator)/float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result of the division is {x}")