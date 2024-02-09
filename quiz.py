print("Welcome to the quiz")

playing = input("Do You want to play ")

if playing.lower() == "yes" :
    print(playing)
    
print("OK let's play:)")
score = 0

answer = input("What does CPU stands for? ")
if (answer.lower() == "central processing unit "):
    print("Correct")
    score += 1

else:
    print("Incorrect")

answer = input("What does GPU stands for? ")
if (answer.lower() == "graphics processing unit"):
    print("Correct")
    score += 2

else:
    print("Incorrect")
    
answer = input("What does RAM stands for? ")
if (answer.lower() == "random access memory"):
    print("Correct")
    score += 3

else:
    print("Incorrect")

answer = input("What does ROM stands for? ")
if (answer.lower() == "read only memory"):
    print("Correct")
    score += 4

else:
    print("Incorrect")

answer = input("What does PSU stands for? ")
if (answer.lower() == "power supply"):
    print("Correct")
    score += 5

else:
    print("Incorrect")

print("You got " + str((score*4)/100) + " questions correct ")

 