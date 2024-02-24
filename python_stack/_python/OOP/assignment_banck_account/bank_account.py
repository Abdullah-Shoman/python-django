

class bank_account:
    # BankAccount 

    def __init__(self, amount =0,int_rate=1.2):
        self.balance = amount
        self.int_rate = int_rate;
    
    # def __init__(self):
    #     pass 

    @classmethod 
    def test(cls,amount):
        return cls(amount,0)

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

account1 = bank_account(12,1)
account2 = bank_account().test(11)

account1.display_account_info()
account2.display_account_info()

# account1.deposit(100).deposit(200).deposit(500).withdraw(100).yield_interest().display_account_info()

# account2.deposit(200).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()
