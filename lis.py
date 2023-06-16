thislist = ["apple", "banana", "orange", "mango", "lemon", "cherry", "kiwi"]
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# Use in keyboard to check the item in the list.
if "pineapple" in  thislist:
    print("It is in the list.")
else:
    print("Pineapple is not in the list.")

thislist[1] = "pineapple"
print(thislist[1])
print(thislist)
print(len(thislist))
thislist.append("jackfruit")
print(thislist)
print(len(thislist))
list1 = ["cherry", "papaya", "strawberry"]
thislist.extend(list1) # .extend() adds the another list to the existing list. 
print(thislist)
print(len(thislist))
