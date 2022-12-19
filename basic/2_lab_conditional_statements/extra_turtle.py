import math
import turtle

animation = turtle.Turtle()
animation.color("Green")
animation.speed(100)
animation.shape("turtle")

animation.begin_fill()

for i in range(1000):
    animation.forward(25)
    animation.left(math.pi)
    animation.left(5)

animation.end_fill()
turtle.mainloop()
