# Name: Jerico James F. Viteño
# Laboratory Exercise 2: Contact Tracing
# November 12, 2022

# Dictionary
contacts = {}

def menu():
    print("\n——====== Menu ======——")
    print("  1. Add an item")
    print("  2. Search")
    print("  3. Exit")
    print("——==================——")

def value():
    print("Name:\t\t", name)
    print("Address:\t", address)
    print("Age:\t\t", age)
    print("Phone Number:\t", phone)
    
while True:
    # Display Menu
    menu()

    # User's Input
    option = int(input("\nWhat do you want to do? "))

    # Selected Options
    # Option 1
    if option == 1:
        print("\n——====== ADD =======——")
        name = input("Enter your full name: \t")
        address = input("Enter your Address: \t")
        age = int(input("Enter your age: \t"))
        phone = int(input("Enter your number: \t"))
        print("——==================——")
        
        print("\n——=== ADDED ITEM ===——")
        contacts[name] = {"Name": name, "Address": address, "Age": age, "Phone Number": phone}
        value()
        print("——==================——")

        print("\n\tSaved!")

    # Option 2
    elif option == 2:
        search = input("Enter your full name: ")

        if search in contacts.keys():
            print("\nSearched Item:\n")
            for item in contacts[search].items():
                print(item[0], ":", item[1])
        else:
            print("Contatcs Not Found!")

    # Option 3
    elif option == 3:
        exit = input("Do you wish to close \nthe program? (y/n): ")
        if exit == "n" or "N" or "No" or "NO":
            continue
        else:
            break
    
    # Invalid Option
    else:
        print("Sorry, Invalid Option!")





