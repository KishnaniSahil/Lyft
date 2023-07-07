class Tire:
    def __init__(self, tire_type):
        self.tire_type = tire_type

    def should_service(self, tire_wear):
        if self.tire_type == "Carrigan":
            return any(wear >= 0.9 for wear in tire_wear)
        elif self.tire_type == "Octoprime":
            return sum(tire_wear) >= 3
        else:
            return False  # Default behavior if tire type is not recognized
