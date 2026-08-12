number = [10,30,60]
try:
    index = int(input("enter a index value: "))
    print(number[index])
except IndexError:
    print("index value doesn't exist")
except ValueError:
    print("enter a valid number")