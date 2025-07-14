numbers=[12,45,98]
minimum=numbers[0]
for num in numbers:
    if num < minimum:
        minimum=num
print("minimum is ", minimum)