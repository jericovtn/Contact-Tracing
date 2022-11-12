# Name: Jerico James F. Viteño
# Laboratory Exercise 2: Contact Tracing
# November 12, 2022

# Dictionary
contacts = {}

def value():
    print("\nAdded Item:\n")
    print("Name:", name)
    print("Address:", address)
    print("Age:", age)
    print("Phone Number:", phone)

# Display Menu
print("\n——====== Menu ======——")
print("  1. Add an item")
print("  2. Search")
print("  3. Exit")
print("——==================——")

# User's Input
option = int(input("\nWhat do you want to do? "))

# Selected Options
# Option 1
if option == 1:
    name = input("Enter your full name: ")
    address = input("Enter your Address: ")
    age = input("Enter your age: ")
    phone = input("Enter your phone number: ")

    # variables ofr dictionaries
    contacts[name] = value()


    print("Saved!")

 

# Option 2
# Option 3




