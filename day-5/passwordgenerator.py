import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to password generator")
nr_letters=int(input("how many letters you want \n"))
nr_symbols=int(input("how many symbols you want \n"))
nr_numbers=int(input("how many numbers you want \n"))
password=[]
for char in range(1,nr_letters+1):
    c=random.choice(letters)
    password+=c

for char in range(1,nr_symbols+1):
    d=random.choice(symbols)
    password+=d

for char in range(1,nr_numbers+1):
    e=(random.choice(numbers))
    password+=e


random.shuffle(password)

realpassword=""
for char in password:
    realpassword+=char
print(f"your password is:{realpassword}")



