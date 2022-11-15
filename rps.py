import random

exit = False

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Scissors
'''
user_point = 0
com_point = 0



while exit == False:
    print()
    user = int(input('Choose 1. Rock, 2. Paper, 3. Scissors , 4. Exit  '))
    com = random.randint(1,3)

    if user == 4:
        print("--------------------------------------------")
        print("End Game")
        print("The User point:",user_point)
        print("The computer point:",com_point)
        print('Good Day mate, what a champ!')
        print("--------------------------------------------")
        print()
        exit = True
        break


    if user >4 or user < 0:
        print("You input the in valid number, youlose!")
        print("The User point:",user_point)
        print("The computer point:",com_point)
        com_point += 1
    elif user == 1:
        print(rock, "User Choose Rock")
    elif user == 2:
        print(paper, "User Choose Paper")
    else:
        print(scissors, "User Choose Scissors")
    
    if com == 1:
        print(rock, "Com Choose Rock")
    elif com ==2:
        print(paper, "User Choose Paper")
    else: 
        print(scissors,"Com Choose Scissors")

    if com == user:
        print()
        print("Draw")
        print()
        print("The User point:",user_point)
        print("The computer point:",com_point)
    elif user == 1 and com == 2: 
        print()
        print("You Lose")
        print()
        com_point += 1
        print("The User point:",user_point)
        print("The computer point:",com_point)
    elif user == 1 and com == 3: 
        print()
        print("User Win")
        print()
        user_point += 1
        print("The User point:",user_point)
        print("The computer point:",com_point)
    elif user == 2 and com == 1: 
        print()
        print("User win")
        print()
        user_point += 1
        print("The User point:",user_point)
        print("The computer point:",com_point)
    elif user == 2 and com == 3: 
        print()
        print("You Lose")
        print()
        com_point += 1
        print("The User point:",user_point)
        print("The computer point:",com_point)
    elif user == 3 and com == 1:
        print()
        print("You lose")
        print()
        com_point += 1
        print("The User point:",user_point)
        print("The computer point:",com_point)
    elif user == 3 and com == 2:
        print()
        print("You win")
        print()
        user_point += 1
        print("The User point:",user_point)
        print("The computer point:",com_point)
