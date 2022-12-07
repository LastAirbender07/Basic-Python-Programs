""" Using Functions write a program to iterate a given string using for loop and while loop."""

def IterateString(s):
    print("\nIterating string using for loop: ")
    for i in s:
        print(i)
    
    print("\nIterating string using while loop: ")
    i = 0
    while i < len(s):
        print(s[i])
        i += 1

s = input("Enter a string: ")
IterateString(s)