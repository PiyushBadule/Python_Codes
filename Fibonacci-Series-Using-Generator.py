# Program to print Upto 10 Fabonacci Series
def fib():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f + s


for x in fib():
    if x > 10:
        break
    print(x, end=" ")
