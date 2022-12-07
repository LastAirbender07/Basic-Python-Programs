""" Write a program that finds sum of all even numbers in a list using function"""

def SumOfEvenNumbers(l):
    sum = 0
    for i in l:
        if i % 2 == 0:
            sum += i
    return sum

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of all even numbers in list is: ", SumOfEvenNumbers(l))