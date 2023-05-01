# must pass the correct number of arguments to a function

#### Arbitrary number of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



#### Default Arguments
# Python program to illustrate Default Arguments in Functions
# This function is used to welcome students to school
def welcome(fullname, msg = 'Welcome to School!!'):

# If the msg argument value is not provided, then the default value in the Function argument is considered
  print('Hey there', fullname + ', ' + msg)

welcome('Sam')   # 2nd argument value not passed; will use function default argument
welcome('Zack', 'How have you been?')


#### Python Keyword Arguments
def fruits(a, b, p):
  print('We have', a+ ',', b+ ' and', p+ ' at our store.')

fruits('apple', 'banana', 'pineapple')

# example using keywork arguments
# Arguments in order
fruits(a = 'apple', b = 'banana', p = 'pineapple')

# Arguments out of order
fruits(b = 'banana', p = 'pineapple', a = 'apple')

# 2 positional, 1 keyword argument
fruits('apple', b = 'banana', p = 'pineapple')

# keywork arguments must come after positional arguments


##############
# Return Statement
##############

def add(num1, num2):
  return num1 + num2


print(add(1, 2))

# code after function  return statement will not be executed

def add(num1, num2):
  return num1 + num2
  print( "Hello World" ) # code not executed
