try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    o=input("Enter operation: ")
    match o:
        case "+":
            print("Result is: ",a+b)
        case "-":
            print("Result is : ",a-b)
        case "*":
            print("Result is: ",a*b)
        case "/":
            print("Result is : ",a/b)
        case _:
            print("Enter a correct operation")

except Exception as e:
    print("Enter a valid value of a and b")