class Car:
    # A car needs to have an id, position and speed
    def __init__(self, id, position, velocity = (0,0)):
        self.id = id
        self.position = position
        self.velocity = velocity

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getPosition(self):
        return self.position

    def setPosition(self, postion):
        self.position = postion

    # TODO: We could add types of cars, and thus have pictures that match them. Size might also be needed