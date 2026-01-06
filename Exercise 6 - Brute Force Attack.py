# This is the provided correct password which the user must input when logging in
password = "admin123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter Password: ")
    attempts = attempts + 1
    
    if user_input == password:
        print("Access Granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print("Incorrect password! Try again")
        else:
            print("Account Locked! Too many attempts.")