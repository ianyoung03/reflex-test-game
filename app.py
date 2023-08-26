from flask import Flask, render_template, Response
import cv2
import detecthands as dh2
import gamestage
import mediapipe as mp
app = Flask(__name__)


@app.route('/')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(hello(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/')
def hello():
    mp_hands = mp.solutions.hands
    # initialize a game instance
    # big loop. put the with hands stuff here?
        #run the mp model on a frame and be returned a cv2 image: image = runModel()
        #image = run_detection_model()
        #update_game(cv2image we receive)
        #uddate_view(image)
    radius = 20
    colour = (255, 102, 0)
    thickness = 2

    game = gamestage.GameStage(1, 1920, 1080)
    cap = cv2.VideoCapture(0)
    counter = 0
    while True:
        # this is the controller component of MVC. We run the model on a given frame, and get back results data, as well as the image of it
        model_results = dh2.run_model(cap)
        image = model_results[0]
        results = model_results[1]
        image_height, image_width, _ = image.shape
        
        #print(image_width)
        #print(image_height)
        
        # essentially updating the game with all the new circles here
        if counter == 0:
            game.add_circle()
        elif counter == 60:
            counter = -1
        counter += 1
        #cv2.flip(image, 1)
        
        #cv2.flip(image,1)
        game.check_circles(results, image_width, image_height)
        
        # "updating" the view ie drawing the still existing circles and updating viewfinder
        
        #cv2.putText(image, str(game.score), (400,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        image = dh2.redraw_circles(image, game)
        
        # translating each frame to jpg for network transmission
        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
        
        if game.check_game_over():
            break
        
        
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

            
    cap.release()
    


if __name__ == '__main__':
    app.run()