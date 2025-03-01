# Password-Generator

This project contains two Python scripts (`easy.py` and `hard.py`) that generate random passwords based on user input. The passwords can include letters, numbers, and symbols.

## Concepts Implemented
- Random number generation
- String manipulation
- User input handling
- Looping
- Conversion of lists to strings

## Files

- `assets.py`: Contains the lists of letters, numbers, and symbols used in the password generation, as well as a welcome message.
- `easy.py`: Generates a password without shuffling the characters.
- `hard.py`: Generates a password and shuffles the characters for added security.

## How to Use

1. Run either the `easy.py` or `hard.py` script.
2. Enter the number of letters, symbols, and numbers you would like in your password when prompted.
3. The script will generate and display a random password based on your input.

### Example

```sh
$ python easy.py
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
3
Your password is: aBcD$!123

$ python hard.py
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
3
Your password is: 1a!B2$cD3