def hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//hcf(x,y)
   return lcm

num1 = int(input('Enter value 1 : '))
num2 = int(input('Enter value 2 : '))
print("The L.C.M. is", lcm(num1, num2))