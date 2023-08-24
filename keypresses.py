# File being used for testing purposes
INDEX_DOWN = 0.80
MIDDLE_DOWN = 0.80
RING_DOWN = 0.78
PINKY_DOWN = 0.74
THUMB_DOWN = 0.69
NEG_ONE = 1
def print_keys(hand_result, mp_hands):
    if hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*NEG_ONE >= INDEX_DOWN:
        print(hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)
        print("INDEX DOWN")
    #print("x: " ,hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x)
    print("INDEX y: " ,hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
    print("INDEX y: " ,hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y)
    print("INDEX y: " ,hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y)
    print("INDEX y: " ,hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_TIP].y)
    print("INDEX y: " ,hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.THUMB_TIP].y)
