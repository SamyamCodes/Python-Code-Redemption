print("Welcome to Leap Year Finder")
year = int(input("Enter the  year you want to check the leap year for: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not leap year.")   
    else:
        print("Leap Year")
else:
    print("Not leap year.")
