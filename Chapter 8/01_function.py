def percent(marks):
    p = ((marks[0] + marks1[1] + marks[2] + marks[3] + marks[4])/400)*100
    
    
    return p
marks1 = [34, 53, 88, 77, 90]
percentage1 = percent(marks1)

marks2 = [56, 66, 78, 87, 86]
percentage2 = percent(marks2)
print(percentage1, percentage2)