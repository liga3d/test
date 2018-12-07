import turtle
import random


def draw_circle_xy(x, y, r):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.fillcolor(random.random(), random.random(), random.random())
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()


turtle.hideturtle()
turtle.speed(0)
answer = ''
while answer != 'N':
	answer = turtle.textinput("Draw more?", 'Y/N')
	if answer != 'N':
		for i in range(0, 99):
			draw_circle_xy(random.randrange(-300, 300), 
				random.randrange(-300, 300), random.randrange(1, 100))
