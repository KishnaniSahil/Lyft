class Calliope(Car):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needs_service(self):
        # Implement the service criteria for Calliope car
        # based on the new design
        pass

# Create an instance of the Calliope car
car = Calliope("2022-01-01")

# Check if the car needs service
if car.needs_service():
    print("Car needs service.")
else:
    print("Car does not need service.")
