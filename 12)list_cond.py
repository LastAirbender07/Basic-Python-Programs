""" Create a list with 21,120,100,105,200,220,250 
    a)	In a list if the values are greater than 100 then apply break statement and print the values in the list. 
    b)	If the values are greater than 200 apply continue statement and print the values in list. """

l = [21,120,100,105,200,220,250]
print('---- Values are greater than 100 ----\n')
for i in l:
    if i > 100:
        break
    print(i)
print('\n---- Values are greater than 200 ----\n')
for i in l:
    if i > 200:
        continue
    print(i)