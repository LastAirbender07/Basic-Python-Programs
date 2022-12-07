# Write a python script to merge two dictionaries

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d3 = {}
for i in (d1, d2):
    d3.update(i)
print(d3)