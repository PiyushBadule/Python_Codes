a = [8,2,6,5,1,-1,-2,-12]
b = 0
for x in range (0,len(a)):
    for y in range(x+1, len(a)):
        if(a[x] > a[y]):
            b = a[x]
            a[x] = a[y]
            a[y] = b
print(a)