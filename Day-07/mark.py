maths = int(input("enter your maths mark: "))
science = int(input("enter your science mark: "))
social = int(input("enter your social mark; "))
marks = {
    "Maths" : maths,
    "Science" : science,
    "Social" : social
    }
print("\nMark List")
for key,value in marks.items():
    print(key ,":" ,value)
print("sum: ",sum(marks.values()))
print("average: ",sum(marks.values())/len(marks)) 