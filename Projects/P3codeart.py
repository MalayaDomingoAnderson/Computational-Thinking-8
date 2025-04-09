#start
import turtle

t = turtle.Turtle()

#color
t.color("pink")
turtle.Screen().bgcolor("navy blue")

t.goto(100, 0)
t.color("cyan")

for i in range(5):
    t.forward(100)
    t.left(72)


#color changing shape
colors = ["pink","light blue","light pink"]
for i in range ( 100 ):
    t.color(colors[i%3])
    t.forward(100)
    t.left(72)
#end

turtle.exitonclick()