""" Write a program that creates a list [ ‘a’ , ‘b’ , ‘c’] then create a tuple from that list. Now do the opposite. 
    That is create the tuple ( ‘a’,’b’,’c’) and then create a list from it."""

def ListToTuple():
     l = ['a', 'b', 'c']
     t = tuple(l)
     print("Tuple from list: ", t)

def TupleToList():
     t = ('a', 'b', 'c')
     l = list(t)
     print("List from tuple: ", l)

ListToTuple()
TupleToList()
