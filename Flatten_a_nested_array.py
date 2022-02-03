# Input:- [1,2,[3],[[4]],[[[5]]]].
# Output:- [1, 2, 3, 4, 5]

def flatten(list_of_lists):
    print("def:- ", list_of_lists)
    if len(list_of_lists) == 0:
        print("First if:-", list_of_lists)
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        print("Second if", list_of_lists)
        print("Second if Return", (list_of_lists[0])+ list_of_lists[1:])
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    print("Last Return:-", list_of_lists[:1]
          + list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


print(flatten([1, 2, [3], [[4]], [[[5]]]]))

