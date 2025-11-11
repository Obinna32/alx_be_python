num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

operator = input("Choose the operator (+,-,*,/): ")

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        result = num1/num2

print(f"The result is {result}.")