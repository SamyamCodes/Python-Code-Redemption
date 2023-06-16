#           *** Program ****
def body_mass_index():

    weight = input("Enter your weight")
    height = input("Enter your height")

    bmi = int(weight)/float(height)

    print(f"Your weight is{weight} ")
    print(f"Your height is {height}")
    bmi_as_int = int(bmi)
    print(f"Your body mass index is :{bmi_as_int} ", bmi_as_int)

def two_digit_sum():

    two_digit_number = input("Enter a two digit number required for the sum: ")
    first_digit = int(two_digit_number[0])
    second_digit = int(two_digit_number[1])
    add = first_digit + second_digit
    print("The sum of the digits of the given number is :", add)

def bill_calculator():
    print("                   ****  Welcome to the bill calculator ****             ")
    total_bill = int(input("What is you total bill in NRS.? : "))
    tip_percent = int(input("What percent tip do you want to give? 5, 7, 9, 12 : "))
    people = int(input("How many people you want to split the bill?: "))
    tip = (total_bill * tip_percent)/100
    bill_in_total = tip + total_bill
    bill_per_person = bill_in_total/people

    print("Your total bill is : Rs.", total_bill)
    print("Your total bill after tip is : Rs.", bill_in_total)
    print("Each person has to pay: Rs.", bill_per_person)

def bmi_compare():
    height = float(input("Enter your height in m: "))
    weight= float(input("Enter you weight in kg. : "))

    bmi = round(weight/height**2 )
    if bmi < 18.5:
        print(f"Your bmi is {bmi} and you are underweight. ")
    elif bmi < 25:
        print(f"Your bmi is {bmi} and you have a normal weight")
    elif bmi < 30:
        print(f"Your bmi is {bmi} and you are slightly overweight.")   
    elif bmi < 35:
        print(f"Your bmi is {bmi} and you are obese.")
    else:
        print(f"Your bmi is {bmi } and you are critically obese.")

def love_calculator():

    # print("Samyamsas".lower().count("s"))
    print("Welcome to love calculator.")
    name1 = input("Enter your name: ")
    name2 = input("Enter your lover's name: ")

    combined_name = name1 + name2
    t = combined_name.lower().count("t")
    r = combined_name.lower().count("r")
    u = combined_name.lower().count("u")
    e = combined_name.lower().count("e")

    true = t+r+u+e

    l = combined_name.lower().count("l")
    o = combined_name.lower().count("o")
    v = combined_name.lower().count("v")
    e = combined_name.lower().count("e")
    love = l+o+v+e

    love_score = int(str(true)+str(love))

    if (love_score <10 ) or (love_score > 90):
        print(f"Your love score is{love_score} and you go like. ")
    elif (love_score) and (love_score<= 50):
        print(f"Your love score is {love_score} and you go like all right together " )
    else:
        print(f"Your score is {love_score} and you are not together")


# Start from Here
# https://github.com/SamyamCodes/100-days-of-learning-python/blob/master/Day%204/lists.py









