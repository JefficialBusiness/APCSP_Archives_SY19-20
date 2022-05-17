#   a123_apple_1.py
import turtle as trtl


apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")



apple = trtl.Turtle()

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_fall(active_apple):
  active_apple.goto(active_apple.xcor(), active_apple.ycor() - 150)
  wn.update()

def draw_an_A():
  apple.color("blue")
  apple.write("A", font=("Arial", 74, "bold")) 

draw_apple(apple)

wn.onkeypress(apple_fall, "a")
wn.listen()
trtl.mainloop()