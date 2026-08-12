try:
    num = int(input("enter a number: "))
except:
    print("enter valid nummber")
else:
    print("you enterd ",num)
finally:
    print("success") 