# First enter the number you want to put in input list.
#Example: if you entered 5
# So now you want to enter 5 numbers separated with space like 12 11 45 6 1
def solution(L):
    # write your code here
    a = max(L)
    b = min(L)
    add = a + b
    return add


N = int(input())
L = []
n = 0
for e in input().split():
    if (n < N):
        L.append(int(e))
        n += 1
if (n < N):
    print("Please input {0} elements".format(N), end='')
else:
    print(solution(L), end='')