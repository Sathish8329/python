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

#Write your code below this line 👇

import random
choice = int(input("please select a number 0 for rock, 1 for paper, 2 for scissors\n"))
user_choice = [rock, paper, scissors]
print(user_choice[choice])
computer_choice = random.randint(0,2)
print(computer_choice)
print(user_choice[computer_choice])
if choice == 0 and computer_choice == 2:
    print("user won")
elif choice == 1 and computer_choice == 0:
    print("user won")
elif choice == 2 and computer_choice == 1:
    print("user won")
elif choice == 0 and computer_choice == 1:
    print("computer won")
elif choice == 1 and computer_choice == 2:
    print("computer won")
elif choice == 2 and computer_choice == 0:
    print("computer won")
else:
    print("draw")
