#Python Variables

#Declare Variable and initialize it
f=0
print(f)

#Re-declare the variable
f="abc"
print(f)

#ERROR : Variables of different types cannot be combined
#WRONG : print("this is a string" + 123)
print("this is a string" + str(123))

#Global vs Local variables in functions
def aFunction():
    global f
    f="def"
    print(f)

aFunction()
print(f)

#Delete a variable
del f
print(f)