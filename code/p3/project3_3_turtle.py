from turtle import *
import random
import numpy as np


def drawLines(dataset):
    screen.colormode(255)
    dotColor = (random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255))
    lineColor = (random.randint(0, 255), random.randint(0, 255),
                 random.randint(0, 255))
    i = 0
    while i < len(dataset) - 1:
        pen.color(lineColor)
        pen.goto(dataset[i][0], dataset[i][1])
        pen.pendown()
        pen.goto(dataset[i + 1][0], dataset[i + 1][1])
        pen.penup()
        t_pos = deCasteljau(dataset[i][0], dataset[i][1],
                            dataset[i + 1][0], dataset[i + 1][1])
        pen.goto(t_pos[0], t_pos[1])
        pen.color(dotColor)
        pen.dot(5)

        i += 1


def deCasteljau(x1, y1, x2, y2):
    # calculate t point between these coordinates
    t_x = (x1 * (1 - tFunction)) + (x2 * tFunction)
    t_y = (y1 * (1 - tFunction)) + (y2 * tFunction)
    t_plot = (t_x, t_y)
    t_coords.append(t_plot)
    return t_plot


screen = Screen()
screen.screensize(1500, 1000)
screen.title("deCasteljau's algorithm")
pen = Turtle()
pen.speed(5)
screen.colormode(255)
pen.penup()
pen.pensize(2)

tFunction = 0.85
t_coords = []
# controlPoints = [[(0, 0), (200, 100), (400, 0)],
#                  [(0, 0), (100, 200), (300, 200),
#                   (400, 0)]
#                  ]
x = np.linspace(0, 0.2, 7)
y = [-10, 10, 10, -20, 10, 10, -10]
controlPoints = [[(a,b) for a in x for b in y]]
for polygon in controlPoints:
    for controlpoint in polygon:
        pen.goto(controlpoint[0], controlpoint[1])
        pen.dot(5)

    for point in range(0, len(polygon) + 1):
        drawLines(polygon)
        polygon = t_coords
        t_coords = []
    screen.clearscreen()
