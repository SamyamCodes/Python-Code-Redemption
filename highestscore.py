# WAP to generate the highest score from the given list.

# Note that we can use max(scores_list). But here use for loop.

scores_list = input("Enter the scores of the students of the class: ").split()
for n in range(0, len(scores_list)):
    scores_list[n] = int(scores_list[n])

highest_score = 0
for score in scores_list:
    if score > highest_score:
        highest_score = score
       
print("The highest score is: ", highest_score)
print(max(scores_list))




