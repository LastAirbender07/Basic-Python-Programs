""" Using Functions Write the command to print “hello world” as “Hello Friends”. """

def CapRep(s):
    string = s.capitalize()
    print(string.replace("world", "Friends"))

s = "hello world"
CapRep(s)