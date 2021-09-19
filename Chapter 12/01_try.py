while(True):
    print("Press q to Quit the match")
    a = input("Enter the number\n")
    if a == 'q':
     break
    try:
        print("Trying.....")
        a = int(a)
        if a > 6:
            print("Your number is greater than 6")
    except Exception as e:
     print(f"The value should be number: {e}")
     
print("Thanks for playing")
