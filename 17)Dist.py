# Calculate the distance between two points by importing math

from math import sqrt

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('Distance between two points is: ', distance)