# output:- I ma hsuyiP
a = "I am Piyush"
b = ''
for x in a:
    if x == " ":
        print(b[::-1], end=" ")
        b = ""
    else:
        b = b + x
print(b[::-1])
