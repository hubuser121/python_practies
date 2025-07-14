inventory = [
    {"name": "Laptop", "price": 60000, "stock": 5},
    {"name": "Mouse", "price": 500, "stock": 20},
    {"name": "Keyboard", "price": 800, "stock": 15},
    {"name": "Monitor", "price": 10000, "stock": 0}
]

Total_value=0


for product in inventory:
    name=product["name"]
    price=product["price"]
    stock=product["stock"]  
    item_total=price*stock
    Total_value+=item_total

    status="OUT OF STOCK "if stock ==0 else " "
    print(f"{name} Total :{item_total}  {status} ")

    
print("Total inventory price :", Total_value)