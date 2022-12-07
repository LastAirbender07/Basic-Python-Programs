""" Using functions make a list of first ten letters of the alphabet, then using the slice operation do the following operations 
    a)	Print the first three letters from the list 
    b)	Print any three letters from the middle 
    c)	Print the letters from any particular index to the end of list."""

def First3Letters():
    print("First three letters from the list are: ", alphabet[:3])

def MiddleLetters():
    print("Any three letters from the middle are: ", alphabet[3:6])

def IndexLetters(n):
    print("Letters from any particular index to the end of list are: ", alphabet[n:])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
First3Letters()
MiddleLetters()
IndexLetters(5)