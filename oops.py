from abc import ABC,abstractmethod
class vehicle:
    def __init__(self, Type):
        self.Type = Type
        self.actions = self.actions(Type)

        if self.Type!="cycle":
            self.EngineState = "OFF"
            self.IsMoving = "Not Moving"

    @abstractmethod
    def ListSensors(self):
        pass
    def properties(self, NoOfWheels=None, TopSpeed=None, weight=None, manufacturer=None):
            self.NoOfWheels = NoOfWheels
            self.TopSpeed = TopSpeed
            self.weight = weight
            self.manufacturer = manufacturer
            self.color = None


    def start(self):
        if self.Type != "cycle":
            self.EngineState = "ON"
            print("your ", self.Type, " is Started")
        else:
            print("Your cycle is ready  to Pedal")

    def off(self):
        if self.Type != "cycle":
            self.EngineState = "OFF"
            print("your ", self.Type, " is turned OFF")
        else:
            print("Your cycle is stopped")
    class actions:
        def __init__(self,Type):
            self.Type = Type
        def accelerate(self):
            self.IsMoving = "Moving"
            print("your ",self.Type," is accelerating")
        def brake(self):
            self.IsMoving = "Not Moving"
            print("your ",self.Type," is stopped")


    def safetyfeatures(self):
        if(self.Type == "bike" or self.Type == "cycle"):
            print("Basic Safety Features: first Aid Kit Provided,Required Repairing Tools Provided")
        elif(self.Type == "car" or self.Type=="Truck"):
            print("Basic Safety Features: first Aid Kit Provided,Required Repairing Tools Provided, Airbags Provided")


    def DisplayAllDetails(self):
        print("Type : ", self.Type, "\nNoOfWheels : ", self.NoOfWheels, "\nTopSpeed : ", self.TopSpeed, "\nmanufacturer :",
              self.manufacturer, "\nColor: ", self.color)


class factory(vehicle):

    def paint(self,color):
        self.color= color
    def ListSensors(self):
        if(self.Type == "cycle"):
            print("side stand sensor")
        elif(self.Type == "bike"):
            print("side stand sensor, fuel indicator sensor")
        else:
            print("door sensor, seatbelt sensor, fuel indicator sensor,parking sensor")
    def safetyfeatures(self):
        if(self.Type == "bike"or self.Type == "cycle"):
            print("Basic Safety Features: first Aid Kit Provided,Required Repairing Tools Provided,"
                  "\n Advanced Safety Features: SideStand Sensor available,leg and hand guards are provided")
        else:
            print("Basic Safety Features: first Aid Kit Provided,Required Repairing Tools Provided, Airbags Provided",
                  "\nAdvanced Safety Features: parking sensors provided, reverse parking cameras provided, selt belt indicator, ")


car2 = factory("car")
car2.properties(4, 180, 1000, "toyota")

car2.paint("white")
car2.DisplayAllDetails()
car2.safetyfeatures()
car2.start()
car2.off()
car2.ListSensors()
car2.actions.accelerate()
print("Engine State : ",car2.EngineState,"\nMoving State :",car2.IsMoving)
