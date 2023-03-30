from random import choice, shuffle

print("Welcome to PassWord generator!")
quantity_letters = int(input("How many letters do you want in your password?\n"))
quantity_symbols = int(input("How many symbols do you want in your password?\n"))
quantity_numbers = int(input("How many numbers do you want in your password?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

passwordList = []
for i in range(0, quantity_numbers):
    passwordList.append(choice(numbers))
for i in range(0, quantity_letters):
    passwordList.append(choice(letters))
for i in range(0, quantity_symbols):
    passwordList.append(choice(symbols))
password = ""
shuffle(passwordList)
for i in passwordList:
    password += i
print(password)



