# This file is core of the application

from flask import Flask, render_template, Response
import cv2
import detecthands as dh2
import gamestage
import mediapipe as mp
application = Flask(__name__)



# this func renders the display for the play section
@application.route('/play')
def play():
    return render_template('play.html')

# Video streaming route. This function initiates and runs webcam feed. Note the call to the main function
@application.route('/go')
def go():
    return Response(main(), mimetype='multipart/x-mixed-replace; boundary=frame')


# rendering home page
@application.route('/')
def home():
    return render_template('home.html')

# the main "driver function" of the game
def main():
    #initialize the game instance
    game = gamestage.GameStage(1, 1920, 1080)
    cap = cv2.VideoCapture(1)
    counter = 0
    max = 60
    
    while True:
        
        # running the hand detection model on current frame
        model_results = dh2.run_model(cap)
        image = model_results[0]
        results = model_results[1]
        image_height, image_width, _ = image.shape
        
        
        # essentially updating the game with all the new circles here depending on current counter
        if counter == 0 and max <= 40:
            game.add_circle()
            game.add_circle()
            game.add_circle()
        elif counter == 0 and max <= 50:
            game.add_circle()
            game.add_circle()
        elif counter == 0:
            game.add_circle()
        elif counter == max:
            counter = -1
            max = max-3
        counter += 1
        
        
        # checking which circles are captured and not
        game.check_circles(results, image_width, image_height)

        # redrawing the relevant circles after update
        image = dh2.redraw_circles(image, game)
        
    
        # translating each frame to jpg for network transmission
        if game.check_game_over():
            image = dh2.write_game_over(image, game)
            ret, buffer = cv2.imencode('.jpg', image)
            image = buffer.tobytes()
            yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
            cv2.destroyAllWindows()
            break
        else:
            ret, buffer = cv2.imencode('.jpg', image)
            image = buffer.tobytes()
            yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
        
        
            
    cap.release()



if __name__ == '__main__':
    application.run(debug=False)