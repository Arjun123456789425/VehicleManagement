from Vehicle import Vehicle

class Car(Vehicle):
    def calculate_rent(self,days):
        service_charge = 500
        Total = self.Retrieve_rent * days + service_charge
        return Total