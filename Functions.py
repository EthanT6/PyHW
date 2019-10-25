#Functions

#Define a function
def func1():
    print ("I am a function")

#runs the function
func1()
#prints the function and returns its value with is the Python constant of "NONE" to string
print (func1())
#prints the function definition
print (func1)

#function that takes args
def func2(arg1,arg2):
    print(arg1, " ",arg2)

#function that returns a value
def cube(x):
    return x*x*x

func2(10,20)
print (func2(10,20))
print (cube(3))

#function with default value for an arg
def power(num,x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print (power(2))
print (power(2,3))
print (power(x=3,num=2))

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print (multi_add(10,4,5,10,4))  
