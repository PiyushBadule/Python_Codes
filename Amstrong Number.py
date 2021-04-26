a = 153
a = str(a);res=0
for x in a:
    z=int(x)
    res1=z**3
    res=res+res1
print(res)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

n = int(input("Enter The Number:"))
a = list(map(int,str(n)))
b = list(map(lambda x:x**3,a))
if(sum(b)==n):
    print(n,"Is Armstrong Number")
else:
    print(n,"Is Not Armstrong Number")