def add(x, y):
    return(x + y)

def sub(x, y):
    return(x - y)

def div(x, y):
    return(x / y)

def multiply(x, y):
    return(x * y)

print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", div(num1, num2))

        elif choice == '4':
            print(num1, "*", num2, "=", multiply(num1, num2))
        break
    else:
        print("Invalid Number")
        

    

