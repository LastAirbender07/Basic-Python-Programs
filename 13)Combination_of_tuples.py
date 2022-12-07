""" Given two tuples t1=(11,3), t2=(15,70) . Find all the pair of combinations of tuple. 
    Output: (11,15),(11,70), (3,15),(3,70),(15,11),(15,3),(70,11),(70,3)"""

t1 = (11,3)
t2 = (15,70)
for i in t1:
    for j in t2:
        print((i,j), end = ',')
print()
for i in t2:
    for j in t1:
        print((i,j), end = ',')
print()