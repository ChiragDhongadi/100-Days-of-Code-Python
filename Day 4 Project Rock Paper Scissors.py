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
game_image = [rock,paper,scissors]

user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_image[user_num])

comp_num = int(random.randint(0,2))

print(f"Computer chose : {comp_num}")
print(game_image[comp_num])

# GAME RULES :
if user_num >= 3 or user_num < 0:
    print("You typed an invalid number. You lose!")
elif user_num == 0 and comp_num == 2:
    print("You win!")
elif user_num == 2 and comp_num == 0:
    print("You lose!")
elif user_num < comp_num:
    print("You lose!")
elif comp_num < user_num:
    print("You win!")
elif user_num == comp_num:
    print("It's draw")




