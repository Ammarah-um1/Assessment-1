#Asking the user to input their name
name = input("What is your name?: ")

#Asking the user to input their hometown
hometown = input("What is your hometown?: ")

#Using while loop to ensure valid age input
while True: 
    try:
        age = int(input("Enter your age: ")) #Asking the user to input their age 
        break #If the input is valid (numeric), exit the loop
    except ValueError: #Using except block to manage the error
        print("Invalid input. Please enter a numeric value.")
        
#Create a dictionary to store user info
user_info = {"Name": name, "Hometown": hometown, "Age": age} 

for user_info2 in user_info.values():
    print(user_info2)