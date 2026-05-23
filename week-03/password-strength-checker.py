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
  print("Password needs to be atleast 8 character long") if (len(password) < 8) else verified += 1
  print("Password must contain atleast 1 uppercase letter") if (upChar < 1) else verified += 1
  print("Password must contain atleast 1 lowercase letter") if (lowChar < 1) else verified += 1
  print("Password must contain atleast 1 digit") if (digit < 1) else verified += 1
  print("Password must contain atleast 1 special character from !@#$%^&*") if (specChar < 1) else verified += 1

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
