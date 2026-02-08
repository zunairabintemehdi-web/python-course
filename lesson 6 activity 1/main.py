import turtle

turtle.Screen().bgcolor("Pink")

sc=turtle.Screen()
sc.setup(500,500)

turtle.title("turtle window is welcoming you")

board=turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)