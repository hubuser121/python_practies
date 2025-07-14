number=(input("Enter the number : "))
even_count=0
odd_count=0
for digit in number:
    if int(digit) % 2==0:
        even_count+= 1
    else:
        odd_count+=1
print(f" there are {even_count} even digits in {number} ")
print(f" there are {odd_count} odd digits in {number} ")