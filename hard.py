from assets import letters, numbers, symbols, message
from random import choice, shuffle

print(message)

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []

for char in range(0, nr_letters):
    password_list.append(choice(letters))
for sym in range(0,nr_symbols):
    password_list.append(choice(symbols))
for num in range(0,nr_numbers):
    password_list.append(choice(numbers))

shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")