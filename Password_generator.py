import random 
import string

length=int(input("Enter the required password length: "))

letters=string.ascii_letters
digits=string.digits
symbols=string.punctuation

password=[]

password.append(random.choice(letters))
password.append(random.choice(digits))
password.append(random.choice(symbols))

all_characters=letters + digits + symbols

for i in range(length-3):
    password.append(random.choice(all_characters))
    
random.shuffle(password)

final_password="".join(password)

print("Password Generated: ",final_password)