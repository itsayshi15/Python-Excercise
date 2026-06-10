x = float(input("Enter the first number: "))

y = float(input("Enter the second number: "))

z = (input("Enter the operator (+, -, *, /): "))



if z == "+":
    print("Result =", x+y)

elif z == "-":
    print("Result =", x-y)

elif z == "*":
    print("Result =", x*y)

elif z == "/":
    if y != 0:
        print("Result =", x/y)
    else:
        print("Division by zero is not allowed.")

else:
    print("Invalid operator")