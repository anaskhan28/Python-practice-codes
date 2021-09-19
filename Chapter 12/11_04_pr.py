num = int(input("Enter the number that you want a multiplication table\n "))

table = [num*i for i in range(1, 11)]
print(table)
with open ("tables.txt", "a") as f:
    f.write(str(table))
    f.write("\n")
         