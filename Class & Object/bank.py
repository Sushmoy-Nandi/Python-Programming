class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You can withdraw below {self.min_withdraw}') 
        elif amount > self.max_withdraw:
            print(f'You can not withdraw more than {self.max_withdraw}') 
        else:
            self.balance -= amount
            print(f'Here is your money {amount}') 
            print(f'Your balance after withdraw {self.get_balance()}')

my_bank = Bank(5000)
# my_bank.withdraw(25)
# my_bank.withdraw(50000000)
# my_bank.withdraw(1000)

my_bank.deposit(2000)
my_bank.deposit(2000)
print(my_bank.get_balance())
