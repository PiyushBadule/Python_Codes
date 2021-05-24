string=input("Enter the string:")
newstring =''
for a in string:
    if (a.isupper()) == True:
        newstring += (a.lower())
    elif (a.islower()) == True:
        newstring += (a.upper())
    elif (a.isspace()) == True:
        newstring += a
print(newstring)