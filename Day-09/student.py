student = set()
for i in range(5):
    name = input(f"enter your name{i+1}: ") 
    student.add(name)
print("\nunique student name")
print(student)
print("length of student: ",len(student))
print("order of name: ",sorted(student))