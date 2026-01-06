def check_even_odd(number): # This is a function that checks if the number is even or odd
    if number % 2 == 0: # This will check if the number is divided by 2 and has no remainder
        return "The number is even"
    else:
        return "The number is odd"
# The return will sends the message back to the main function
def main():
    num = int(input("Enter a number: "))
    message = check_even_odd(num)
    print(message)

if __name__ == "__main__":
    main() # This gets the users input, calls function, and prints result