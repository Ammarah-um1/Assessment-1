# Dictionary to store the number of days for each month
months_dict = {1:31, 2:28, 3:31 , 4:30, 5:31, 6:30, 7:31,
        8:31, 9:30, 10:31, 11:30, 12:31}

selected_month = int(input("Enter the month number (1-12): ")) # Prpmpt user to enter a month number

if selected_month < 1 or selected_month > 12: # Check if the entered month is valid (between 1-12)
    print("incorrect!")

elif selected_month == 2: # If the entered month is (month 2), ask if it's a leap year
    leap_year_input = 2
    leap_year_input = input("It's a leap year? Answer [yes/no]: ")  # Take input from user

    if leap_year_input == "yes": # If its a leap year, update Februray to 29 days
        months_dict[2] = 29 # modifying the dictionary, if the input is a leap year
        
# Initializing the user input and the dictionary in a single variable 
        days_in_selected_month = months_dict[selected_month] 

else:
    leap_year_input = "no" # If it's not a leap year, February remains with 28 days
days_in_selected_month = months_dict[selected_month]

# Output the number of days in the selected month
print(f"The {selected_month} has {days_in_selected_month} days.") 