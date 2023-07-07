from tire import Tire
def test_should_service_tires_carrigan(self):
    tire = Tire("Carrigan")
    car_factory = CarFactory("Calliope", "Spindler", tire)
    tire_wear = [0.5, 0.7, 0.8, 0.9]  # Example tire wear array
    self.assertTrue(car_factory.should_service_tires(tire_wear))

def test_should_service_tires_octoprime(self):
    tire = Tire("Octoprime")
    car_factory = CarFactory("Calliope", "Spindler", tire)
    tire_wear = [0.2, 0.6, 0.5, 1.2]  # Example tire wear array
    self.assertTrue(car_factory.should_service_tires(tire_wear))
