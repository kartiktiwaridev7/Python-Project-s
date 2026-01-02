# Creating Class 
# class car:
#    name = "karan"
#    Address  = "123"

#creating Object(instance)
# s1 = car()
# print(s1.name)

# s2 = car()
# print(s2.Address)

class Student:
    
    def __init__(self,fullname,Marks):
        self.name = fullname
        self.marks = Marks
        print("Adding new student in the database......")

s1 = Student("Karan" , 98)
print(s1.name,s1.marks)

s2  = Student("arjun",88)
print(s2.name,s2.marks)
