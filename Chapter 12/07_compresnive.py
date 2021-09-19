a = [23,44, 5,5, 7, 2 ,4, 6 ,8, 10, 9, 12,]
# b= []
# for item in a: 
#     if item%2==0:
#         b.append(item)
# print(b)
    
b = [i for i in a if i>8]
print(b)
t = [1, 2, 3, 4, 1, 3 ,6 ,7,8,43,3]
print(t)
s = {i for i in t}
print(s)