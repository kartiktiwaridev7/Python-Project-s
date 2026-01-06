# file = open("data.txt","w")
# file.write("Kartik")
# file.close()

# file = open("data.txt","r")
# print(file.read())
# file.close()

with open("mydata.txt","a") as file:
    file.append("yash")
    file.append(15)


file = open("mydata.txt","r")
print(file.read())
file.close()