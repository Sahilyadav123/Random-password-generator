
import random
print("Welcome to the PyPassword generator !")
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols=["!","@","#","$","%","&","*"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
no_letters=int(input("How many letters would you like in your password?\n"))
value1=""
for i in range(0,no_letters):
    i=letters[random.randint(0,len(letters)-1)]
    value1=value1+i
# print(value1)

value2=""
no_symbol=int(input("How many symbols would you like in your password?\n"))
for i in range(0,no_symbol):
    i=symbols[random.randint(0,len(symbols)-1)]
    value2=value2+i
# print(value2)
no_numbers=int(input("How many numbers would you like in your password?\n"))

value3=""
for i in range(0,no_letters):
    i=numbers[random.randint(0,len(numbers)-1)]
    value3=value3+i
# print(value3)

# this is a less secured password as it presents the password in the order in which they details are placed.
# print(value1+value2+value3)


list=[value1,value2,value3]
# password=list[random.randint(0,2)]

#check the list which is being printed
# print(list)
random.shuffle(list)

#the list got shuffled this means the indexing got changed randomely
# print(list)
# print(value1+value2+value3
password=""
for i in list:
    # print(i)
    password=i+password
print(password)
