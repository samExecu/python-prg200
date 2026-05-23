#ATM Withdrawl Validator
import sys

#getting users account balance and daily_withdrawn amount (if any)
currentBalance = int(input("Enter your current account balance: "))
dailyWithdrawn = int(input("Amount of money you have withdrawn today: "))

#configuring negative value validation
if(currentBalance < 0 or dailyWithdrawn < 0):
  print("Invalid Balance or Daily Withdrawl Amount!")
  sys.exit()

#comparing users daily_withdrawl with amount of withdrawl you can do in a day
if(dailyWithdrawn >= 50000):
  #if yes, throw an error and exit the program, if no then continue
  print("Daily withdrawl limit reached, try again tomorrow")
  sys.exit()

#providing note so that user knows that the withdrawl amount should be a multiple of 500
print("Note: Amount Must be Multiple of 500")
#getting withdrawl amount frW the user
withdrawlAmount = int(input("Amount of money you want to withdraw: "))

#checking if the value entered by the user is valid or not
if((withdrawlAmount % 500) != 0 or withdrawlAmount < 0):
  #if yes, throw an error and exit the program, if no then continue
  print("Invalid Withdrawl Amount!, Must be a multiple of 500.")
  sys.exit()

#comparing users current balance with the amount they want to withdraw
if(withdrawlAmount > currentBalance):
  #if yes, throw an error and exit the program, if no then continue
  print("Insufficient Balance!, Withdrawl amount more than current balance.")
  sys.exit()

#if all the cases pass, then show withdrawl successfull and display users updated balance
print(f"Rs. {withdrawlAmount} has successfully been withdrawn.")
print(f"Your new balance is Rs. {currentBalance - withdrawlAmount}")
