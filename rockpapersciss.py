import random 

computer_wins = 0
user_wins = 0 
options = ["rock","paper","scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit ")
    if user_input == "q":
        break
        
    if user_input not in options:
        continue
         
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick + "." )    
    if user_input.lower() == "rock" and computer_pick.lower() == "scissors":
        print("You win")
        user_wins += 1
        continue
    
    
    if user_input.lower() == "rock" and computer_pick.lower() == "scissors":
        print("You won")
        user_wins += 1       
   
   
    elif user_input.lower() == "paper" and computer_pick.lower() == "rock":
        print("You won")
        user_wins += 2
            
        
    elif user_input.lower() == "scissors" and computer_pick.lower() == "paper":
        print("You won")
        user_wins += 3
    
    else:
        print("You lost")
        computer_wins += 1
        
print("You won ", user_wins ,"times.")
print("Computer won ", computer_wins ,"times.")        
            
print("Goodbye! ")