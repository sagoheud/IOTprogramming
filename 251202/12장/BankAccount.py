class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance   
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self, name, number, balance, interest_rate):
        super().__init__(name, number, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self.balance
    
class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance, withdraw_charge):
        super().__init__(name, number, balance)
        self.withdraw_charge = withdraw_charge
    def withdraw(self, amount):
        return BankAccount.withdraw(self, amount + self.withdraw_charge)
    
    
a1 = SavingsAccount(10000, "홍길동", 123456, 0.05)
a1.add_interest()
print("저축예금의 잔액=", a1.balance)

a2 = CheckingAccount(2000000, "김철수", 123457, 100)
a2.withdraw(100000)
print("당좌예금의 잔액=", a2.balance)