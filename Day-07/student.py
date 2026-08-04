name = input("enter your name: ")
age = int(input("enter your age: "))
course = input("enter your course: ")
student = {
    "Name" : name,
    "Age" : age,
    "Course": course
    }
print("\nStudent Details")
for key,value in student.items():
    print(key ,":",value) 