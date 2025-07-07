letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#for letters to be used in the password
import random
letterlist =[]
for i in range(0 , nr_letters):
    letterlist.append(random.randint(0,len(letters)-1))
    letterlist[i] = letters[letterlist[i]]

#for symbols to be used in the password
symbollist =[]
for i in range(0 , nr_symbols):
    symbollist.append(random.randint(0,len(symbols)-1))
    symbollist[i] = symbols[symbollist[i]]

#for numbers to be used in the password
numberlist =[]
for i in range(0 , nr_numbers):
    numberlist.append(random.randint(0,len(numbers)-1))
    numberlist[i] = numbers[numberlist[i]]


total_length = nr_letters + nr_numbers + nr_symbols

letterr = nr_letters
symr = nr_symbols
numr = nr_numbers
queue = []

for i in range(total_length*10):
    if len(queue) >= total_length:
        break

    choice = random.randint(1,3)
    if choice == 1 and letterr > 0:
        letterr -= 1
        queue.append(1)
    elif choice == 2 and symr > 0:
        symr -= 1
        queue.append(2)
    elif choice == 3 and numr > 0:
        numr -= 1
        queue.append(3)

password = []
letterq = 0
symq = 0
numq = 0


for k in range(total_length):
    if queue[k] == 1:
        password.append(letterlist[letterq])
        letterq += 1
    elif queue[k] == 2:
        password.append(symbollist[symq])
        symq += 1
    elif queue[k] == 3:
        password.append(numberlist[numq])
        numq += 1

NewPassword = ""

for f in range(total_length):
    NewPassword = NewPassword + password[f]

print("your password is", NewPassword)