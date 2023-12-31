# this file is the class that represents the game itself
import circle
import mediapipe as mp
mp_hands = mp.solutions.hands
BUFFER = 100 # the value that the center point of hand must be within
OB = -5 # out of bounds value (if the hand is out of bounds feed dead coordinates)
class GameStage:
    score = 0 # num of "grabbed" circles
    missed_circles = 0 # how many missed circles there are 
    active_circles = [] # List of all active circles
    #window_x = 0
    #window_y = 0
    lives = 3

    def __init__(self, difficulty, window_x, window_y):
        self.difficulty = difficulty
        self.windox_x = window_x
        self.window_y = window_y
    
    # updates the data of all the circles currently in the game
    def check_circles(self, results, image_width , image_height):
        if results.multi_hand_landmarks != None:
            #getting pos of both hands in x and y coords
            x1 = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
            y1 = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
            x1_scaled = x1*image_width
            y1_scaled = y1*image_height
            
            if (len(results.multi_hand_landmarks) >= 2):
                x2 = results.multi_hand_landmarks[1].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                y2 = results.multi_hand_landmarks[1].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                x2_scaled = x2*image_width
                y2_scaled = y2*image_height
            else:
                x1_scaled = OB
                y1_scaled = OB
                x2_scaled = OB
                y2_scaled = OB
            
            
        else: 
            x1_scaled = OB
            y1_scaled = OB
            x2_scaled = OB
            y2_scaled = OB

        for circ in self.active_circles:
            circ.lifetime = circ.lifetime - 1
            #lifetime condition (if circle isn't caught do stuff)
            if circ.lifetime == 0:
                self.increase_missed_circ()
                self.active_circles.remove(circ)

            # condition: if coordinates of hand are within a certain bound of the coordinates of the circle, remove circle
            if circ.x >= x1_scaled - BUFFER and circ.x <= x1_scaled + BUFFER and circ.y >= y1_scaled - BUFFER and circ.y <= y1_scaled + BUFFER:
                self.active_circles.remove(circ)
                self.score += 1
            elif circ.x >= x2_scaled - BUFFER and circ.x <= x2_scaled + BUFFER and circ.y >= y2_scaled - BUFFER and circ.y <= y2_scaled + BUFFER:
                self.active_circles.remove(circ)
                self.score += 1

    def increase_missed_circ(self):
        self.missed_circles += 1
    
    # func that checks if game is over
    def check_game_over(self):
        if self.missed_circles == self.lives:
            return True
    
    # func that adds another circle to the model
    def add_circle(self):
        self.active_circles.append(circle.Circle(0,30))


    
        
