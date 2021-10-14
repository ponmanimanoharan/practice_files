def say_hello(x):
    print("Hello World," + x)

say_hello("Ponmani!")
print("------------------------------")
y = say_hello("Caleb")
print(y)

def multiply_by_three(num):
    return num * 3

print(multiply_by_three(3))

def multiply(num1, num2):
    return num1 * num2

print(multiply(4,5))

def hello_world_enterprise_edition(username, greeting_pharse = "Hello "):
    return greeting_pharse + username

print(hello_world_enterprise_edition("peter"))
print(hello_world_enterprise_edition("peter", "good morning "))

def sum_numbers(*args):
    print(sum(args))
# args is immutable because
# it repersents the set of parameters which will be combined into a tuple.
# it can be used as aby other datatype


""""
kwargs: uses a dictionary 
args: collect arguments into a tuple 

"""
sum_numbers(1,2,3,4)

#notion of the variable local and global variable
# function call - all the variables of a function belongs to a function
# fucntion have movable and reusable objects which belong to itself thus does not interfere with other issues

dummy_variable_declared_outside = 8

def my_func():
    dummy_variable = 5
    return dummy_variable

print(dummy_variable_declared_outside)

dummy_variable  =10

print(dummy_variable)

def my_function():
    global dummy_variable
    dummy_variable = 5
    print(dummy_variable)

my_function()

def s_n(**kwargs):
    print(type(kwargs))
    print(kwargs)

s_n(name = "Mehran", id = 2001)
"""
KWARGS - converts the inputs into a collection of key value pairs(dictionary)

"""
def return_multiple_things():
    return(1,2,"ponmani")

num1, num2, num3 = return_multiple_things()
print(num1, num2, num3)