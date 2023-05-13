alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(text,shift,direction) :
 cipher_text = ""
 if direction == "decode":
     shift *= -1
 for char in text :
   if char in alphabet:
     position = alphabet.index(char)
     new_position  = position + shift
     cipher_text += alphabet[new_position]
   else:
     cipher_text += char
 print(f"The {direction}d text : {cipher_text} ")

Continue = True
while Continue:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  
  caesar(text,shift,direction) 
  result = input("Type 'Yes' if you want to go again. otherwise type 'No'.\n").lower()
  if result == 'no':
    Continue = False
    print("Goodbye...")

 



































































#Created by Karthik Ganapa R