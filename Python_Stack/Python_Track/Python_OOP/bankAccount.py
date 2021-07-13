class BankAccount:
	def __init__(self, int_rate=0, balance=0):
		self.int_rate=int_rate
		self.balance=balance
	def deposit(self, amount=0):
		# increases the account balance by the given amount
		self.balance+=amount
	def withdraw(self, amount=0):
		# decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
		if self.balance<amount:
			print("Insufficient Funds: Charging a $5 fee")
			self.balance-=5
		else:
			self.balance-=amount
		
	def display_account_info(self):
		# print to the console: eg. "Balance: $100"
		print("Balance: ", self.balance)
	def yield_interest(self):
		# increases the account balance by the current balance * the interest rate (as long as the balance is positive)
		if self.balance>0:
			self.balance=round(self.balance*(1+self.int_rate), 2)

myAccount = BankAccount(0.17,100000)

myAccount.display_account_info()
myAccount.deposit(73)
myAccount.display_account_info()
myAccount.withdraw(13)
myAccount.display_account_info()
myAccount.yield_interest()
myAccount.display_account_info()