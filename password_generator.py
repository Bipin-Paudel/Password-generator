import random
import string
alphabet = list(string.ascii_lowercase +string.ascii_uppercase )  
number=list( range(0,10))
symbol=['!','@','#','$','%','&','*']

e_alphabet=int(input("Enter number of alphabets you want in password:"))
e_number=int(input("Enter number of numbers you want in password:"))
e_symbol=int(input("Enter number of symbols you want in password:"))

password=[]

for char in range(0,e_alphabet):
    password.append(random.choice(alphabet))

for char in range(0,e_number):
    password.append(random.choice(number))

for char in range(0,e_symbol):
    password.append(random.choice(symbol))


random.shuffle(password)

for i in password:
    print(i,end='')


 