# a121_catch_a_turtle.py

#-----import statements-----


import turtle as t
import random as rand

#-----game configuration----

# leaderboard variables
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name: ")

t_size = 2
t_color = "green"
t_shape = "triangle"
score = 0
scorepx = -195
scorepy = 155
timerpx = 195
timerpy = 155
font_setup = ("Terminal", 20, "bold")
timer = 20
counter_interval = 1000  
timer_up = False

#-----initialize turtle-----
score_writer = t.Turtle()
score_writer.penup()
score_writer.goto(scorepx,scorepy)
score_writer.hideturtle()

counter = t.Turtle()
counter.goto(timerpx,timerpy)
counter.hideturtle()

markiplier = t.Turtle(shape=t_shape)
markiplier.penup()
markiplier.fillcolor(t_color)
markiplier.shapesize(t_size)

#-----game functions--------


def markiplier_clicked(x,y):
    if timer_up == False:
        update(x,y)
        change_position()
    

def change_position():
    markiplier.hideturtle()
    newx = rand.randint(-200,200)
    newy = rand.randint(-150,150)
    markiplier.goto(newx,newy)
    markiplier.showturtle()

score = 0

def update(x,y):
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("GAME!", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)
    

      
# manages the leaderboard for top 5 scorers


#-----events----------------
countdown()
markiplier.onclick(markiplier_clicked)
wn = t.Screen()
wn.mainloop()
wn.ontimer(countdown, counter_interval) 

