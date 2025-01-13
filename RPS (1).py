wins = 0
loss = 0
ties = 0
def rpsgame():
    global wins
    global loss
    global ties
    while True:#infinite Loop
        import random
        print ("Welcome to Rock, Paper, Scissors")
        print("What is your move?")
        player = input ("Rock, Paper, Scissors. Go:") #string
        player = player.lower()
        computer= random.randint(1,3)
        if computer == 1 :
            computer = "rock"
            print("The Computer's move is Rock!")
        if computer == 2 :
            computer = "paper"
            print("The Computer's move is Paper!")
        if computer == 3 :
            computer = "scissors"
            print("The Computer's move is Scissors!")
        if player == "rock" and computer == "rock":
            print ("Its a Tie!")
            ties = ties+1
        if player == "paper" and computer == "paper":
            print ("Its a Tie!")
            ties = ties+1
        if player == "scissors" and computer == "scissors":
            print ("Its a Tie!")
            ties = ties+1
        if player == "rock" and computer == "paper":
            print ("Computer wins!")
            loss = loss+1
        if player == "rock" and computer == "scissors":
            print ("Player wins!")
            wins= wins+1
        if player == "paper" and computer == "rock":
            print ("Player wins!")
            wins= wins+1
        if player == "paper" and computer == "scissors":
            print ("Computer wins!")
            loss = loss+1
        if player == "scissors" and computer == "pock":
            print ("Computer wins!")
            loss = loss+1
        if player == "scissors" and computer == "paper":
            print ("Player wins!")
            wins= wins+1
        playagain = input ("Do you want to keep playing?")
        if playagain.lower()== "yes":
            print ("restarting...")
        else:
            print("Thanks for playing !")
            break
rpsgame()
