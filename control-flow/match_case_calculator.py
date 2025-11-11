num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /):.")

if operation == "+":
    result = num1+num2
elif operation == "-":
    result = num1-num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1/num2

print(f"The result is {result}.")