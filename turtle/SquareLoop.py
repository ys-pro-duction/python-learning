import random
from time import sleep
from turtle import Turtle, Screen

t = Turtle()
t.speed(0)
s = Screen()
s.screensize(600, 600, "black")
t.color("black")
t.goto(-300, 300)
height = s.window_height()
width = s.window_width()
print(height, width)
gap = 1
angel = 90
t.color("white")
t.forward(width)
width *= gap
while True:
    t.right(angel)
    t.color(random.random(), random.random(), random.random())
    t.forward(height)
    height *= gap
    t.right(angel)
    t.forward(width)
    width *= gap
    t.right(angel)
    t.forward(height)
    height *= gap
    t.right(angel)
    t.forward(width)
    width *= gap
    gap -= 0.001
    angel -= 0.06
    t.pensize(91-angel)
