def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b if b != 0 else 'Not allowed'}")

calculator()

#above is the basic math calculation like addition,subtraction, multiplication and division
#i.e ,-,*,/


