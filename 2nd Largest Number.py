# Question: Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.
# Find the second Largest number from an given integer array
# Input:5
# 2 3 6 6 5
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
B = arr.count(max(arr))
print("B",B)
if(B == 1):
    print(f'runnerup is {int(arr[-2])}')
else:
    print(f'runnerup is {int(arr[-1-B])}')