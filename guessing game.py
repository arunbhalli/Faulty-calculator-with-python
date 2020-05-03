import random
print("Welcome to guessing game.","You will have only five attempts")
print("Given no will be in the range of 1 to 20")
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Enter your no.")
player1=random.choice(lst)
atte = 1
while atte<=5:
  player2 = int(input())
  if player2 > player1:
     print("Your no. is greater than player 1.")
     print("Your left attempts are:",5-atte)
  elif player2 < player1:
     print("Your no is less than player 1.")
     print("Your left attempts are:",5-atte)
  elif player1 == player2:
     print("You guessed right no.")
     print("&&&&&&&&&& :) YOU WON THE GAME :)  &&&&&&&&&&&")
     break
  atte+=1
  if atte==6:
    print("GAME IS OVER ")

print("     THANK YOU FOR PLAYING      ")
