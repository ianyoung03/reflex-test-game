# small class so that each circle in the game can be represented as an object
import random
# Each circle that appears is an object. This is the class for it
SCALING_FACTOR = 0.75
class Circle:
    x = 0 # x coord of circle
    y = 0 # y coord of circle
    caught = False
    lifetime = 30

    def __init__(self, index, lifetime):
        self.index = index
        self.caught = False
        self.lifetime = lifetime
        self.x = random.randrange(int(SCALING_FACTOR*0),int(1920*SCALING_FACTOR))
        self.y = random.randrange(int(SCALING_FACTOR*0),int(1080*SCALING_FACTOR))
    
    def decrement_lifetime(self):
        self.lifetime =- 1
        
        
        