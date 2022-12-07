import cmath

def root(a, b, d):
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('root1 : ', sol1)
    print('root2 : ', sol2)

a = float(input('Enter the coefficient of x^2 : '))
b = float(input('Enter the coefficient of x : '))
c = float(input('Enter the constant value : '))

d = b**2 - 4*a*c

if d==0:
    print('The roots are real and equal')
    root(a, b, d)
elif d>0:
    print('The roots are real')
    root(a, b, d)
else:
    print('The roots are imaginary')
    root(a, b, d)