# Write a function which takes a list as a argument and double the each from that list.
# output:- ["aa", "bb", "cc"]

input = ["a", "b", "c"]
a = []
def fun(input):
    for x in input:
        a.append(x*2)
    return a
print(fun(input))