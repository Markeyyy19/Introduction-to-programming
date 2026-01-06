name = input("Enter your name: ")
city = input("Enter your city: ")
age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)
else:
    print("Age must be a value.")
    age = 0

person = {
    "name": name,
    "city": city,
    "age": age
}

print("Name:", person["name"], "\nCity:", person["city"], "\nAge:", person["age"])