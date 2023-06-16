print("Welcome to the tip calculator.")
bill = float(input("What is the total bill? $"))

tip_percent = int(input("What percentage tip do you want to give? 10, 12, or 15?% "))
no_people = int(input("How many people do you want to split the bill? "))

total_bill = bill + bill* (tip_percent/100)
round_total_bill = round(total_bill, 2)

each_person_bill = round(round_total_bill/no_people, 2)

print(f"Each person should pay: ${each_person_bill}")
