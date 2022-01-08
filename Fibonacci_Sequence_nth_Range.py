nterms = int(input("Enter The Range Of Sequence:"))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("Please enter positive integer")
elif nterms == 1:
    print("Fibonacci squence upto", nterms, "is:")
    print(n1)
else:
    print("Fibonacci squence upto", nterms, "is:")
    while n1 <= nterms:
        print(n1, end=",")
        nth = n1 + n2
        n1 = n2
        n2 = nth