import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


total = nr_letters + nr_symbols + nr_numbers

password = ''
arr = ['letter','number','symbol']
for i in range(0, total):
    ran = random.choice(arr)
    if ran == 'letter':
        ranletter = random.choice(letters)
        password += ranletter
        nr_letters -= 1
        if nr_letters == 0:
            arr.remove('letter')
    elif ran == 'number':
        rannumber = random.choice(numbers)
        password += rannumber
        nr_numbers -= 1
        if nr_numbers == 0:
            arr.remove('number')
    elif ran == 'symbol':
        ransymbol = random.choice(symbols)
        password += ransymbol
        nr_symbols -= 1
        if nr_symbols == 0:
            arr.remove('symbol')

print(f"Password: {password}")
