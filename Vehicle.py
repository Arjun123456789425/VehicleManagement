from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,model,rent):
        self.model = model
        self.__rent = rent

    @property
    def Retrieve_rent(self):
        return self.__rent

    @abstractmethod
    def calculate_rent():
        pass

    def display_details(self):
        print('Model:',self.model)
        print('Rent:',self.__rent)