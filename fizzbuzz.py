#  Range: for i in range(a,b):
    # Do something

# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# sum = 0
# for n in range(0, 101, 2):  sum of first 100 even numbers.
#     sum += n
# print(sum)
  
# Fizz BUZZ
for n in range(1, 101):
    if n % 3 == 0 and n% 5 == 0:
        print("FizzBuzz")
    elif n% 3 == 0:
        print("Fizz")
    elif n% 5 == 0:
        print("Buzz")
    else:
        print(n)



