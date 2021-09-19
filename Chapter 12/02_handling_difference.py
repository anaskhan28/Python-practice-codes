try:
    a = int(input("Enter the number\n"))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value")

except ZeroDivisionError as e:
    print("Maybe you enter a zero which is not divisible by any number")
    
print("Thanks for usning the code!")