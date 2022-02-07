"""
Name: Jillian Landin
hw3.py

Problem: using graphics package with for loops

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def squares():
    width = 350
    height = 350
    win = GraphWin("Lab 4", width, height)

    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to create new square")
    instructions.draw(win)

    shape = Rectangle(Point(20, 20), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")

    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()

    inst_pt = Point(width / 2, height - 10)
    instructions_2 = Text(inst_pt, "Click again to close")
    instructions_2.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    inst_pt = Point(200, 350)
    instructions = Text(inst_pt, "Click to create 2 points on a rectangle")
    instructions.draw(win)

    p = win.getMouse()
    p2 = win.getMouse()
    shape = Rectangle(p, p2)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    length = abs(p.getY() - p2.getY())
    width = abs(p.getX() - p2.getX())
    perimeter = 2 * (length + width)
    area = (width * length)

    instructions.undraw()
    inst_pt = win.getMouse()
    instructions_2 = Text(inst_pt, "Perimeter = " + str(perimeter))
    instructions_2.draw(win)
    inst_pt2 = win.getMouse()
    instructions_3 = Text(inst_pt2, "Area = " + str(area))
    instructions_3.draw(win)
    win.getMouse()

    instructions_2.undraw()
    instructions_3.undraw()

    inst_pt = Point(200, 350)
    instructions_4 = Text(inst_pt, "Click to quit")
    instructions_4.draw(win)
    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    num_clicks = 2

    inst_pt = Point(200, 350)
    instructions = Text(inst_pt, "Click to create center and outer edge of a circle")
    instructions.draw(win)

    p = win.getMouse()
    p2 = win.getMouse()

    px = p.getX()
    py = p.getY()
    p2x = p2.getX()
    p2y = p2.getY()
    radius = math.sqrt(((p2x - px) ** 2 + (p2y - py) ** 2))

    shape = Circle(p, radius)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    instructions.undraw()
    inst_pt = win.getMouse()
    instructions_2 = Text(inst_pt, "Radius = " + str(radius))
    instructions_2.draw(win)
    win.getMouse()
    instructions_2.undraw()

    inst_pt = Point(200, 350)
    instructions_4 = Text(inst_pt, "Click to quit")
    instructions_4.draw(win)
    win.getMouse()
    win.close()


def pi2():
    n = eval(input("enter the number of terms to sum:"))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + 2 * i
        frac = (num / denom) * ((-1) ** i)
        acc = acc + frac
    print("pi approximation: ", acc)
    print("accuracy: ", math.pi - acc)


def main():
    # squares()
    # rectangle()
    # circle()
    pi2()


main()
