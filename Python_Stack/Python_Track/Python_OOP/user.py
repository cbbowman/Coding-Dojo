class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance+=amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance-=amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}")
        print(f"Balance: {self.account_balance}")

user1 = User("Mark", "mark@email.com")
user2 = User("Joe", "joe@email.com")
user3 = User("Jack", "jack@email.com")

user1.make_deposit(10).make_deposit(10).make_deposit(10).make_withdrawl(2).display_user_balance
user2.make_deposit(10).make_deposit(10).make_withdrawl(2).make_withdrawl(2).display_user_balance
user2.make_deposit(100).make_withdrawl(10).make_withdrawl(2).make_withdrawl(2).display_user_balance


