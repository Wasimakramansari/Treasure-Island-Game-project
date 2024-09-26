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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
Choice1 = input('You\'re at a crossroad, where do you want to go?'
                ' Type "left"  "right".\n').lower()

if Choice1 == "left":
    choice2 = input('You\'re at the lake.There is an island at the middle of the lake.'
                    ' Type "wait" for a boat. Type "swim" for swimming\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the lake unharmed. "
                        "There is a palace which has three doors."
                        " One red. One yellow and one blue. "
                        "Which colour do you choose.\n").lower()
        if choice3 == "red":
            print("You are burned by fire. Game over")
        elif choice3 == "yellow":
            print("Hurrah! you got the treasure. You win")
        elif choice3 == "blue":
            print("Eaten by beast. Game over")
        else:
            print("You choose a wrong door. Game over")
    else:
        print("You are attacked by trout. Game over")
else:
    print("You fall into the hole. Game over")