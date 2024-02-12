name = input("Type your name: ")
print("Hello,", name + ", " + "Welcome to adventure ")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around or swim to swim across: ")
    if answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    elif answer == "swim":
        print("You swam across the river and were eaten by an alligator. ")
    else:
        print("Not a valid option. You lose ")
    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back: ")
    if answer == "back":
        print("You go back where you started from and you lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger, do you talk to them (yes/no) ")
        if answer == "yes":
            print("You talked to the stranger and they take you to treasure. You win.")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option you lose")
    else:
        print("Not a valid option. You lose ")
else:
    print("Not a valid option. You lose")

print("Thank you for playing", name)
