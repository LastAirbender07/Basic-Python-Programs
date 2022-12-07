# 	Print the composite numbers in the range of 0-20 using function

def composite():
    for i in range(0,21):
        if i > 1:
            if (i % 2) == 0:
                print(i)

composite()