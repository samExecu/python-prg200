#Dummy data
accounts_data = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        #Gets account name, number and balance
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Rs. {amount}. Your New balance is: Rs. {self.balance}")
        else:
            print("Invalid Deposit Amount!")

    def withdraw(self, amount):
        #Checking if withdrawal amount is greater than balance or not
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: Rs. {self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn: Rs. {amount}. New balance: Rs. {self.balance}")
        else:
            print("Invalid Withdrawal Amount!")

    def get_balance(self):
        #Display users name and balance
        print(f"{self.name}: Rs. {self.balance}")

accounts = {}
for name, account_num, balance in accounts_data:
    accounts[account_num] = BankAccount(name, account_num, balance)

print("\n=== Making Transactions ===")

#Deposit 3000 into A002
print("\nDepositing 3000 into A002:")
accounts["A002"].deposit(3000)

#Withdraw 15000 from A003 (should fail)
print("\nWithdrawing 15000 from A003 (should fail):")
accounts["A003"].withdraw(15000)

#Withdraw 2000 from A001
print("\nWithdrawing 2000 from A001:")
accounts["A001"].withdraw(2000)

#Displaying the final balance of all three accounts
print("\n=== Final Balances ===")
for account in accounts.values():
    account.get_balance()
