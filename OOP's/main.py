# Creating Class 
# class car:
#    name = "karan"
#    Address  = "123"

#creating Object(instance)
# s1 = car()
# print(s1.name)

# s2 = car()
# print(s2.Address)

# class Student:
    
#     def __init__(self,fullname,Marks):
#         self.name = fullname
#         self.marks = Marks
#         print("Adding new student in the database......")

# s1 = Student("Karan" , 98)
# print(s1.name,s1.marks)

# s2  = Student("arjun",88)
# print(s2.name,s2.marks)

# class parent:
#     def __init__(self ,fullName ,Property):
#         self.name = fullName
#         self.property = Property
        
# s1 = parent()

# class father:
#     def __init__(self,Name,HowMuchAdd):
#         self.name = Name
#         self.property = HowMuchAdd

# s2 = father()

# class children:
#     def __init__(self,Name,Dream):
#         self.Name = Name
#         self.Dream = Dream

# s3 = children()

# class student:
#     def __init__(self , Name  , Age):
        
#         self.name = Name
#         self.age = Age

# s1 = student("Ayush",17)
# s2 = student("Yash",15)
# s3 = student("Simmy",12)


# print(s1.name,s1.age)
# print(s2.name,s2.age)
# print(s3.name,s3.age)


class Animal:
    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


d1 = Dog()
d1.speak()
d1.bark()
