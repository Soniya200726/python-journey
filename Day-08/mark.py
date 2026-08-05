def average(mark1,mark2,mark3):
    avg = (mark1+mark2+mark3)/3
    return avg
m1 = int(input("enter mark1: "))
m2 = int(input("enter mark2: "))
m3 = int(input("enter mark3: "))
result = average(m1,m2,m3)
print("Average= ",result) 