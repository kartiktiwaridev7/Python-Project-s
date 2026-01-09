time = int(input("Enter the number how many times you want to perform calculation \n"))
for i in range(time):
    print("Your Number of iteration is :" , i+1)
    a = int(input("Enter a number \n"))
    b = int(input("Enter b number \n"))
    menu = input("Enter the claculationa that you want to perform \n 1)sum \n 2) Minus \n 3) Multiplication \n 4)Division \n ")
    if(menu == "1"):
        sum = a+b
        print(sum)

    elif(menu == "2"):
        minus = a-b
        print(minus)

    elif(menu == "3"):
        multi = a*b
        print(multi)

    elif(menu == "4"):
        division = a/b
        print(division)

    

    else:
        print("You Enter the wrong number : ")