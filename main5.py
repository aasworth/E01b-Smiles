#!/usr/bin/env python3

import utils, open_color, arcade    #Import the necessary libraries into the file

utils.check_version((3,7))      #Checks to verify that the user has python 3.7 downloaded on their computer

SCREEN_WIDTH = 800      # This sets the screen width to be 800 pixels
SCREEN_HEIGHT = 600     # This sets the screen height to be 600 pixels 
SCREEN_TITLE = "Smiley Face Example"    # This sets the screen title to say "Smiley Face Example" at the top of the window

class Faces(arcade.Window):     #Creates a class in the file, which purpose is to create a window inside of the pop-up arcade box to track where the mouse is.
    """ Our custom Window Class"""

    def __init__(self):     # This is an initializer that initializes the class window to be the pop-up game window. This lets python track where the mouse is inside of the window.
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)     #Actually calls the initializer with the variables being the width, height, and name of the window declared above

        # Show the mouse cursor
        self.set_mouse_visible(True)    #Tells the class that the mouse is visible to the program

        self.x = SCREEN_WIDTH / 2       #This is the x variable where the mouse location is stored. it is divided by 2 because the face must be centered around the mouse.
        self.y = SCREEN_HEIGHT / 2      #This is the y variable where the mouse location is stored. it is divided by 2 because the face must be centered around the mouse.

        arcade.set_background_color(open_color.white)   #Sets the background of the screen to be white

    def on_draw(self):      #This is the function inside the file that will actually draw the face onto the screen!
        """ Draw the face """
        arcade.start_render()   #Must have this at the beginning of the draw functions anytime you want to draw something on the screen
        face_x,face_y = (self.x,self.y)     #This sets where the yellow face is drawn. unlike previous files, this uses "self.x/y", the same variables that the mouse tells python where it is at on the screen.
        smile_x,smile_y = (face_x + 0,face_y - 10)      #This sets the smile inside of the face, with appropriate offset
        eye1_x,eye1_y = (face_x - 30,face_y + 20)       #This sets the first (left) eye inside of the face, with appropriate offset
        eye2_x,eye2_y = (face_x + 30,face_y + 20)       #This sets the second (right) eye inside of the face, with appropriate offset
        catch1_x,catch1_y = (face_x - 25,face_y + 25)   #This sets the first (left) gray catch circle inside of the left eye, again with appropriate offset
        catch2_x,catch2_y = (face_x + 35,face_y + 25)   #This sets the second (right) gray catch circle inside of the right eye, with appropriate offset

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3)
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4)
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black)
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black)        # ALL of lines 37-43 draw the shapes that were previously declared inside of lines 29-35
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4)   #This line just draws the black outline on the outside of the yellow smiley face



    def on_mouse_motion(self, x, y, dx, dy):        #This function is what actually tells the rest of the program where the location of the mouse is on the screen
        """ Handle Mouse Motion """
        self.x = x  #Sets the location in the program to be the location of the mouse, horizontally
        self.y = y  #Sets the location in the program to be the location of the mouse, vertically



window = Faces()    #This calls the Faces class, starting the windows that the face will be drawn in and the window that will sense the mouse location
arcade.run()        #This finally calls the arcade that draws the face in the location of the mouse.