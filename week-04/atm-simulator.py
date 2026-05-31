#dummy data
accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500, "pin": "5678"},
    "A003": {"name": "Bikash Rai", "balance": 22000, "pin": "9012"}
}

def atm(account_id, pin, action, amount=0):
  #see if the account exists or not, if not then exit the code
  if account_id not in accounts:
    print("Account not found")
    return

  #checks the pin, if incorrect then exit the code
  if accounts[account_id]["pin"] != pin:
    print("Incorrect PIN")
    return

  #if both the above conditions pass then go throuh the action
  if action == "balance":

    #display the account holder"s name and balance
    print(f"{accounts[account_id]["name"]} | Balance: NPR {accounts[account_id]["balance"]}")

  elif action == "deposit":

    #add the given amount to the account balance
    accounts[account_id]["balance"] += amount
    print(f"Deposit successful. New balance: NPR {accounts[account_id]["balance"]}")

  elif action == "withdraw":

    #Check if enough balance exists
    if accounts[account_id]["balance"] >= amount:
      accounts[account_id]["balance"] -= amount
      print(f"Withdrawal successful. New balance: NPR {accounts[account_id]["balance"]}")
    else:
      print("Insufficient funds")

  else:
    #If action is not recognized
    print("Invalid action")


# Test calls
atm("A001", "1234", "balance")
atm("A002", "0000", "withdraw", 2000)
atm("A002", "5678", "deposit", 3000)
atm("A003", "9012", "withdraw", 25000)
atm("A004", "1111", "balance")
