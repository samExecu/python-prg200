#creating a function for case validation
def passwordValidation(password):
  specialCharacter = "!@#$%^&*"
  #creating counters
  verified = 0
  upChar = 0
  lowChar = 0
  digit = 0
  specChar = 0

  #checking for all the cases through one loop, if case match then the incrementer goes up
  for i in password:
    if(i >= 'A' and i <= 'Z'): upChar += 1
    if(i >= 'a' and i <= 'z'): lowChar += 1
    if(i >= '0' and i <= '9'): digit += 1
    if i in specialCharacter: specChar += 1

  #printing out missing criterias if any, if not updating the verified variable by 1
  if len(password) < 8:
    print("Password needs to be at least 8 characters long")
  else:
    verified += 1

  if upChar < 1:
    print("Password must contain at least 1 uppercase letter")
  else:
    verified += 1

  if lowChar < 1:
    print("Password must contain at least 1 lowercase letter")
  else:
    verified += 1

  if digit < 1:
    print("Password must contain at least 1 digit")
  else:
    verified += 1

  if specChar < 1:
    print("Password must contain at least 1 special character from !@#$%^&*")
  else:
    verified += 1

  return verified

#list of weak passwords to compare
passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

password = input("Enter password: ")
validations = passwordValidation(password)

#checking if the password went through or not among all the checks
if(validations == 5):
  #checking if the password is weak or not
  weak = False
  for i in passwords:
    if(password == i):
      weak = True
      break
  print("Password Status: Weak Password!, try making a strong password") if (weak) else print("Password Status: Strong Password!")
else:
  print("Password Status: Weak Password")
  print("Criterias Not Fullfilled!, please try again")
