# Challenge 1
Create the beginnings of a polymorphic vehicle system using an abstract base class, inheritance, and polymorphism.

## Requirements
- Define `Vehicle` as an abstract class with a concrete implementation of a `get_details()` method and an additional abstract method `start_engine()`.
- Vehicles should have `make`, `model`, and `year` instance variables.
- Create at least two classes that inherit from `Vehicle` including `Car` and `Truck`.
- Implement the abstract method from `Vehicle` in each subclass and extend the `get_details()` method to include specific details for each vehicle type using `super`.
- For `Truck`, include at least one additional attribute including `towing_capacity`.
- Implement a `display_vehicle_details` function that can process objects of any type derived from `Vehicle`.
- Adhere to SOLID principles, ensuring your classes are well-structured and maintainable.

## Example code with expected outputs
```python
...

car = Car(make="Toyota", model="Corolla", year=2021)
truck = Truck(make="Ford", model="F-150", year=2020, towing_capacity=5000)

print(car.get_details())  # Car: 2021 Toyota Corolla
print(truck.get_details())  # Truck: 2020 Ford F-150, Towing Capacity: 5000

display_vehicle_details(car)  # Car: 2021 Toyota Corolla
display_vehicle_details(truck)  # Truck: 2020 Ford F-150, Towing Capacity: 5000
```
