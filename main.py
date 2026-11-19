from Car import Car

from Bike import Bike

car = Car('Benz',4000)
car.display_details()
carrent= car.calculate_rent(6)
print('Rent of the car is:',carrent)

print('____________________________________________')

bike =Bike('R15',1500)
bike.display_details()
bikerent = bike.calculate_rent(7)
print('Rent of the Bike is :',bikerent)