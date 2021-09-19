mydict = {
    "Fast": "In a cooler manner",
    "Anas": {'Cloud Architect': 'Data Scientist'},
    1: 2
}
# dictionary method
print(mydict.keys())  # print the keys of the dictionary
print(mydict.values())  # print the values of the dictionary
print(mydict.items())  # print the (values and keys) of all contents
something = {
    'clue': 'less'
}
(mydict.update(something))  # update the dictionary by adding key values of something
print(mydict)
print(mydict.get('Fast')) # returns the key value
print(mydict['Fast']) # returns the key value

# The difference between .get and [] is this
print(mydict.get('cooler')) # returns None of a cooler is not present in dictionary
print(mydict['cooler']) # throws an error of a cooler value is not present in the dictionary
