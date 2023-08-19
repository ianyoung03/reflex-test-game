KEY_DOWN = 0.11
NEG_ONE = -1
def print_keys(hand_result, mp_hands):
    if hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z*NEG_ONE <= KEY_DOWN:
        print("INDEX DOWN")
    
    print(hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].z)
    
    if hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].z*NEG_ONE <= KEY_DOWN:
        print("MIDDLE DOWN")

    if hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.RING_FINGER_TIP].z*NEG_ONE <= KEY_DOWN:
        print("RING DOWN")

    if hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.PINKY_TIP].z*NEG_ONE <= KEY_DOWN:
        print("PINKY DOWN")

    if hand_result.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.THUMB_TIP].z*NEG_ONE <= KEY_DOWN:
        print("THUMB DOWN")