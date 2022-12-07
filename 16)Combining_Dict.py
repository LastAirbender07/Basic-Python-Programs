"""	Combine two dictionaries adding values for common keys. Input: D1={ ‘a’:100 , ‘b’:200 , ‘c’:300 , ‘d’:400 } 
    D2 = { ‘a’:50 , ‘b’:20 , ‘c’ : 100 } Output : {‘a’:150 , ‘b’:220 ,’c’:400 , ‘d’:400 } """

from collections import Counter 

d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
d2 = {'a': 50, 'b': 20, 'c': 100}
d3 = Counter(d1) + Counter(d2)
print(d3)