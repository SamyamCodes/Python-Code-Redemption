def pay():

    import random

    names_string = input("Give me everybody's name separated by comma: ")
    names = names_string.split(", ") #The split() method splits a string into a list.
    print(names)

    # txt = "apple#banana#cherry#orange"

    # # setting the maxsplit parameter to 1, will return a list with 2 elements!
    # x = txt.split("#", 1)

    # print(x)


    items = len(names)

    random_choice = random.randint(0, items -1)
    print(random_choice)
    person_who_pay = names[random_choice]
    print(person_who_pay + " is going to buy the meal today.")

import random
names_list = input("enter your friend's name separated by comma.")
names = names_list.split(", ")

no_list = len(names)
print(f"There are {no_list} of you.")
random_choice = random.randint(0, no_list -1)
person_who_pay = names [random_choice]
print(person_who_pay + " is going to pay the bill today.")
print("                 *** Have a nice day! ***                    ")
