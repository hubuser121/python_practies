def check_even_odd(num):
    if num%2==0:
        return "Even"
    else:
        return "odd"
    
num=int(input("enter a number : "))
result=check_even_odd(num)
print("the number is ",result)