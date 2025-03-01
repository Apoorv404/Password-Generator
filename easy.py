from assets import letters, numbers, symbols, message
from random import choice

print(message)

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range (0, nr_letters):
    password += choice(letters)
for sym in range (0, nr_symbols):
    password += choice(symbols)
for num in range(0, nr_numbers):
    password += choice(numbers)

print(f"Your password is {password}")