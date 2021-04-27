no=int(input("Enter Number:"))
p1=no%10;r=0
while(no!=0):
    p2=no%10
    no=no//10
    r=p1+p2
print("The Sun Is:",r)