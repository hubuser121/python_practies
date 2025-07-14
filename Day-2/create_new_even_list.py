numbers=[12, 5, 8, 13, 90, 33, 66, 1]
Even_list=[]
Odd_list=[]
for num in numbers:
    if num % 2 == 0:
        Even_list.append(num)
    else:
        Odd_list.append(num)

print(f"Even list is :{Even_list}")
print(f"Odd list is :{Odd_list}")