def greet():
    print("Hi")

greet(); 

def greet_with_name(name,location):
    print(f"hi {name}")
    print(f"What is it like in {location}")

    
greet_with_name(name=input("Whats your name?"), location=input("Where you live?"))


#Prime NUMBER sometimes a leetcode question 

def prime_checker(number):
    is_prime=True
    for i in range (2,number):
        if number%i==0:
            is_prime= False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



#encoding messages 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  cipher_text=""
  for letter in text:
  
    position = alphabet.index(letter)
    new_position = position+shift
    new_letter=alphabet[new_position]
    cipher_text +=new_letter
  print(f"the encode text is {cipher_text}")

def decrypt(text, shift):
  cipher_text=""
  for letter in text:
    position=alphabet.index(letter)
    new_position=position-shift
    new_letter=alphabet[new_position]
    cipher_text +=new_letter
  print(f"the decoded text is {cipher_text}")


if direction == "encode":
  encrypt(text,shift)
elif direction == "decode":
  decrypt(text,shift)
else: 
  print("Please choose encode or decode")


  #we can simplify our code as such 
  def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



caesar(start_text=text, shift_amount=shift, cipher_direction=direction)