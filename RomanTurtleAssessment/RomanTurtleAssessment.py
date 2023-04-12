# Instructors/Lecturers:   Roman Mitch, Pinal Shah and Marina Kharitonova

# John Meni Williams - 20210689

# For the below Project I used the following online resources:

# Turtle Graphics Links:

# https://pythonguides.com/turtle-programming-in-python/
# https://docs.python.org/3/library/turtle.html
# https://vegibit.com/draw-color-filled-shapes-in-python-turtle/#:~:text=You%20can%20do%20so%20using,filled%20with%20the%20color%20blue.
# https://www.geeksforgeeks.org/python-turtle-pencolor-method/
# https://www.futurelearn.com/info/courses/object-oriented-principles/0/steps/31483

#  Digital Course Manual in Canvas
#  LinkedIn free student tutorials
#  W3schools free online tutorials
#  Codecademy online beginner interactive tutorials
#  Python.org the Official Python website that provided fundamental to advanced concepts
#  GitHub which has a vast repository of Python code examples that can be used to be able to learn from other people's code.

# import the turtle library

# the turtle library is a module containing functions and
# methods that allow me to create turtle objects and manipulate them

import turtle
import random
import winsound
import time

# screen size configuration

ws = turtle.Screen()  # create a new turtle screen object
ws.title("Python Turtle Rules - 20210689") # add title to canvas title bar
ws.bgcolor("pink") # change screen background color
ws.setup(width=800, height=800)  # canvas screen size

# define an audio for shape draw
def play():  # define a play function to use after each shape has been drawn
    winsound.PlaySound("bounceball.wav", winsound.SND_ALIAS)  # this will play the "Bounceball.wav" file not MP's friendly

ws.listen()
ws.onkeypress(play,"space")  # this defines that the audio file will play on "spacebar" keyboard shortcut

time.sleep(0) # pause function allows code to pause in seconds, discuss canvas, title, gridline, spacebar sound

t = turtle.Turtle()  # create a new turtle object to draw gridlines

def draw_yaxs(val, height):  # define a function to draw vertical lines of grid
    t.up()  # lift the pen up
    t.goto(val, -height/2)  # move to the left end of the screen at the given y coordinate
    t.down()  # put the pen down
    t.goto(val, height/2)  # move to the top of the screen at the given y coordinate

def draw_xaxs(val, width):  # define a function to draw horizontal lines
    t.up()  # lift the pen up
    t.goto(-width/2, val)  # move to the left end of the screen at the left edge of the screen at the given x coordinate
    t.down()  # put the pen down
    t.goto(width/2, val)  # move to the right end of the screen at the given x coordinate

def label(width, height):  # define a function to label the axes
    t.penup()  # lift the pen up
    t.goto(0, 0)  # move to the center of the screen
    t.write(0, align="center", font=("Verdana", 18, "bold"))  # write label zero integer (0) at the center of the screen
    t.goto(width/2 - 30, 0)  # move to the right end of the screen
    t.write("x", align="center", font=("Verdana", 18, "bold"))  # write the x axis label for the x axis
    t.goto(0, height/2 - 30)  # move to the top of the screen
    t.write("y", align="center", font=("Verdana", 18, "bold"))  # write the y axis label for the y axis

ws.setup(800, 800)  # set up the turtle screen with a width and height of 800 pixels

t.speed(0)  # set the drawing speed
t.color('blue')  # set the pen grid line color to blue

width, height = ws.window_width(), ws.window_height()  # confirm the dimensions of the turtle screen

