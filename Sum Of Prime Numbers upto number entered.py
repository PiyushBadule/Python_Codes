a=int(input())
l=[]
for num in range (2,a+1):
    for i in range (2,num):
        if num%i==0:
            break
    else:
        l.append(num)
print(sum(l))
print (l)