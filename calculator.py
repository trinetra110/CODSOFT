a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
operator=input("Enter the operator: ")
if operator=="+":
    print("{a} + {b} = {c}".format(a=a,b=b,c=a+b))
elif operator=="-":
    print("{a} - {b} = {c}".format(a=a,b=b,c=a-b))
elif operator=="*":
    print("{a} * {b} = {c}".format(a=a,b=b,c=a*b))
elif operator=="/":
    print("{a} / {b} = {c}".format(a=a,b=b,c=a/b))
else:
    print("Invalid operator")
