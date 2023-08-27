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
        self.x = random.randrange(int(0*0.85), int(1920*0.85))
        self.y = random.randrange(int(0.85*0),int(1080*0.85))
    
    def decrement_lifetime(self):
        self.lifetime =- 1
        
        
        