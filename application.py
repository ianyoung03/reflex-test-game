from flask import Flask, render_template, Response
import cv2
import detecthands as dh2
import gamestage
import mediapipe as mp
import time
application = Flask(__name__)
#app = application

@application.route('/')
def hello_world():
    return "hello world"
"""
@app.route('/play')
def play():
    return render_template('play.html')

# Video streaming route. Put this in the src attribute of an img tag
@app.route('/go')
def go():
    return Response(main(), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/')
def home():
    return render_template('home.html')
#@app.route('/')
def main():
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
    cap = cv2.VideoCapture(1)
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
        
        #if game.check_game_over():
            #print("got to here")
         #   image = dh2.write_game_over(image, game)
        
        #if game.check_game_over():
            #cv2.destroyAllWindows()
        #    break
        # translating each frame to jpg for network transmission
        if game.check_game_over():
            #print("in")
            image = dh2.write_game_over(image, game)
            ret, buffer = cv2.imencode('.jpg', image)
            image = buffer.tobytes()
            yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
            #over = True
            cv2.destroyAllWindows()
            break
        else:
            ret, buffer = cv2.imencode('.jpg', image)
            image = buffer.tobytes()
            yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
        
        
        
        
        
        
        
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    cv2.destroyAllWindows()
        #    break

            
    cap.release()
"""


if __name__ == '__main__':
    application.run(debug=False)