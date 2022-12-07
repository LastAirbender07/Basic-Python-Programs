#	Calculate square root of a number. Demonstrate use of import, break and continue statements

import math

while True:
    num = input('Enter a number: ')
    if num.isnumeric():
        num = int(num)
        print('Square root of', num, 'is', math.sqrt(num))
        break
    else :
        print('Please enter a valid number')
        continue