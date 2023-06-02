from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setpos(x, 0)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
