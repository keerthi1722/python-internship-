name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? (left/right): ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. What do you choose? (walk/swim): ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator. Game over 💀.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game. Game over 💀.")
    else:
        print("Not a valid option. You lose 💀.")

elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or go back? (cross/back): ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no): ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win! 🏆")
        elif answer == "no":
            print("You ignore the stranger and they get angry. You lose 💀.")
        else:
            print("Not a valid option. You lose 💀.")

    elif answer == "back":
        print("You go back and lose. Game over 💀.")
    else:
        print("Not a valid option. You lose 💀.")

else:
    print("Not a valid option. You lose 💀.")
