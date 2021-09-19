mydict = {
    "Gulaab" : "Rose",
    "Waqt" : "Time",
    "Madat" : "Help",
    "Shukriya" : "Thank You"
}
print("Options are", mydict.keys())
a = input("Enter your Hindi word\n")
print("The meaning of your hindi word is :",mydict.get(a))