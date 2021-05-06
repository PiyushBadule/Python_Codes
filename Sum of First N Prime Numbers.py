# Program to Print Sum of First n Number of Prime Numbers
ab = int(input("Enter the number of Prime Numbers You Want:"))
c = 0
l = []
b = 1
while (c != ab):
    b += 1
    for x in range(2, b):
        if b % x == 0:
            break
    else:
        l.append(b)
        c += 1
print(sum(l))