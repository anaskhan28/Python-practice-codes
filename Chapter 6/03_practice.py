text = input("Enter the text\n")
if ("make a lot of money " in text):
    spam = True
elif("Click now " in text):
    spam = True
elif("Subscribe this channel " in text):
    spam = True
else:
    spam = False
if(spam):
       print("This text is a Spam")
        
