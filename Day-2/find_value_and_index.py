numbers=[23,45,67,89,90,99,2200]
search=int(input("enter a value to be searched "))
if search in numbers:
    index=numbers.index(search)
    print(f"{search} Value found and at the location {index}")
else:
    print(f"{search} Value  not found ")