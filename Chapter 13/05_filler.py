# Filter Syntax: list(filter(function, list))
def num_greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


g10 = lambda num: num>5


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 132]
# print(list(filter(num_greater_than_5, l)))
print(list(filter(g10, l)))
