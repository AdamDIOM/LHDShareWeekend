import turtle
import math

s = turtle.Screen()

t = turtle.Turtle()
t.ht()
t.color("purple")
t.pensize(5)
t.speed(0)

colours = ["red", "orange", "yellow", "lime", "blue", "purple"]#, "pink"]

for i in range(1,2000):
    colour = colours[i%len(colours)]
    t.color(colour)
    t.forward(i)
    t.pensize(5+i/50)
    t.left(89)
