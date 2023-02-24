#Password Generator Project
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_count=0
symbol_count=0
number_count=0

options = [letters,numbers,symbols]
password_random =""
while(letter_count != nr_letters or symbol_count != nr_symbols or number_count != nr_symbols):
  lns_random = options[random.randint(0,2)]
  if(letter_count < nr_letters and lns_random == letters):
    password_random += random.choice(letters)
    letter_count+=1
  elif(symbol_count < nr_symbols and lns_random == symbols):
    password_random +=random.choice(symbols)
    symbol_count+=1
  elif(number_count < nr_numbers and lns_random == numbers):
    password_random += random.choice(numbers)
    number_count+=1

print(password_random)