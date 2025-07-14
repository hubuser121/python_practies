num1=int(input("enter the first number : "))
operator=input("enter a operator (+,-,*,/,%) : ")
num2=int(input("enter the second number : "))
if operator=='+':
    sum=num1+num2
    print(sum)
elif operator=='-':
    subtraction=num1-num2
    print(subtraction)
elif operator=='*':
    multiplication=num1*num2
    print(multiplication)
elif operator=='/':
    if num2==0:
        print("cannot be divisible by Zero ")
    else:
        division=num1 / num2
        print(division)
elif operator=='%':
    if num2==0:
        print("cannot do modulus  by Zero ")
    else:
        reminder=num1 % num2
        print(reminder)
else:
    print("choose appropriate operator")