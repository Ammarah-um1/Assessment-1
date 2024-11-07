# List of names 
names_list = ["Jake", "Zac", "Ian", "Sam", "Dave"]

# Taking input from the user for the name
search = input("Enter the name you want to search for: ")

# Checking if the user input is in the list
if search in names_list:
    print(f"{search} is in the list") # If the user input is in the list, display the message 
else:
    print("Entered name not found on the list") # Else show the given name is not in the list
    