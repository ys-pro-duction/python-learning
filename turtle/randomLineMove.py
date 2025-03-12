from time import sleep
from turtle import Turtle, Screen
import random
t = Turtle()
t.speed(0.01)
s = Screen()
s.bgcolor("black")
forward = 1
for i in range(0,9999):
    t.color(random.random(),random.random(),random.random())
    t.left(forward%360)
    t.forward(3)
    # t.color("black")
    # t.setx(0)
    # t.sety(0)
    forward *= 1.005
    t.pensize(50/forward)
# for i in range(0,9999):
#     t.color(random.random(),random.random(),random.random())
#     t.left(random.randint(0,4)*90)
#     t.forward(5*forward)
#     if i % 30 == 0:
#         # t.color("black")
#         t.setx(0)
#         t.sety(0)
#         forward += 1
#         t.pensize(forward)

    # sleep()
