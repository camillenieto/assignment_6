#Program 2: Addition Trainer
#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)
name = input("Enter Name: ")

print(f"Welcome to Addition Trainer!", name)
print("Answer the following addition excercises. Good Luck!")

import random 
score = 0

for i in range(10) :
    number_one = random.randint(0,99)
    number_two = random.randint(0,99)
    print(f"{number_one} + {number_two} =")
    add = number_one + number_two
    sum = int(input(f"The sum is "))

    if add == sum :
        print("Your answer is correct! Keep it up!")
        score += 1
    else:
        print("Sorry, your answer is incorrect. ")
        if add != sum :
            print("The correct answer is ", add)

print(f"Total score: {score}/10")

def outro() :
    if score == 0 :
        print(f"Please study hard!")
    elif score >= 1 and score <= 4 :
        print(f"Not bad. Try and try until you get more score. :)")
    elif score >= 5 and score <= 8 :
        print(f"Great! Keep working on it; you’re improving. ")
    else:
        if score == 10 :
            print(f"Excellent! You’ve got your brain in gear today.")

outro()

print(f"Addition Genius, {name}. You have completed this assessment!")
print(f"Thank you for using Addition Trainer")