for i in range(-width//2 + 10, width//2, 20):  # draw vertical lines with a gap of 20 pixels eg 800/20=40 lines
    draw_yaxs(i, height)

for i in range(-height//2 + 10, height//2, 20):  # draw horizontal lines with a gap of 20 pixels
    draw_xaxs(i, width)

label(width, height)  # label the axes

t.hideturtle()  # hide the turtle

time.sleep(0) # discuss stop use spacebar sound, auto sound event

#Grid End -------------------------------

# define a list of colors for each title letter
colors = ["gold", "red", "blue", "orange", "gold", "red"]  # this line defines a list "[]" of colors to use for each letter of the word "TURTLE"

# define a font for the text
font = ("Arial", 80, "bold")  # this line defines a font for the text. The font is specified as a tuple of three values: the font family ("Arial"), the font size (80), and the font weight ("bold")
# the default font "Normal"

# define the starting position for the first letter
x = -290
y = 300
# with the above 2 lines these lines define the starting position for the turtle. The turtle will start at "horizontal" x-coordinate -290 and "vertical" y-coordinate 300.  The Turtle default start coordinates is (0,0)

# create a turtle object to write the letters
t = turtle.Turtle()  # this line creates a turtle object, which will be used to draw the letters

# loop through each letter in the word "TURTLE"
for i, letter in enumerate("TURTLE"):  # this line starts a loop that will iterate through each letter in the string "TURTLE".  The enumerate() function is used to get both the index (i) and value (letter) of each letter in the string

    # set the color of the pen based on the index of the letter
    t.pencolor(colors[i])  # this line sets the pen color of the turtle to the color corresponding to the current letter, using the pencolor() method defined earlier as a "list" in "colors = ["gold", "red", "blue", "orange", "gold", "red"]"

    # write the letter using turtle graphics
    t.penup()
    t.setposition(x, y)
    t.pendown()
    t.write(letter, font=font)

    # the above lines move the turtle to the correct position to write the current letter, using the penup() and pendown() methods to control the turtle's pen, and the setposition() method to move the turtle to the correct position. Finally, the write() method is used to write the current letter using the specified font.  The turtle pen motheds can be reference at this wesite link below:
    # https://pythonguides.com/python-turtle-grid/

    # move to the right for the next letter
    if letter == "A":
        x += 120
    else:
        x += 80
    # the above lines update the x-coordinate of the turtle based on the current letter. If the current letter is "A", the turtle is moved 120 pixels to the right to account for the extra width of the letter. For all other letters, the turtle is moved 80 pixels to the right. Note: with this as letters have diffeent widths this was difficult as using something like the letter capital "I" as it is a letter narrower then other letters once a word was printed extra gaps/spaces appeared between them. Exampl if I used the letter "T" OR "I" to start the output would be "T URT LE".  I am trying to see if there is a specific font that has equal letter distribution abilities

t.hideturtle()  # hide the turtle cursor

# time.sleep(20)

# draw turtle shapes begins  -------------------------------------

# in this code below, "turtle.Turtle" is the class, and "t" is an object of the turtle class

# penup(), pendown(), goto(), color(), begin_fill(), circle(), end_fill(), forward(), left(), and hideturtle() are methods 


# the circle wil be drawn first, then the triangle is drawn, and finally, the 4 squares are drawn cross tiled below the triangle

# Note: experimenting with "goto(horizontal, verticle)" co-ordinates for the shapes was hard

# create a turtle class object

t = turtle.Turtle()

#  set the fill colors for the shapes

circle_color = "red"
triangle_color = "green"
square1_color = "blue"
square2_color = "yellow"
square3_color = "orange"
square4_color = "purple"


# draw a circle

# the below lines create a turtle object, instructing it to move to a specific location on the canvas first, and then draw a circle with a radius of 150 pixels, then fill
# the circle with a specified color, and finally finish drawing the shape

t.penup() # this line gets the pen ready to move into position on the canvase ready to draw with the pen
t.goto(0, -150) # this line moves the turtle to the coordinates (0, -150) on the canvas. On the canvas the coordinates of (0,0) are the center of the canvas
t.pendown() # this line puts the turtle's pen back down, so that it will draw when it moves from the designated start co-ordinates
t.color("black", circle_color) # pen will draw circle shape/outline in "black"
t.begin_fill() # this line tells the turtle to start filling in the shape using "circle_color = "red" method created above
t.circle(150) # this line instructs the turtle to draw a circle with a radius of 150 pixels
t.end_fill() # this line instructs the turtle to stop filling the shape with color
play() # play above attached audio file at shape end (this will now apply to all shapes)

# draw a triangle to top right of the circle with a filled color of "green"

t.penup()
t.goto(-20, 150)

# Note that with goto the first value inside the () is hoizontal value negative value moves to left and positive value move to the right
# Note that with goto the second value inside the () is vertical value negative value moves down and positive value moves up

t.pendown()
t.color("black", triangle_color)
t.begin_fill()
for i in range(3): # this defines 3 sides of the shape to draw
    t.forward(150) # this defines go forward by a 150 units
    t.left(120)    # this defines turn left by 120 degrees
t.end_fill()
play()
 

# draw four squares below the triangle in a checkerboard pattern just below the triangle and fill with colors from the method above

# First square

t.penup()
t.goto(-50, -50)
t.pendown()
t.color("black", square1_color)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
play()

# Second square

t.penup()
t.goto(50, -50)
t.pendown()
t.color("black", square2_color)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
play()

# Third square

t.penup()
t.goto(0, 50)
t.pendown()
t.color("black", square3_color)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
play()

# Fourth square

t.penup()
t.goto(0, -150)
t.pendown()
t.color("black", square4_color)
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
play()

# move a ball -------------------------------------------

ws.setup(600, 600) # reduces canvas size loose text but zoom in effect on graphics
t.penup()
t.goto(0, 0)
t.pendown()
t.width(5)
t.color("gold")
t.shape("circle")
t.pencolor("black")

if t.xcor() > 290 or t.xcor() < -290:
    # speedy = -speedy
    speedx = random.choice([290, -290])

speedx = 97
t.setx(t.xcor() + speedx) # check ball position, currently (0.0) and move at speed of x
play()

if t.ycor() > 290 or t.ycor() < -290:

    speedy = random.choice([290, -290])

speedy = 97
t.sety(t.ycor() + speedy) # check y coordinates
play()

# turtle spiral shape begins and loops 11 times
Circles = turtle.Turtle()
for i in range(10):
    Circles.circle(10 * i)
t.penup()
play()
t.goto(300, 3000)
turtle.exitonclick()
