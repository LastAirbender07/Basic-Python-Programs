"""Convert tuple of list to tuple Input : ( [10,50,60] , [40,65]) Output : (10,50,60,40,65"""

t1 = ([10,50,60] , [40,65])
t2 = tuple(t1[0] + t1[1])
print(t2)