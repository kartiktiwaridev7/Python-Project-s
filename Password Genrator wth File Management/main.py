import random

char = "123456789!@#$%^&*()ABCDEGHIJKLMNOPQRSTUVWXYZ"

num = int(input("Please enter the length of password\n :"))

passw = ""

for i in range(num):
    passw += random.choice(char)

# print(passw)

with open("mydata.txt", "w") as file:
    file.write(passw)

with open("mydata.txt", "r") as file:
    print(file.read())