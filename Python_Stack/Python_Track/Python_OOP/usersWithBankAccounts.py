class BankAccount:
	def __init__(self, int_rate=0.01, balance=0):
		self.int_rate=int_rate
		self.balance=balance
	def deposit(self, amount=0):
		# increases the account balance by the given amount
		self.balance+=amount
		return self

	def withdraw(self, amount=0):
		# decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
		if self.balance<amount:
			print("Insufficient Funds: Charging a $5 fee")
			self.balance-=5
		else:
			self.balance-=amount
		return self

	def display_account_info(self):
		# print to the console: eg. "Balance: $100"
		print("Balance: ", self.balance)
		return self

	def yield_interest(self):
		# increases the account balance by the current balance * the interest rate (as long as the balance is positive)
		if self.balance>0:
			self.balance=round(self.balance*(1+self.int_rate), 2)
		return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_deposit(self, amount):
        if amount<0:
            return self
        self.account.balance+=amount
        return self

    def make_withdrawl(self, amount):
        if amount<0:
            return self
        if self.account.balance<amount:
            return self
        self.account.balance-=amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}")
        print(f"Balance: {self.account.balance}")

