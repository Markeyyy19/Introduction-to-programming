# This is a dictionary of days and months in a year
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# This asks the user for preferred month in a year
month = int(input("Enter month number: "))

# This will check if the preferred month is valid within the year
if month >= 1 and month <= 12:
    # This is a special check for the month "February" because of its leaping year once in four years
    if month == 2:
        year = input("Is it a leap year? (yes/no): ")
        if year == "yes":
            print("Days: 29")
        else:
            print("Days: 28")
    else:
        print("Days:", months[month])
else:
    print("Invalid month number!")