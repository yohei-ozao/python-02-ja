class Inventory:
    def __init__(self):
        self.vehicles = []
        
    def add_vehicl(self, v_input):
        vehicle = Vehicle(
            model = v_input["model"],
            make = v_input["make"],
            year = v_input["year"],
            price = v_input["price"],
        )
        self.vehicles.append(vehicle)


    def apply_discount(self, function, dicount):
        for vehicle in self.vehicles:
            if function(vehicle):
                vehicle.discount = dicount