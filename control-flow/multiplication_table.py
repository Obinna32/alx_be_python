number = eval(input("Enter a number to see its multiplication table: "))

for i in range(10):
    print(f"{number} * {i+1} =", number*(i+1))
    i+=1