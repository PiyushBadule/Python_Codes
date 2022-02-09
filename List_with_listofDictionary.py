# Convert list of dict to dict [[{},{}],[{},{}]]
# input: [[{'name': "piyush", "rank": 10}, {"name": "rahul", "rank": 20}],
#      [{"rank": 10, "class": 1}, {"rank": 20, "class": 3}]]
# output: [{'name': 'piyush', 'rank': 10, 'class': 1}, {'name': 'rahul', 'rank': 20, 'class': 3}]
a = [[{'name': "piyush", "rank": 10}, {"name": "rahul", "rank": 20}],
     [{"rank": 10, "class": 1}, {"rank": 20, "class": 3}]]
b = []
c = len(a)-1
for i in a[0]:
    for j in a[c]:
        if i.get("rank") == j.get("rank"):
            i.update({'class': j.get("class")})
            b.append(i)
print(b)