# Defining a function to determine if a number is even or odd
def even_or_odd(number):
    if number % 2 == 0: # Check if the number is divisible by 2
        return("The number is even.")
    else:
        return ("The number is odd.")
# Main function
def main():
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = even_or_odd(number)
    print(result)
if __name__ == "__main__":
    main()