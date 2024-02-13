# チャレンジ2
商品のリストがあり、各商品は商品名、カテゴリー、価格を含む辞書型のデータで表されています。このチャレンジでは、`apply_discount` 関数を完成させてください。リスト内包表記とラムダ関数を使用し、最低価格のしきい値にもとづいて商品をフィルタリングした後、フィルタリングされた商品に割引を適用します。そして、商品名とその割引価格のリストを出力してください。

- リスト内包表記を使用して、最低価格のしきい値以上の商品をフィルタリングします。
- リスト内包表記の中でラムダ関数を使用し、フィルタリングされた商品に割引を適用します。
- タプルのリストとして結果を出力し、各タプルには商品名とその割引価格を含みます。

## 入力と出力の例
入力:
```python
[
    {"name": "Laptop", "category": "Electronics", "price": 1200},
    {"name": "Bread", "category": "Food", "price": 2},
    {"name": "Jacket", "category": "Apparel", "price": 100}
]
```

- 最低価格のしきい値: 50
- 割引率: 10

出力:
```python
[("Laptop", 1080.0), ("Jacket", 90.0)]
```

入力:
```python
[
    {"name": "Smartphone", "category": "Electronics", "price": 800},
    {"name": "Sneakers", "category": "Footwear", "price": 120},
    {"name": "Coffee", "category": "Beverage", "price": 5}
]
```

- 最低価格のしきい値: 100
- 割引率: 15

出力:
```python
[("Smartphone", 680.0), ("Sneakers", 102.0)]
```