a = int(input("Enter a value for n : "))

if(a>=0):
    if(a!=0):
        if(a%2 == 0):
            print(a,' is a even number')
        else:
            print(a,'is a odd number')
    else:
        print(a,' is a even number')
else:
    print("Error!! Enter a positive integer!!")