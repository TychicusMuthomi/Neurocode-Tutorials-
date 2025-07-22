#create two empty lists for the names and numbers:
name = []
phone_numbers = []
number_of_contact = int(input("Enter the number of contacts you would like to add: "))
count = number_of_contact
for i in range(number_of_contact):
    contacts = input(f"Enter contact name {i+1}: ").capitalize()
    number = int(input(f"Enter contact number {i+1}: "))
    count-=1
    name.append(contacts)
    phone_numbers.append(number)
    response = input("Would you like to continue to add contacts or view your contacts or delete your contacts or search for a contact: ")
    if response == "would you like to continue to add contacts":
        continue
    elif response == "view your contacts":
        print(name + phone_numbers)
    elif response == "delete your contacts":
        name_contact = input("Which contact would you like to delete: ")
        how_many = int(input("Which contact would you like to delete according to index: "))
        name.remove(name_contact)
        del phone_numbers[how_many]
        second_response = input("Would you like to view your contacts (y,n): ").lower()
        if second_response =="y":
            print(name + phone_numbers)
        else:
            continue
    elif response == "search for a contact":
        third_response = int(input("Enter the contact's positional index: "))
        print(name[third_response])




