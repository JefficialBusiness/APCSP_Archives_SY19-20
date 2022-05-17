import turtle as trtl

wn=trtl.Screen()
wn.bgcolor("red")
# turtle attributes

t = trtl.Turtle()
t.pensize(1)
t.penup()


# create Smash Ball

t.goto(100, 50)
t.pendown()
t.begin_fill()
t.fillcolor("orange")
t.circle(100, 360)
t.end_fill()
t.penup()
t.goto()

colors_weave = ("white", "black")

# create the 'SMASH BALL' text


for c in colors_weave:
    t.goto(-500, -100)
    t.pencolor(c)
    t.write('SMASH', move=False, align="left", font=("Arial", 70, "bold"))
    
    t.goto(-400, -178)
    t.pencolor(c)
    t.write('BALL', move=False, align="left", font=("Arial", 70, "bold"))

# draw the decorating triangles

t_angles = (360 = (22.5*r))

turtle