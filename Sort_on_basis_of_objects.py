# Sort it first on the basis of age then on the basis of salary.
import pandas as pd

a = [{'name': 'a', 'salary': 20000, 'age': 25},
     {'name': 'b', 'salary': 25000, 'age': 23},
     {'name': 'c', 'salary': 34000, 'age': 25},
     {'name': 'd', 'salary': 13000, 'age': 30}]

df1 = pd.DataFrame(a)
print(df1.sort_values(by='age'))
print(df1.sort_values(by='salary'))