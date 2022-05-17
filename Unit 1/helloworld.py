# robot maze
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
square = 50
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.fd(square)

def turn_left():
  robot.lt(90)

def reset():
  robot.penup()
  robot.goto(startx, starty)
  robot.pendown()

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)

#----- init robot
robot = trtl.Turtle(shape="turtle")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.pendown()

#---- TODO: change maze here
wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:
'''
i = 0
while (i < 3): # forward 3
  i += 1
  move()
'''

#---- end robot movement 

wn.mainloop()
