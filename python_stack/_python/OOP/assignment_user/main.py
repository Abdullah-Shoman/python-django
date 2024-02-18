# assignment: user 

class user:

    def __init__(self,name,email_address):
        self.name= name
        self.email_adress = email_address
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance +=amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User:",self.name,",Account Balance $",str(self.account_balance))

    def transfer_money(self,other_user,amount):
        if(self.account_balance != 0):
            other_user.make_deposit(amount)
            self.make_withdrawal(amount);

# User 1
user1 = user("abdullah","abdullah119@gmail.com");
user1.make_deposit(500)
user1.make_deposit(500)
user1.make_deposit(200)
user1.make_withdrawal(150)
user1.display_user_balance()
# User 2
user2 = user("ahmad","ahmad@gmail.com")
user2.make_deposit(100)
user2.make_deposit(300)
user2.make_withdrawal(200)
user2.display_user_balance()
# User 3
user3 = user("smer","smer_mohammad@outlook.com")
user3.make_deposit(1000)
user3.make_withdrawal(10)
user3.make_withdrawal(50)
user3.make_withdrawal(200)
user3.display_user_balance()
#  bonus 
user1.transfer_money(user2,50)
user1.display_user_balance()
user2.display_user_balance()
