# reflex-test-game

Flask web application created with Flask and HTML/CSS, also utilizing Google MediaPipe and OpenCV. 

The objective of the game is to "catch" as many of the disappearing circles with your hands as you can. You get 3 lives.

**The application can be broken down as follows:**

**application.py**-> This is the core of the Flask application, the other Python files can be thought of as "modules" that hold classes, methods, and data that the application will use

**gamestage.py** -> This is a class that represents the entire game itself. Works in an observer relationship with circle.py

**circle.py** -> A small class to represent the circles that appear on the screen. Works in an observer-type relationship with gamestage.py

**detecthands.py** -> This is where the core of the hand detection happens.

**templates, static** -> holds the front end files

**hand_landmarker.task** -> data required to run the hand detection model from MediaPipe

**requirements.txt** -> all required libraries in the venv

