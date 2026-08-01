print("=" * 40)
print("Bank Account")
print("=" * 40)


class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount
        print("Depoisted:", amount)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn:",amount)
        else:
            print("Insufficent Balance")

    def display_balance(self):
        print("current balance :",self.balance)


account = BankAccount("Shubham", 10000)

account.display_balance()
account.deposit(5000)
account.display_balance()
account.withdraw(3000)
account.display_balance()