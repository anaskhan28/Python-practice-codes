def largest(num1, num2, num3):
    # if(num1 > num2):
    if(num1 > num3):
        return num1
    else:
     return num3
    if(num2>num3):
        return num2
    else:
       return num3

    
m = largest(56, 77, 55)
print( "The vlaue of largest number is " + str(m))
