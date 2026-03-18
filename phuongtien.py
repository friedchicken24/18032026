class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Phương tiện: {self.brand} {self.model} ({self.year})")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Ô tô: {self.brand} {self.model} ({self.year}) - Số cửa: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type

    def display_info(self):
        print(f"Xe đạp: {self.brand} {self.model} ({self.year}) - Loại: {self.type}")
my_car = Car("Toyota", "Camry", 2022, 4)
my_bike = Bike("Giant", "Escape 3", 2023, "road")

my_car.display_info()
my_bike.display_info()