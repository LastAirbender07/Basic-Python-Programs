mm = int(input('Enter month : '))
yy = int(input('Enter Year : '))
  
month ={1:'January', 2:'February', 3:'March', 
        4:'April', 5:'May', 6:'June', 7:'July',
        8:'August', 9:'September', 10:'October',
        11:'November', 12:'December'}
   
day =(yy-1)% 400
day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
day = day % 7
  
nly =[31, 28, 31, 30, 31, 30, 
      31, 31, 30, 31, 30, 31]
ly =[31, 29, 31, 30, 31, 30, 
     31, 31, 30, 31, 30, 31]
s = 0
  
if yy % 4 == 0:
    for i in range(mm-1):
        s+= ly[i]
else:
    for i in range(mm-1):
        s+= nly[i]
  
day += s % 7
day = day % 7
   
space =''
space = space.rjust(2, ' ')
  

print(month[mm], yy)
print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
  
if mm == 9 or mm == 4 or mm == 6 or mm == 11: 
    for i in range(31 + day):
          
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()
elif mm == 2:
    if yy % 4 == 0:
        p = 30
    else:
        p = 29
          
    for i in range(p + day):
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print() 
else:
    for i in range(32 + day):
          
        if i<= day:
            print(space, end =' ')
        else:
            print("{:02d}".format(i-day), end =' ')
            if (i + 1)% 7 == 0:
                print()