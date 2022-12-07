def area(a, b, c) :
    s = (a + b + c)//2
    area = (s*(s-a)*(s-b)*(s-c))**(0.5)
    return area

x = float(input('Enter side1 of the triangle : '))
y = float(input('Enter side2 of the triangle : '))
z = float(input('Enter side3 of the triangle : '))

area_of_triangle = area(x, y, z)
print('Area of the given triangle is : %0.2f' %area_of_triangle)