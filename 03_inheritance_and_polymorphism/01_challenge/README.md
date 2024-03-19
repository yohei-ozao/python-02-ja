# チャレンジ1
抽象基底クラス、継承、ポリモーフィズムを使用して、ポリモーフィックな性質を備えた初歩的な車両システムを作成します。

## 要件
- `Vehicle` を抽象クラスとして定義します。`Vehicle` には`make` (メーカー)、`model` (モデル)、`year` (年式) のインスタンス変数が必要です。
- 各車両タイプの詳細情報を含めるように `Vehicle` に `get_details()` 抽象メソッドを追加します。
- `Vehicle` を継承したクラスを2つ以上作成します (`Car`、`Truck`、その他のクラス)。
- `Truck` には、1つ以上の属性 (`towing_capacity`、その他の属性) を追加します。
- 各サブクラスで `Vehicle` の抽象メソッドを実装します。
- `Vehicle` から派生した任意のタイプのオブジェクトを処理できる `display_vehicle_details` 関数を実装します。
- SOLIDの原則を順守し、クラスを適切に構造化して容易に維持管理できるようにします。

## コード例と想定される出力
```python
...

car = Car(make="Toyota", model="Corolla", year=2021)
truck = Truck(make="Ford", model="F-150", year=2020, towing_capacity=5000)

print(car.get_details())  # Car: 2021 Toyota Corolla
print(truck.get_details())  # Truck: 2020 Ford F-150, Towing Capacity: 5000

display_vehicle_details(car)  # Car: 2021 Toyota Corolla
display_vehicle_details(truck)  # Truck: 2020 Ford F-150, Towing Capacity: 5000
```
