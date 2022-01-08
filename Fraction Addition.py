# Take input as 2 different Array and add them and as a fraction
# Input: a = [2, 3]
#        b = [1, 2]
# Output: [7, 6]

# Input: a = [0, 3]
#        b = [0, 2]
# Output: [0, 0]

# Input: a = [1, 0]
#        b = [3, 2]
# Output: [3, 2]
# Hint: {2/3 +1/2}
# Note Handle Zero Condition as well

a = [2, 3]
b = [1, 2]
if(a[1] == b[1]):
    Fraction = a[0] + b[0]
    print([Fraction, a[1]])
elif 0 in a and 0 in b:
    print([0,0])
elif 0 in a:
    print(b)
elif 0 in b:
    print(a)
else:
    Fraction = (a[0] * b[1]) + (a[1] * b[0])
    print([Fraction, (a[1] * b[1])])