"""program for 'tomato' 'to' Given string s1 and s2 , count the occurrence of string s2 in s1"""

s1 = 'tomato'
s2 = 'to'
count = 0
for i in range(len(s1)):
    if s1[i:i+len(s2)] == s2:
        count += 1
print('The number of occurrences of substring in string is: ', count)