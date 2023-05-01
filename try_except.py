'''
can catch a specific error by name

the else statement will execute if nothing went wrong
the finally statement will execute wether or not an exception was raised
'''


try:
  x = int(input("Input an integer: "))
  print(x)
except ValueError:
  print("Value is not an integer")
except:
  print("Something went wrong, try again")
else:
  print("Nothing went wrong")
finally:
  print("try, except, finished")