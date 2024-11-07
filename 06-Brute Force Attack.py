#Define the correct password
correct_password = 12345
allowed_attempts = 5 #Number of attempts allowed
attempts = 0 #start the loop
while attempts < allowed_attempts:
#Asking the user to enter the password
    entered_password = int(input("Please enter the password: "))
    if entered_password == correct_password: #Checking if the entry is valid
        print("Access has been granted!")
        break #Breaking the loop if the password is valid
    else:
        attempts += 1
        remaining_attempts = allowed_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("You have reached the maximum number of attempts. The authorities have been alerted")
            break #Breaking the loop after the maximum number of attempts is reached