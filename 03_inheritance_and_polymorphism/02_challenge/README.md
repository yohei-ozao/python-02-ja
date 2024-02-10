# Challenge 2
Create a simplified banking system that demonstrates the use of Abstract Base Classes (ABCs). The system should allow for different types of bank accounts with unique functionalities.

## Requirements
### Part 1
- Create an ABC named `Account` with the following:
  - Constructor: Initialize `account_number` and `balance`.
  - Abstract methods: `can_withdraw(amount)`.
  - Concrete methods: `deposit(amount)`, `withdraw(amount)`, `apply_interest()`, and `get_transaction_history()`.
### Part 2
- Create two subclasses: `SavingsAccount` and `CheckingAccount`.
- Implement unique withdrawal rules and interest rates for each subclass.
### Part 3
Implement a banking system that allows for account operations and showcases polymorphism in action.

## Example Usage
```python
alice_savings = SavingsAccount("123456", 1000)
bob_checking = CheckingAccount("987654", 500)

accounts = [alice_savings, bob_checking]

print("Initial Account Details:")
print(alice_savings)
print(bob_checking)

print(alice_savings.deposit(200))
print(alice_savings.withdraw(500))
print(bob_checking.deposit(300))
print(bob_checking.withdraw(1000))

print(alice_savings.get_transaction_history())
print(bob_checking.get_transaction_history())

print(alice_savings)
print(bob_checking)
```
