#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

len_of_pass = int(nr_letters) + int(nr_symbols) + int(nr_numbers)
len_of_letters = int(nr_letters)
len_of_symbols = int(nr_symbols)
len_of_numbers = int(nr_numbers)

password = ""
for i in range (0, len_of_pass):
    if len_of_letters > 0:
        password += random.choice(letters)
        len_of_letters -= 1
    elif len_of_symbols > 0:
        password += random.choice(symbols)
        len_of_symbols -= 1
    elif len_of_numbers > 0:
        password += random.choice(numbers)
        len_of_numbers -= 1

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
len_of_pass1 = int(nr_letters) + int(nr_symbols) + int(nr_numbers)
len_of_letters1 = int(nr_letters)
len_of_symbols1 = int(nr_symbols)
len_of_numbers1 = int(nr_numbers)

password1 = ""
for i in range(len_of_pass1):
    random_number = random.randint(0, 2)

    if random_number == 0:
        if len_of_letters1 > 0:
            password1 += random.choice(letters)
            len_of_letters1 -= 1
        elif len_of_symbols1 > 0:
            password1 += random.choice(symbols)
            len_of_symbols1 -= 1
        else:
            password1 += random.choice(numbers)
            len_of_numbers1 -= 1
    elif random_number == 1:
        if len_of_symbols1 > 0:
            password1 += random.choice(symbols)
            len_of_symbols1 -= 1
        elif len_of_letters1 > 0:
            password1 += random.choice(letters)
            len_of_letters1 -= 1
        else:
            password1 += random.choice(numbers)
            len_of_numbers1 -= 1
    else:
        if len_of_numbers1 > 0:
            password1 += random.choice(numbers)
            len_of_numbers1 -= 1
        elif len_of_letters1 > 0:
            password1 += random.choice(letters)
            len_of_letters1 -= 1
        else:
            password1 += random.choice(symbols)
            len_of_symbols1 -= 1

print(password1)




