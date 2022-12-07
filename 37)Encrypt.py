""" Using Functions write a program that encrypts a message by adding a key value to every character. [Note : key vaue=3] hello -> khoor """

def Encrypt(s):
    string = ''
    for i in s:
        string += chr(ord(i)+3)
    print(s + " ----> " + string)

s = "hello"
Encrypt(s)