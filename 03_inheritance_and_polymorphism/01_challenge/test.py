import unittest
from vehicles import Vehicle, Car, Truck

class TestVehicleManagementSystem(unittest.TestCase):

    def test_vehicle_is_abstract(self):
        with self.assertRaises(TypeError):
            Vehicle(make="", model="", year=0)

    def test_car_is_subclass_of_vehicle(self):
        self.assertTrue(issubclass(Car, Vehicle))

    def test_truck_is_subclass_of_vehicle(self):
        self.assertTrue(issubclass(Truck, Vehicle))

    def test_car_implements_get_details(self):
        car = Car(make="Honda", model="Civic", year=2022)
        self.assertEqual(car.get_details(), "Car: 2022 Honda Civic")

    def test_truck_implements_get_details(self):
        truck = Truck(make="Chevrolet", model="Silverado", year=2021, towing_capacity=6000)
        self.assertEqual(truck.get_details(), "Truck: 2021 Chevrolet Silverado, Towing Capacity: 6000")

    def test_polymorphic_behavior(self):
        vehicles = [Car(make="Mazda", model="3", year=2021), Truck(make="Ram", model="1500", year=2022, towing_capacity=7000)]
        for vehicle in vehicles:
            self.assertTrue('2021' in vehicle.get_details() or '2022' in vehicle.get_details())

if __name__ == '__main__':
    unittest.main()

