def great(x, y, z):
    if x == y == z:
        print("All are equal.")

    elif x >= y and x >= z:
        print("X is greatest:", x)

    elif y >= x and y >= z:
        print("Y is greatest:", y)

    else:
        print("Z is greatest:", z)

x = int(input("Enter the x value "))
y =int(input("Enter the y value "))
z = int(input("Enter the z value"))

great(x,y,z)
