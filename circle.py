import random
# Each circle that appears is an object. This is the class for it
class Circle:
    x = 0
    y = 0
    caught = False
    lifetime = 30

    def __init__(self, index, lifetime):
        self.index = index
        self.caught = False
        self.lifetime = lifetime
        self.x = random.randrange(0, 1920)
        self.y = random.randrange(0,1080)
    
    def decrement_lifetime(self):
        self.lifetime =- 1
        
        
        