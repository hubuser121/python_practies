contacts=[]


def add_contact(name, phone, email):
    contact={"name":name,"phone":phone,"email":email}
    contacts.append(contact)
    print(f"contact for {name} added \n")


def view_contact():
    if not contacts:
        print("contacts not found")
    else:
        print("your contacts")
        for c in contacts:
            print(f"name:{c['name']},\nphone:{c['phone']},\nemail:{c['email']}\n")


def search_contacts(name):
    found=False
    for c in contacts:
        if c["name"].lower()==name.lower():
            print("contact found")
            found= True
            break
        if not found:
            print("contact not found ")

#  menu book

while True:
    print("\nContacts Menu Book\n ")
    print("1.Add Contact")
    print("2.View contacts")
    print("3.Search Contacts")
    print("4.Exit")

    choice=(input("Enter your choice (1-4) \n"))

    if choice == "1":
        name=input("Enter name \n")
        phone=int(input("Enter phone number\n"))
        email=input("Enter  email\n")
        add_contact(name, phone, email)
    elif choice== "2":
        view_contact()
    elif choice== "3":
        name=input("Enter your name\n")
        search_contacts(name)
    elif choice== "4":
        print("Exiting contact Book")
        break
    else:
        print("Invalid operation")