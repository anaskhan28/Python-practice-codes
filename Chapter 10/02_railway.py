class Employee:
    company = "Deloite"


anas = Employee()
Ahmed = Employee()
print(anas.company)
print(Ahmed.company)
Employee.company = "Youtube"
print(anas.company)