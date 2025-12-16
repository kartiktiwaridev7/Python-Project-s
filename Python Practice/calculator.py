import addition as ad
import sub as s
import division as d
import multiplication as m

print("Calculator")
print("1 Add")
print(" 2 Sub")
print("3 Division")
print(" 4 Multiplication")
print("5 Exist")

x = int(input("Enter 1 to 5"))

if(x == 1):
    ad.addition()
else:
    if(x==2):
        s.sub()
    else:
         if(x==3):
             d.division()
         else:
             if(x == 4):
                 m.multiplication()
             else:
                 print("Exist")
                 

      
