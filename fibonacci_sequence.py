# Simple Fibonacci Sequence
a = int(input("Enter Number:"))
count = 1
F = 0
S = 1
while count <= a:
    print(F, end=',')
    Final = F + S
    F = S
    S = Final
    count += 1

print()


print("******************************************************************************************")

def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


for i in range(10):
    print(fib(i), end=',')
