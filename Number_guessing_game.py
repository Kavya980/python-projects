import random
    
print("Welcome to Number Guessing Game!")
number=random.randint(1,100)

att=0   
while True:
  try:
    user=int(input("Guess the number(1-100):"))
    att+=1
    if user<=100 and user>0:
       if user>number:
        print("Too high!")  
       elif user<number:
        print("Too low!") 
       else:
        print("Correct!You guessed it in",att,"attempts!")
        break
    else:
        print("Please enter a valid number!")
        
  except:
        print("Invalid input! Please enter a number.")