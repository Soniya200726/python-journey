class Student:
    def __init__(self,name,age,department):
        self.name = name
        self.age = age
        self.department = department

name = input("enter your name: ")
age = int(input("enter your age: "))
department = input("enter your department: ")

student1 = Student(name, age, department)

print("Name: ",student1.name)
print("Age: ",student1.age) 
print("Department: ",student1.department) 
