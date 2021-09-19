try:
    i = int(input("Enter the number\n"))
    c = 1/i
except Exception as e:

    print(e)
    exit()
finally:
    print("You did atleast something")
print("Thanks for usning python programming")
