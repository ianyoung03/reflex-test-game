import keypresses
import cv2
import mediapipe as mp
import circle

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# just preset values for now
radius = 20
colour = (255, 0, 0)
thickness = 2

# Code for generating and removing circles
generatedCircles = [circle.Circle(0, 1)]
counter = 0

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.50,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
            continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)


        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_height, image_width, _ = image.shape
        
        # Now displaying a circle randomly in a certain location that will then disappear
        for circ in generatedCircles:
            if results.multi_hand_landmarks != None and circ.lifetime > 0:
                image = cv2.circle(image, (circ.x, circ.y), radius, colour, thickness)
        
        # Decrement lifetime of all "alive" circles
        for circ in generatedCircles:
            circ.decrement_lifetime()
        
        # Counter manipulation to add a circle every 60 frames
        if counter == 60:
                generatedCircles.append(circle.Circle(0,60))
                counter = 0
        else:
            counter += 1

            

        # "Drawing" the detection of the hand on the hand
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        # Displaying the annotation visual of the hands
        cv2.imshow('View', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
cap.release()
