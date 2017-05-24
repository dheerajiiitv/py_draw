import turtle

def alphabet_D():
	d = turtle.Turtle()
	window = turtle.Screen()
	d.circle(50,180)
	d.left(90)
	d.forward(100)
	


def alphabet_H():
	h = turtle.Turtle()
	window = turtle.Screen()
	h.pu()
	h.setpos(100,100)
	h.pd()
	h.forward(100)
	h.backward(50)
	h.right(90)
	h.forward(100)
	h.left(90)
	h.forward(50)
	h.backward(100)

	window.exitonclick()


alphabet_D()
alphabet_H()