def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a/b
def mod(a,b):
    return a%b

num_1=int(input("enter the first number\n"))

num_2=int(input("enter the second number \n"))

op=input("enter your opertaor +,-,*,/,% \n")

while op in['/','%'] and num_2==0:
    print("second number cannot be zero ")
    num_2=int(input("Reenter the second number "))


if op == "+":
    result=add(num_1,num_2)
elif op=="-":
    result=sub(num_1,num_2)
elif op=="*":
    result=mul(num_1,num_2)
elif op=="/":
    result=divide(num_1,num_2)
elif op=="%":
    result=mod(num_1,num_2)
else:
    result="invalid operator"

print(" the result is :",result)