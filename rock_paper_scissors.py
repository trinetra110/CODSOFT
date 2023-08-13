import random

c="yes"
i=1
lst=["rock","paper","scissors"]
user_score=0
comp_score=0
while c.lower() not in "noNO":
    print(f"Round {i}:")
    print("ROCK PAPER SCISSORS\n")
    user_choice=input("Enter your choice: ")
    if user_choice.lower() not in lst:
        print("Invalid input ! Please try again\n")
        continue
    else:
        computer_choice = random.choice(lst)
        print(f"You chose: {user_choice}\ncomputer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("Result: It's a tie\n")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("Result: You win!\n")
            user_score += 1
        else:
            print("Result: You lose!\n")
            comp_score += 1
    print(f"Your score: {user_score}\nComputer score: {comp_score}\n")
    c=input("Do you want to play more? Enter 'no' to exit or 'yes' to continue: ")
    i+=1