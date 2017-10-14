import random
import turtle
from collections import defaultdict
import math
import sys


def drawGrid():
	turtle.penup()
	turtle.goto(-25, 25)
	turtle.pendown()
	turtle.left(90)
	drawColumns()
	turtle.left(90)
	drawRows()
	turtle.forward(200)
	turtle.right(90)
	turtle.forward(200)

def drawColumns():
	for i in range(2):
	    turtle.right(90)
	    turtle.forward(50)
	    turtle.right(90)
	    turtle.forward(200)
	    turtle.left(90)
	    turtle.forward(50)
	    turtle.left(90)
	    turtle.forward(200)

def drawRows():
	for i in range(2):
	    turtle.forward(200)
	    turtle.left(90)
	    turtle.forward(50)
	    turtle.left(90)
	    turtle.forward(200)
	    turtle.right(90)
	    turtle.forward(50)
	    turtle.right(90)
def rest1():
	turtle.penup()
	turtle.goto(0,0)
	turtle.pendown()

def mapIt(x,y):
	# 	print(x,y)
	if x>-25 and x<175 and y<25 and y>-175:
		radius=25
		turtle.penup()
		turtle.goto(math.floor((x+25)/50)*50,math.floor((y+25)/50)*50)
		turtle.pendown()
		turtle.goto(math.floor((x+25)/50)*50+radius,math.floor((y+25)/50)*50)
		colorIt(25)

def inMap(Input,player):
	turtle.penup()
	turtle.goto((Input%4)*50,-int(Input/4)*50-25)
	turtle.pendown()
	if player=='H':                  
		turtle.color("blue")                        #1-> H, blue
		colorIt(25)
	if player=='M':
		turtle.color("green")
		colorIt(25)


def player(win):   # to map on the player as we click on it. This way no keyboard is required
	win.onclick(mapIt)		

def colorIt(radius):
	turtle.begin_fill()
	turtle.circle(radius)
	turtle.end_fill()

# def main():

# 	# board=
# 	win = turtle.Screen()
# 	drawGrid()
# 	inMap(9,'M')
# 	win.listen()
# 	win.mainloop()
	

# if __name__ == "__main__":
# 	main()

