BUFFER = 20
class GameStage:
    score = 0 # num of "grabbed" circles
    missed_circles = 0 # how many missed circles there are 
    active_circles = [] # List of all active circles
    window_x = 0
    window_y = 0

    def __init__(self, difficulty, window_x, window_y):
        self.difficulty = difficulty
        self.windox_x = window_x
        self.window_y = window_y
    
    def check_circles(self, x , y):
        for circ in self.active_circles:
            #lifetime condition (if circle isn't caught do stuff)
            if circ.lifetime == 0:
                self.increaseMissedCirc()
                self.active_circles.remove(circ)

            # condition: if coordinates of hand are within a certain bound of the coordinates of the circle, remove circle
            if circ.x >= x - BUFFER and circ.x <= x + BUFFER and circ.y >= y - BUFFER and circ.y <= y + BUFFER:
                self.active_circles.remove(circ)

    def increase_missed_circ():
        missed_circles += 1

    
        
