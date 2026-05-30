print("Simple Calculator")

while True:
 n1=float(input("Enter first number:"))
 op=input("Enter operand(+,-,*,/):")
 n2=float(input("Enter second number:"))

 if op=="+":
    print("Result:",n1+n2)
 elif op=="-":
    print("Result:",n1-n2)
 elif op=="*":
    print("Result:",n1*n2)
 elif op=="/":
    if n2!=0:
      print("Result:",n1+n2)
    else:
      print("Can't divided by zero!")
 else:
    print("Invalid operator!")
 again = input("Do you want to calculate again? (yes/no): ").lower()
 if again!= "yes":
    print("Calculator closed.")
    break