# Write a program to print
# APQR
# ABQR
# ABCR
# ABCD
a="ABCD"
b="PQR"
for x in range (1,5):
    print(a[:x],end="")
    print(b[x-1:])
