choice = str(input("Enter the player you want to make choice : "))
if choice.lower() == "player_one".lower():
    player_1 = int(input("Hey Player 1! Guess a number : "))
    player_2 = int(input("Hey Player 2! Now you guess a number : "))
    if player_1 == player_2:
        print("Hey Player 2! You guessed it right!")
    else:
        print("Oops Player 2! You guess it wrong!")

elif choice.lower() == "player_two".lower():
    player_2 = int(input("Hey Player 2! Guess a number : "))
    player_1 = int(input("Hey Player 1! Now you guess a number : "))
    if player_2 == player_1:
        print("Hey Player 1! You guessed it right!")
    else:
        print("Oops Player 2! You guessed it wrong!")
