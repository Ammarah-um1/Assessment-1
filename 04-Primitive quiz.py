# Print a welcome message to start the quiz
print("Welcome to the quiz! Let's start.")

import re # Importing regular expression (re) library to use search and IGNORECASE functions

# Dictionary of European countries and their capitals
countries = {
    "France": "paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Finland": "Helsinki",
    "Norway": "Oslo",
    "Netherlands": "Amsterdan"
}
for  country, capital in countries.items(): # Loop through the questions and check answers
    answer = input(f"What is the capital of {country}?: ") # Ask user the question

# Use re.match() with re.IGNORECASE to compare the user's answer with the correct answer
    if re.fullmatch(capital, answer, re.IGNORECASE):
        print("Correct answer! ")
    else:
# If the answer is wrong, display the correct answer
        print(f"Wrong answer! The correct answer is {capital}. ")
