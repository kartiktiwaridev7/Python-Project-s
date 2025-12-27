class booking:
    def insert(x):
        f = open("book.txt","w")
        pname=str(input("enter the passenger name"))
        f.write(pname)
        f.close()
    def display(x):
        f= open("book.txt","r")
        print(f.read())
        f.close()

class cancelation(booking):
    def insert(x):
        f = open("cancel.txt","w")
        ticketno = str(input("enter the ticket no"))
        f.write(ticketno)
        f.close()
    def display(x):
        f = open("cancel.txt","r")
        print(f.read())
        f.close()

class tatkal(booking):

    def insert(x):
        f=open("tat.txt","r")
        print(f.read())
        f.close()

b = booking()
c = cancelation()
t = tatkal()

ans = int(input("do u want to count (1/0)"))
while(ans == 1):
    print("Indian railway Reservation")
    print("1 Booking")
    print("2 Cancellation")
    print("3 Tatkal")
    print("4 exit")
    x = int(input("select choice 1 to 4"))
    if(x == 1):
        print("Welcome To Booking dept!")
        print("1 Insert ")
        print("2 Dispaly")
        print("3 Exit")

        y = int(input("Select choice 1 to 3"))
        if(y ==1):
            b.insert()

        else:
            if(y == 2):
                b.display()
            else:
                print("exit from bookig menu")
    else:
        if(x == 2):
            c.insert()
            c.display()
        else:
            if(x==3):
                t.insert()
                t.display()
            else:
                print("exit")

ans = int(input("Do U want to count(1/0)"))
