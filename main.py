print("REplit Login System")
print()

def login():
  while True:
    userName = input("Enter your username: ")
    password = input("Enter your password: ")
    if userName == "David123" and password == "cats":
      print("ACCESS GRANTED")
      exit()
  else:
    print("Login details incorrect")

login()



