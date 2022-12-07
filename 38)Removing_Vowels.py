""" Using Functions 13.	Write a program that accepts a string from user and redisplays the string after removing vowels 
    from it using function. [Note : string is “ The food is very tasty”] """

def Remove_Vowels(s):
    string = ''
    for i in s:
        if i not in 'aeiou':
            string += i
    print(string)

s = "The food is very tasty"
Remove_Vowels(s)