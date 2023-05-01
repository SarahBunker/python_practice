'''
can catch a specific error by name

the else statement will execute if nothing went wrong
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