from Vehicle import Vehicle

class Bike(Vehicle):
    def calculate_rent(self,days):
        service_charge = 100
        Total = self.Retrieve_rent * days + service_charge
        return Total 