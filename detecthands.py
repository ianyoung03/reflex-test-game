# this class behaves as the controller and viewport in MVC. 
import keypresses
import cv2
import mediapipe as mp
import circle
import gamestage

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# just preset values for now
radius = 20
colour = (21, 248, 249)
thickness = -1



#cap = cv2.VideoCapture(0)
def run_model(cap):
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.50,
        min_tracking_confidence=0.5) as hands:
        #while cap.isOpened():
            success, image = cap.read()
            #if not success:
                #print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
                #continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)


            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            image_height, image_width, _ = image.shape
            
            # "Drawing" the detection of the hand on the hand
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            #returning the image
            return image, results
            
    #cap.release()

def redraw_circles(image, game):
    for circ in game.active_circles:
        if circ.lifetime > 0:
            image = cv2.circle(image, (circ.x, circ.y), radius, colour, thickness)    
        
    #cv2.imshow('View', cv2.flip(image, 1))

    image = cv2.flip(image,1)
    cv2.putText(image, "Score: " + str(game.score), (5,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
    cv2.putText(image, "Lives: " + str(game.lives - game.missed_circles), (5,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)

    return image

def write_game_over(image, game):
     #cv2.putText(image, "Score: " + str(game.score), (15,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
     #image = cv2.flip(image,1)
     #cv2.putText(image, "Lives: " + str(game.lives - game.missed_circles), (20,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
     cv2.putText(image, "GAME OVER",(40,640), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 8)
     return image