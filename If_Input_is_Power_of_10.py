#Returns true if x is a power - of - 10.
# Otherwise returns false.
# INPUT:
# Input1: 3
# Output1: false
# Input1: 10
# Output1: true


import math
a = int(input())
b = 10
x = math.log(a, b)
y = round(x)
if (b ** y) == a:
    print(True)
else:
    print(False)