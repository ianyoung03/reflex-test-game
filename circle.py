import random
# Each circle that appears is an object. This is the class for it
class Circle:
    x = 0
    y = 0
    caught = False

    def __init__(self, index, lifetime):
        self.index = index
        self.caught = False
        self.lifetime = 180
        self.x = random.randrange(0, 500)
        self.y = random.randrange(0,500)
    
    def decrement_lifetime(self):
        self.lifetime = self.lifetime - 1
        
        
        