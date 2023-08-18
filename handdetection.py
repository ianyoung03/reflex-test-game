import mediapipe as mp # google media pipe
import cv2 as cv # open-cv for python
import numpy as np
#from mediapipe.tasks import python
#from mediapipe.tasks.python import vision
import time
#from mediapipe.tasks import python
#from mediapipe.tasks.python import vision

#mp_drawing = mp.solutions.drawing_utils
#mp_hands = mp.solutions.hands
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

mp_drawing = mp.solutions.drawing_utils
# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('hand landmarker result: {}'.format(result))

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)

with HandLandmarker.create_from_options(options) as landmarker:
# setting up webcam usage with open cv (from here: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html )
    cap = cv.VideoCapture(2)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        # Display the resulting frame
        #detection_result = landmarker.detect(frame)
        detection_result = landmarker.detect_async(mp_image, int(round(time.time()*1000)))
        #print(int(round(time.time())*1000))
        #print(1000*int(cap.get(cv.CAP_PROP_POS_MSEC)))
        #print(cap.get(cv.CAP_PROP_POS_MSEC))
        #print(date.time)
        #detection_result = landmarker.detect_async(mp_image)
        annotated_frame = mp_drawing.draw_landmarks(mp_image.numpy_view(), detection_result)
        cv.imshow(cv.cvtColor(annotated_frame, cv.COLOR_RGB2BGR))
        #cv.imshow('view', annotated_frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
