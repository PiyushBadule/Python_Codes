# Question: Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.
# Find the second Largest number from an given integer array
# Input:5
# 2 3 6 6 5
n = int(input())
arr = map(int, input().split())
A = list(arr)
A.sort()
B = A.count(max(A))
if(B == 1):
    print(f'runnerup is {int(A[-2])}')
else:
    print(f'runnerup is {int(A[-1-B])}')