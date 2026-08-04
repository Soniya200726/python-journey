marks = []
for i in range(3):
    mark = int(input(f"enter mark {i+1} ="))
    marks.append(mark) 
print(f"highest mark:{max(marks)}")
print(f"lowest mark:{min(marks)}")
print(f"total mark:{sum(marks)}")
print(f"average :{sum(marks)/len(marks)} ") 