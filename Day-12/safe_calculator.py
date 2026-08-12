try: 
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    result = num1 + num2 
    print(result)
except ValueError:
    print("enter a number")
except TypeError:
    print("can't add number and string")
except ZeroDivisionError:
    print("can't divided by 0")
