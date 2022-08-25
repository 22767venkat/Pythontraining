player1=input("p1 turn")
player2=input("p2 turn")
if (player1 == "Rock" and player2=="Scissors") or(player1 == "Scissors" and player2=="paper") or ( player1 == "paper" and player2 == "Rock"):
    print("Player1 won")
elif(player1==player2):
    print("It is a tie Break")
else:
    print('given a unauthorised sign')