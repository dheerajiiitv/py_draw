import turtle
def draw_sqaure():
	window = turtle.Screen()
	window.bgcolor("white")
	brad = turtle.Turtle()
	brad.shape("circle")
	brad.color("violet")
	brad.speed()
	count = 0
	for i in range(0,50):
		brad.right(7.3)
		count = 0
		while(count<4):
			brad.forward(100)
			brad.right(90)
			count = count+1
	
	


#def draw_circle():
#	window = turtle.Screen()
#	window.bgcolor("white")
#	dheeraj = turtle.Turtle()
#	dheeraj.shape("arrow")
#	dheeraj.color("green")
#	dheeraj.circle(100)	
#	draw_traingle()	
#	
##	window = turtle.Screen()
#	window.bgcolor("white")
#	dheeraj = turtle.Turtle()
#	dheeraj.shape("circle")
# dheeraj.color("blue")
#	dheeraj.backward(100)
#	dheeraj.right(60)
#	dheeraj.forward(100)
#	dheeraj.left(120)
#	dheeraj.forward(100)
#	window.exitonclick()

	
draw_sqaure()
