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
print('''0 for rock
1 for paper
2 for scissors''')
user1 = int(input("What is your choice: "))
print("Your move")
if user1 == 0:
    print(rock)
elif user1 == 1:
    print(paper)
elif user1 == 2:
    print(scissors)
else:
    print("Enter a valid number!")
user2 = random.randint(0,2)
win = [[0,2],[1,0],[2,1]]
print("Opponents move")
if user2 == 0:
    print(rock)
elif user2 == 1:
    print(paper)
elif user2 == 2:
    print(scissors)
else:
    print("Opponent is mad!")
dis = [user1,user2]
if user1 == user2:
    print("Draw")
elif dis in win:
    print("You won!")
else:
    print("You lose!")
