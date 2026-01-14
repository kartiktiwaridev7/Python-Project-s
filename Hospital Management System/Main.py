print("=========Hospital Management Sysytem===========")
menu = input("What do You want 1) Transport Sysytem\n 2) Doctor \n 3) Want to by Medicine\n 4) Pay the Bill \n ")

if(menu == "1"):
    Name = input("Enter The Passenger Name\n")
    ID = input("Enter the Passenge Name \n")
    Address = input("Enter The Passenge Addrees\n")
    root = input("Please select the root\n")
    print("Thanks for using our services\nWe Are Available for 24/7 😊")

elif(menu == "2"):
    Disease = input("Please enter the Disease \n")
    Experince = input("Please tell us How Much Experinced Dotor do you Want \n But the Fee also Increases \n")

elif(menu == "3"):
    Medicine = input(" What medicine do you want to by \n")
    Amount = input("Please enter the amount of the medicine ")
    print("Please first take the medicine slip and pay the {Amount} then go and take your medicine \n from the store😊 ")

elif(menu == "4"):
    bill = input("Enter the what is this bill for \n ")
    type = input(" Enter the method of payment 1) Cash 2) UPI ")
    Amount = input("Please Enter the amount do you want to pay \n")
    print("Thanks for the payement Sir\Mam")

else:
    print("You Choose Somthing wrong \n Please try Again 😒(●'◡'●)")
