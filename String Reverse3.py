a2 = " I am Piyush"
# output:- Piyush am I
b2 = ''
for x in a2[::-1]:
    if x == " ":
        print(b2[::-1], end=" ")
        b2 = ""
    else:
        b2 = b2 + x
print(b2)
