def area(a, b) :
    area = (0.5)*a*b
    return area

x = float(input('Enter Base of the Right Angled Triangle : '))
y = float(input('Enter Height of the Right Angled Triangle : '))

area_of_triangle = area(x, y)
print('Area of the given triangle is : %0.2f' %area_of_triangle)