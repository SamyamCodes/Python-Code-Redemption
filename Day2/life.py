age =  int(input("Enter your age in years old: "))
years_left = 90 - age


week_left = int((90*52) - (age*52))
days_left = int((90*365) - (age*365))
months_left = int((90*12) - (age*12))

print(f"You have {days_left} days, {week_left} weeks, and {months_left} months left.")
