from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

    @abstractmethod
    def can_withdraw(self, amount):
        pass

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposited {amount}.')
        return f'Deposited {amount}.'

    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.balance -= amount
            self.transaction_history.append(f'Withdrew {amount}.')
            return f'Withdrew {amount}.'
        else:
            return 'Withdrawal denied.'

    def apply_interest(self):
        pass

    def get_transaction_history(self):
        return self.transaction_history

    def __str__(self):
        return f'Account {self.account_number} has a balance of {self.balance}.'

class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.02

    def can_withdraw(self, amount):
        return self.balance - amount >= 0

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        self.transaction_history.append(f'Applied interest.')

class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.01

    def can_withdraw(self, amount):
        return self.balance - amount >= -500

    def apply_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
            self.transaction_history.append(f'Applied interest.')

# 使用例
alice_savings = SavingsAccount("123456", 1000)
bob_checking = CheckingAccount("987654", 500)

accounts = [alice_savings, bob_checking]

print("Initial Account Details:")
print(alice_savings)
print(bob_checking)

alice_savings.deposit(200)
alice_savings.withdraw(500)
bob_checking.deposit(300)
bob_checking.withdraw(1000)

print(alice_savings.get_transaction_history())
print(bob_checking.get_transaction_history())

print(alice_savings)
print(bob_checking)
