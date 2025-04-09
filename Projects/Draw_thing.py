import turtle

t = turtle.Turtle()

t.goto(0,0)
t.color("blue") #color

turtle.Screen() .bgcolor("black")

t.speed(0)

colors = ["blue", "green","purple"]
#repeat
for i in range(138) :
    t.color(colors[i%3])
    t.forward(-33 + i)
    t.left(-35 + 1)
    t.pendown

t.penup
t.goto(12,9)
colors = ["blue", "green","purple"]
#repeat
for i in range(138) :
    t.color(colors[i%3])
    t.forward(-33 + i)
    t.left(-35 + 1)
    t.pendown

t.penup
t.goto(54,92)

colors = ["blue", "green","purple"]
#repeat
for i in range(138) :
    t.color(colors[i%3])
    t.forward(-33 + i)
    t.left(-35 + 1)
    t.pendown

t.penup
t.goto(24,67)

colors = ["blue", "green","purple"]
#repeat
for i in range(138) :
    t.color(colors[i%3])
    t.forward(-33 + i)
    t.left(-35 + 1)
    t.pendown

t.penup
t.goto(85,45)

colors = ["blue", "green","purple"]
#repeat
for i in range(138) :
    t.color(colors[i%3])
    t.forward(-33 + i)
    t.left(-35 + 1)
    t.pendown

t.penup
t.goto(100,32)

colors = ["blue", "green","purple"]
#repeat
for i in range(138) :
    t.color(colors[i%3])
    t.forward(-33 + i)
    t.left(-35 + 1)
    t.pendown

t.penup
t.goto(-185,-72)

colors = ["blue", "green","purple"]
#repeat
for i in range(138) :
    t.color(colors[i%3])
    t.forward(-33 + i)
    t.left(-35 + 1)
    t.pendown

    # Move the turtle to the starting positionpen.penup()
t.goto(0, -200)
t.pendown()

# write the text
t.write("vote for me for a cookie", align="center", font=("Arial", 30, "bold"))

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
#leaves when you click
turtle .exitonclick()