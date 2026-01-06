# This will get the user input
name = input("Enter your name: ")
city = input("Enter your city: ")
age_input = input("Enter your age: ")

# This check if the provided age is a number
if age_input.isdigit():
    age = int(age_input)
else:
    print("Age must be a value.")
    age = 0

# This stores in dictionary which will prompt the user accordingly
person = {
    "name": name,
    "city": city,
    "age": age
}

print("Name:", person["name"], "\nCity:", person["city"], "\nAge:", person["age"])
# This prints a separate line which the user must asnwer accordingly