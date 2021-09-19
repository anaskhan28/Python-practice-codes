class Employee:
    company = "Deloite"
    salary = 100


anas = Employee()
Ahmed = Employee()

# creating attribute salary for both instances
# anas.salary = 150
Ahmed.salary = "200 $"
print(type(Ahmed.salary))
print(anas.company)
print(Ahmed.company)
print(anas.salary)
print(Ahmed.salary)
# Below line throw an error as adress in not defined in class\object
# print(salary.salam)