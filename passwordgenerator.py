
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("                     Welcome to Password Generator                        ")
nr_numbers = int(input('Enter how man numbers would you like? \n'))
nr_letters = int(input("Ener how many lettters you would like ? \n"))
nr_symbols = int(input('How many symbols would you like? \n'))

# Easy level
# password = ''

# for charc in range(1, nr_letters+1):
#    password+= random.choice(letters)

# for charc in range(1, nr_symbols+1):
#    password+= random.choice(symbols)

# for charc in range(1, nr_numbers+1):
#    password+= random.choice(numbers)

# print(password)

# Hard level.


password_list = []

for charc in range(1, nr_letters+1):
   password_list += random.choice(letters)

for charc in range(1, nr_symbols+1):
   password_list += random.choice(symbols)

for charc in range(1, nr_numbers+1):
   password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password+= char

print(f"Your password can be: {password}")
  