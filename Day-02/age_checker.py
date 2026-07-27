age = int(input("Enter your age:"))
print("Age Checker")
if age>=100 :
    print("Invalid age entered")
elif age>=18:
    print("eligible for vote")
elif age<=0:
    print("Invalid age entered")
else :
    print("not eligible")