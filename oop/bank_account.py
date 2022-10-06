class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self


class User:
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

        
    def display_user_balance(self):
        print(f"Balance: {self.account.balance}")
        return self



# account1 = BankAccount(0.01, 100)
# account2 = BankAccount(0.01, 200)

# account1.deposit(50).deposit(100).deposit(125).yield_interest().display_account_info()
# account2.deposit(500).deposit(200).withdraw(25).withdraw(100).withdraw(75).withdraw(200).yield_interest().display_account_info()

new_user = User("Kelsey", "kb@abc.com")
new_user.display_user_balance()
