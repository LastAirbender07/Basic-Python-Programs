a = int(input('Enter a number : '))
b = a
sum = 0

while(b > 0):
    rem = b % 10
    sum = sum + rem
    b = b //10

print('sum of the dights is : ', sum )
