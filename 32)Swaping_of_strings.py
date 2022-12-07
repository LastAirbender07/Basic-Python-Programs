""" Write a program to swap two strings using function"""

def SwapStrings(s1, s2):
    temp = s1
    s1 = s2
    s2 = temp
    return s1, s2

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Strings after swapping are: ", SwapStrings(s1, s2))