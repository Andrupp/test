class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
    
    def start(self):
        print("Engine started.")


class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start_engine(self):
        self.engine.start()


# Creating the dependencies
engine = Engine("gasoline")
car = Car(engine)

# Using the objects
car.start_engine()