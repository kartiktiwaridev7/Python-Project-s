class abc:
    def india(x):
        age = int(input("enter your age"))
        print('age = ' , age)

class xyz(abc):
    def pak(x):
        salary = int(input('Enter Salary '))
        print("salary = " ,salary)

class pqr (abc):
    def usa(x):
        qty = int(input("Enter your qty"))
        print("qty=",qty)
class mnc(xyz,pqr):
    def uk(x):
        name = str(input("Enter Your name "))
        print("Name =" , name)
        

m =mnc()
print("Enter Your choice")
print("1 india")
print("2 pak")
print("3 USA")
print("4 UK")
print("5 Exist")
b = int(input("Select 1 to 5 : "))
if(b== 1):
      m.india()
else:
    if(b==2):
        m.pak()
        m.india()
    else:
        if(b == 3):
            m.usa()
            m.india()
        else:
            if(b==4):
                m.uk()
                m.india()
                m.pak()
                m.usa()
            else:
                print("exist")
