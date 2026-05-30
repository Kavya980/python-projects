print("Welcome to the Quiz!\n")
score=0

questions={
    "What is the capital of India? ":"delhi",
    "Who created Python? ":"guido van rossum",
    "Add 5+7? ":"12",
    "What does CPU stands for? ":"central processing unit"
} 

for ques,ans in questions.items():
    user_ans=input(ques)
    
    if user_ans.lower()==ans:
      print("Correct!")
      score+=1
      
    else:
      print("Wrong Answer!") 
      print("Correct answer is ",ans)
    
print("-------Quiz ended-------")
print("Your score: ",score,"/",len(questions))    
if score==len(questions):
    print("Excellent!")
elif score>=len(questions)/2:
    print("Good job!")
else:
    print("Better luck next time!")
