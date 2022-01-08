# Check If given String is Anagram or not
a = 'listen silent'
li = list(a.split(" "))
print('Anagram' if sorted(li[0]) == sorted(li[1]) else 'Not Anagram')