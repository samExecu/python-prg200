#Discount Calculator depending on Total Amount Spent
import sys

#checks what % discount is availabe for the user and returns the discounted amount
def discountChecker(currentAmount):
  if(currentAmount >= 1000 and currentAmount <= 4999 ):
    print("Applied 5% Discount")
    return currentAmount * 0.95
  elif(currentAmount >= 5000 and currentAmount <= 14999 ):
    print("Applied 10% Discount")
    return currentAmount * 0.9
  elif(currentAmount >= 15000 ):
    print("Applied 20% Discount")
    return currentAmount * 0.8
  else:
    print("No Discounts Availabe")
    return currentAmount

currentAmount = float(input("Whats your Current Total Amount: "))
#validating negative value first
if(currentAmount < 0.0):
    print("Invalid Amount!, please enter valid amount")
    sys.exit()

membership = int(input("Do you have a membership? (1: yes | 0: no): "))
#validating membership value
if not (membership == 1 or membership == 0):
    print("Invalid!, Enter either 1 or 0")
    sys.exit()

#checking if user has the memership or not
if (membership):
#if yes, applies loyalto discount, if no then continue
  discountedAmount = discountChecker(currentAmount)
  print("Applied 5% Loyalty Discount")
  payableAmount = discountedAmount * 0.95
else:
  payableAmount = discountChecker(currentAmount)

#printing the payable amount
print(f"Payble Amount after applying all discounts is Rs. {payableAmount}")
