print("-------Hotel Management System-----------")

class main:
    hotel = "City Hotel"   # Class Variable
    def __init__(self,  Manager):
        self.Manager = Manager
        pass

class Staff:
    def __init__(self , Staff_Name):
        self.Staff_Name = Staff_Name  # Instance Variable 
        pass

class Customer:
    def __init__(self , Name ):
        self.Name = Name
        self.order =  []
    print("=========Welcome To Our City Hotel Sir===============")
    
    def show_menu(self):
        print("===============Food Menu==============")
        print("1.Coffe 5$")
        print("2.Tea 2$")
        print("3.Burger 4$")
        print("4.Sandwich 4$")
        print("5.Water 1$")

    def take_order(self):
        choice = int(input("Enter food choice (1-5): "))
        if choice == 1:
            self.order.append(("Coffe", 5))
        elif choice == 2:
            self.order.append(("Tea", 2))
        elif choice == 3:
            self.order.append(("Burger", 2))    
        elif choice == 4:
            self.order.append(("Sandwich", 4))
        
        elif choice == 5:
            self.order.append(("Water", 1))
        else:
            print("Invalid choice")

    def bill(self):
        total = 0
        print("---- Your Bill ----")
        for item, price in self.order:
            print(item, "₹", price)
            total += price
        print("Total Amount: $", total)
  
print("Please Select One -------\n 1) Manager \n 2) Staff \n 3) Customer \n 4) Exit")

menu = int((input("Enter Your Choice 1, 2, 3 , 4 \n")))

if(menu == 1):
    s1 = main(input("Enter Your Name-----\n"))
    print("Name Of the Manager in the Hotel City is ", s1.Manager)

elif(menu == 2):
    s2 = Staff(input("Enter Your Name-----\n"))
    print("Name Of the Staff in the Hotel City is", s2.Staff_Name)

elif menu == 3:
    cname = input("Enter Customer Name: ")
    c1 = Customer(cname)

    print("Welcome", c1.Name)
    c1.show_menu()
    c1.take_order()
    c1.bill()

else:
    print("Thanks For visiting sir I hope we will meet again 😊 ")
