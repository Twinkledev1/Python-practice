import random

# define the function rock_paper_scissors

def rock_paper_scissors():
    
    choices = ["rock", "paper", "scissors"]

    print("Welcome to rock, paper, scissor game. Lets play!")
    print ("Type 'rock', 'paper', 'scissors' to play the game")
    print("Type 'quit' to stop the game. ")
    
    # apply the while loop to play the game
    while True:

      # computer takes a random choice
        computer_choice = random.choice(choices)

     # user choose the input

        user_choice = input("Enter your choise: ").lower()

     # condition when user wants to qite the game

        if user_choice == "quit":
            print("Thanks for playing the game. Goodbye!")
            break

    # Validate user input
        if user_choice not in choices :
            print("Invalid choice! please choose 'rock' 'paper', 'scissors'.")
            continue
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

    # Determine the winner
    # condition when game is tie
        if user_choice == computer_choice:
            print("Try again! its tie")

        elif (user_choice == 'rock' and computer_choice == 'scissors' ) or (user_choice == 'scissors' and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
            print("You wins!")
            
        else:
            print("Computer wins!")
       


rock_paper_scissors()