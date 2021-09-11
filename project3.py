print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
step1 = input("Where do you wanna go Left or Right: ")
if step1.lower() == "left":
    print("You came to a lake! There is a island in the middle of the lake. Do you wanna wait or wanna swim to get to the island")
    step2 = input("What do wanna do swim or wait: ")
    if step2.lower() == "wait":
        print("A boat arrived!")
        print("You reached the island unhurmed")
        step3 = input("There is a house with 3 doors. red,yellow and blue. Which door color do you choose: ")
        if step3.lower() == "yellow":
            print("You Win")
        elif step3.lower() == "red":
            print("You got burned by fire")
            print("Game over!")
        elif step3.lower() == "blue":
            print("You got eaten by beast!")
            print("Game over!")
        else:
            print("You did not choose any of the door so a demon came and took you away to his den")
            print("Game over!")
    else:
        print("Attacked by a trout")
        print("Game over!")
else:
    print("Fall into a hole\nGame OVER!")