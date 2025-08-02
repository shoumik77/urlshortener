
class BankAccount:
    def __init__(self, acc_num, owner, account_type):
        self.acc_num = acc_num
        self.owner = owner
        self.balance = 0
        self.account_type = account_type

    def getAccountNumber(self):
        return self.acc_num
    
    def deposit(self, amount):
        balance += amount

    def withdraw(self, amount):
        if amount <= balance:
            balance -= amount
        else:
            print('Withdraw amount exceeds balance')
