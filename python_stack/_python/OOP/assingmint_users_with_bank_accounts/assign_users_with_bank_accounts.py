

class bank_account:

    def __init__(self, amount =0,int_rate=0.01):
        self.balance = amount
        self.int_rate = int_rate;

    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >=amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -=5
        return self

    def display_account_info(self):
        print(f"Blance:$",self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance+  (self.int_rate * self.balance)
        return self


class user:

    def __init__(self,name,email_address,amount=0):
        self.name= name
        self.email_adress = email_address
        self.account = bank_account(amount)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User:",self.name), self.account.display_account_info();    
        return self



user1 = user("Abdullah","abo.kannh7@gmial.com",200)
user1.make_deposit(200).display_user_balance().make_withdrawal(500).display_user_balance()

user2 = user("Don Litto","Donlitto@gmail.com",0)
user2.make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

