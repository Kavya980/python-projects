import random

options=["rock","paper","scissors"]

user_score=0
computer_score=0

print("Welcome to Rock🪨 Paper📄 Scissors✂️  game: ")
num=1
while True:
  
    print("Round", num)
    user=input("Enter rock🪨 (r), paper📄 (p), or scissors✂️ (s) to play or type 'quit' to exit:\n").lower()
      
    if user=="quit":
      print("You quit the game!")
      break
    elif user=="r":
      user="rock"
    elif user=="p":
      user="paper"
    elif user=="s":
      user="scissors"
    elif user not in options:
      print("❌ Invalid choice! Try again.")
      continue
    
    computer=random.choice(options)
    print("Computer's choice: ",computer)
    
    if user==computer:
      print("It is a tie")
     
    elif (user=="rock" and computer=="scissors") or (user=="paper" and computer=="rock") or(user=="scissors" and computer=="paper"):
      print("You win this round!")
      user_score+=1
    else:
      print("You lose this round!")
      computer_score+=1   
    print("Your Score->",user_score,"Computer's score:",computer_score)

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        break
    num+=1
    print("------------------------------")
    
print("\nFinal scores🏁:")
print("You:", user_score)
print("Computer:", computer_score)
    
if user_score>computer_score:
    print("You won the game!🎉🎮")
elif user_score<computer_score:
    print("You lost the game!👎")
else:
    print("It's a tie!🤝")
    
print("Thanks for playing!")