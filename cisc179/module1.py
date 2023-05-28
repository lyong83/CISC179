from cisc179.Vehicle import Vehicle

class Module1Class:
    def execute(self):
        pickup_truck = PickupTruck("Manufacturer", 10000, 25000, 5, ["Option 1", "Option 2"], 500)
        dialog_text = f"Manufacturer: {pickup_truck.manufacturerName}\n" \
                      f"Miles: {pickup_truck.milesOnVehicle}\n" \
                      f"Price: {pickup_truck.price}\n" \
                      f"Number of Seats: {pickup_truck.numberOfSeats}\n" \
                      f"Options: {', '.join(pickup_truck.options)}\n" \
                      f"Cargo Capacity: {pickup_truck.getCargoCapacity}"

        return dialog_text

class PickupTruck(Vehicle):
    def __init__(self, manufacturerName, milesOnVehicle, price, numberOfSeats, options, cargoCapacity):
        super().__init__(manufacturerName, milesOnVehicle, price, numberOfSeats, options)
        self.cargoCapacity = cargoCapacity

    @property
    def getCargoCapacity(self):
        return self.cargoCapacity
