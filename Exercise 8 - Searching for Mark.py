# This is a list of names
names = ["Abi", "Mark", "Roschelle", "Lea", "Rowel", "Yen"]
# This is a search term so the user would be easier to find
search = input("Enter name to search: ")

if search in names:
    print(search, "Found on the list!")
else:
    print(search, "Not in the list!")