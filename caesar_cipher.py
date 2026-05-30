def caeser_cipher(message,shift):
    
    result=""

    for char in message:
    
      if char.isalpha():
      
         if char.islower():
           result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
           
         else:
           result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
           
      else:
        result+=char
        
    return result    
   
   
while True:
  message=input("Enter message:")
  shift=int(input("Enter shift:"))

  print("---Caeser Cipher---")
  print("1.Encrypted")
  print("2.Decrypted")
  print("3.Exit")
  choice=input("Enter choice:")

  if choice=='1':
    
    encrypted=caeser_cipher(message, shift)  
    print("Encrypted:", encrypted)
    
  elif choice=='2':  
      
    decrypted=caeser_cipher(message, -shift)
    print("Decrypted:", decrypted)
    
  elif choice=='3':
    
    print("Exiting program...")
    break

  else:
    print("Invalid choice")







# message=input("Enter the message:")
# shift=int(input("Enter the shift:"))

# encrypted=""

# for char in message:
    
#     if char.isalpha():
        
#         # ascii_value=ord(char) #convert in ascii value
#         # new_ascii=ascii_value+shift
#         # new_char=chr(new_ascii)

#         if char.islower():
#             new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

#         else:
#             new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        
#         encrypted+=new_char
#     else:
#         encrypted+=char    
        
# print("Encrypted message:",encrypted)