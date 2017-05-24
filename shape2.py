import turtle
def draw_flower():
		flower=turtle.Turtle()
		window = turtle.Screen()
		window.bgcolor("white")
		flower.shape("turtle")
		flower.color("red")
		flower.speed(0)
		for x in range(1,61):
			flower.left(45)
			flower.forward(100)
			flower.right(45)
			flower.forward(100)
			flower.right(135)
			flower.forward(100)
			flower.right(45)
			flower.forward(100)
			flower.right(138)
		flower.right(90)	
		flower.forward(500)	
					
		
		

	
		window.exitonclick()

draw_flower()		
		

