Billing_app=[]

def get_item():
    item_name=input("Enter your item name \n")
    price=float(input("Enter the price\n"))
    Quantity=int(input("Enter the Quantity \n"))


    item_dict={
        "name":item_name,
        "price":price,
        "quantity":Quantity
    }
    return item_dict

num_items=int(input("How many items you want to add\n"))

for _ in range(num_items):
    item=get_item()
    Billing_app.append(item)

print("\n---------BILL-----------")
total_bill=0
for p in Billing_app:
    name=p["name"]
    price=p["price"]
    quantity=p["quantity"]
    item_total=price*quantity
    total_bill+=item_total
    print(f"{name}                {quantity} x ${price} = {item_total}")
print("-------------------------")
print("Total_bill", total_bill)