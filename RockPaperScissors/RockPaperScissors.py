import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = random.randint(1,3)

if choice == 1:
    computer_choice = rock
elif choice == 2:
    computer_choice = paper
elif choice == 3:
    computer_choice = scissors

user_choice = input("Rock...Paper...Scissors...Shoot! (pick rock, paper or scissors) ")
if user_choice == "rock":
    user_choice = rock
elif user_choice == "paper":
    user_choice = paper
elif user_choice == "scissors":
    user_choice - scissors

print(user_choice)
print(computer_choice)

if user_choice == computer_choice:
    print("It's a tie!\n")
elif (user_choice == rock and computer_choice == scissors) or (user_choice == paper and computer_choice == rock) or (user_choice == scissors and computer_choice == paper):
    print("You win!\n")
else:
    print("You lose!\n")