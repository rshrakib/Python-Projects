class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"{self.model} : {self.color}, {self.year}")

class ElectricCar(Car):
    def __init__(self, model, year, color, capacity):
        super().__init__(model, year, color)
        self.capacity = capacity
    def display_info(self):
        super().display_info()
        print(f"Battery capacity: {self.capacity}")


car1_info = Car("m1", 2001, "blue")
car1_info.display_info()

electric_car = ElectricCar("m2", 2001, "red", 200)
electric_car.display_info()