# チャレンジ2
抽象基底クラス (ABC) を使用したシンプルなバンキングシステムを作成します。このシステムでは、複数の種類の銀行口座を扱い、各口座の種類に独自の機能があるものとします。

## 要件
### パート1
- `Account` という名前の抽象基底クラスを次のように作成します。
  - コンストラクタ: `account_number` と `balance` を初期化
  - 抽象メソッド: `can_withdraw(amount)`
  - 具象メソッド: `deposit(amount)`、`withdraw(amount)`、`apply_interest()`、`get_transaction_history()`
### パート2
- 2つのサブクラス `SavingsAccount` と `CheckingAccount` を作成します。
- 各サブクラスでそれぞれの引き出しルールと金利を実装します。
### パート3
口座を操作するバンキングシステムを実装し、ポリモーフィズムの動作を実際に確認します。

## 使用例
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
