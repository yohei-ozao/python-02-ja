# Challenge 2
Create an automotive sales system.

## Part 1
- Define a Vehicle Class
  - Create a `Vehicle` class in a separate module. Attributes should include model, make, year, price, and discount. Include methods for setting and getting these attributes.
- Vehicle Inventory
  - Create an `Inventory` class that maintains a collection of `Vehicle` instances. Implement methods to add vehicles and retrieve vehicles based on various criteria (e.g., make, year, price range).
- Discount Application
  - Implement a method in the `Inventory` class to apply discounts to vehicles. Try to make use of list comprehensions, lambdas, and/or decorators for dynamic discount criteria (e.g., 5% off on all SUVs).
- Search Functionality
  - Add a method to search for vehicles by model using regular expressions. This method should return a list of vehicles matching the search pattern.
- Iterating Over Vehicles
  - Implement a generator in the `Inventory` class that allows iteration over all vehicles, yielding one vehicle at a time.

## Part 2
- Parsing Vehicle Data
  - Create a module to parse vehicle data from a text file (you can provide a sample file with vehicle details). Use string formatting and file handling to read and process this data.
- Creating Vehicle Instances
  - Use the parsed data to create instances of `Vehicle` and add them to the `Inventory`.

## Example

**vehicles.txt**
```
Corolla,Toyota,2020,20000
Civic,Honda,2021,22000
```

**main.py**
```python
from inventory import Inventory
from data_parser import parse_vehicle_data

vehicles = parse_vehicle_data("vehicles.txt")
inventory = Inventory()
for vehicle in vehicles:
    inventory.add_vehicle(vehicle)

inventory.apply_discount(lambda v: v.make == 'Toyota', 5)
toyotas = inventory.search_vehicles("Corolla")

for toyota in toyotas:
    print(toyota)

for vehicle in inventory:
    print(vehicle)
```
