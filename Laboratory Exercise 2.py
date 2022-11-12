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
    print("Name:", name)
    print("Address:", address)
    print("Age:", age)
    print("Phone Number:", phone)
    
while True:
    # Display Menu
    menu()

    # User's Input
    option = int(input("\nWhat do you want to do? "))

    # Selected Options
    # Option 1
    if option == 1:
        name = input("Enter your full name: ")
        address = input("Enter your Address: ")
        age = int(input("Enter your age: "))
        phone = int(input("Enter your phone number: "))
        
        print("\nAdded Item:\n")
        contacts[name] = {"Name": name, "Address": address, "Age": age, "Phone Number": phone}
        value()

        print("Saved!")

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
        exit = input("Do you wish to close the program? (y/n): ")
        if exit == "n" or "N" or "No" or "NO":
            continue
        else:
            break
    
    # Invalid Option
    else:
        print("Sorry, Invalid Option!")





