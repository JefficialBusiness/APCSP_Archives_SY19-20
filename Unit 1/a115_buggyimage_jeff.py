#   a115_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

legs = 6
length = 70
angle = 380 / legs
spider.pensize(5)
leg_pos = 0

while (leg_pos < legs):
  spider.goto(0,0)
  spider.setheading(angle*leg_pos)
  spider.forward(length)
  leg_pos = leg_pos + 1

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()

spider = 1
length = 5
'''
while (spider < 5):
  print(spider*y)
  spider = spider + 1 
  '''
