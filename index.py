class Vehicle:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')


my_car = Vehicle('Tesla', 'Model 3')
my_car2 = Vehicle('Honda', 'Model 2')

my_car.moves()
my_car2.moves()
print(my_car.make)
print(my_car2.make)
