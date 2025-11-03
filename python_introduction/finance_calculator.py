x = eval(input("Enter your monthly income: "))
y = eval(input("Enter your total monthly expenses: "))

monthly_savings = x - y

rate = 0.05

projected_savings = monthly_savings * 12 + monthly_savings *12*rate

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")