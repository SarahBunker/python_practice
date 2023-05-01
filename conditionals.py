a = "10"
b = "10"

if a < b:
  print(f"{a} is less then {b}")
elif b < a:
  print(f"{b} is less then {a}")
else:
  print(f"{a} equals {b}")

c = True

if c:
  print("C was true")

"""
Other symbols

>=
<=
!=
==

and
or

"""

boy = True
short = True

if boy and short:
  print("He is a boy and he is short")

num = 4.2

if num % 2 == 0:
  print("Number is even")
elif num % 2 == 1:
  print("Number is odd")
else:
  print("Number is niether")