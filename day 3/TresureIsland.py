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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')


print("Welcome to the Treasure Island. ")
print("Your mission is to find the treasure. ")

cross_road = input('Your\'re at a crossroad. Where do you want to go? Type "left" or "Right" ').lower()
if cross_road == "left":
    lake = input('You come to a lake. There is an island in the middle of the island. Type "wait" to wait for a boat. Type "swim" to swim across.  ').lower()
    if lake == "wait":

        door = input("You arrived at the island unharmed. There is a house with three doors. One red,one yellow and one blue. Which  colour do you choose? ").lower()
        if door == "red":
            print("Room is full of fire. Game Over.")
        
        elif door == "yellow":
            print("You found the treasure. You win. ")
        elif door == "blue":
            print("Your enter a room of bones. Game over.")
        else:
            print("You chose a door that doesn't exist.")
    else:
        print("You're caught by shark. Game Over.")

else:
    print("You fell into a hole. Game Over.")    