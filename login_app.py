username = input("Enter username: ")
password = input("Enter password: ")

print(f"Account creation for {username} was successful")
print("Login now!")

username2 = input("Enter username: ")
password2 = input("Enter password: ")

if username == username2 and password == password2:
  print("Logged in Successfully")
else:
  print("Incorrect credentials")