""" Using Functions write a program that prints the maximum and minimum value in a dictionary."""

def Max_Min_Dict(d):
    
    print("Maximum value in dictionary: ", max(d.values()))
    print("Minimum value in dictionary: ", min(d.values()))

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
Max_Min_Dict(d)