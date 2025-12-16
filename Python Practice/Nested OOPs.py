class saving:
    def sac(x):
        amount = int(input("Enter Saving A/C"))
        if (amount>= 1000):
            print("Saving A/C Open")
        else:
            print("Sorry for current A/C")


class current(saving):
    def cur(x):
        amount = int(input("Enter current account amount"))
        if(amount>=5000):
            print("Current A/C Open")

        else:
            print("Sorry for C.A/C ")

class personal:
    def pers(x):
        salary = int(input("Enter Your Salary"))
        if(Salary >= 5000):
            loan = salary*5
            print("loan = " , loan)
        else:
            print("Sorry for P.Loan")

class education(personal):
    def edu(x):
        per = int(input("Enter Education Percentage"))
        if(per >= 70):
            req = int(input("Enter loan requirement"))
            loan = req*per/100
            print("loan = ",loan)
        else:
            print("Sorry for Personal loan")

c = current()
e = education()
print("Online Banking")
print("1 A/C Department")
print("2 loan department")
print("3 Exist")

x = int(input("Select 1 to 3"))
if(x== 1):
    print("Welcome to A/c Department")
    print("1 saving A/c")
    print("2 Current A/C")
    print("3 Exist")
    y = int(input("Saving 1 to 3"))
    if(y == 1):
        c.saving()
else:
    if(x == 2):
        print("loan menu")
        print("1 personal loan")
        print("2 Education loan")
        print("3 Exist")

        z = int(input("Select 1 to 3"))
        if( z == 1):
            e.per()
        
        else:
            if(z == 2):
            
                e.edu()
            else:
                
                print("Exist")

    else:
        print("Exist")
            

           
        
