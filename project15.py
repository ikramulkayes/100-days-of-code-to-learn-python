###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import os
import turtle as t
import random
path = 'F:\\Github\\100-days-of-code-to-learn-python'
os.chdir(path)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    ncolor = (r,g,b)
    rgb_colors.append(ncolor)

#print(rgb_colors)

t.colormode(255)
timmy = t.Turtle()
screen = t.Screen()
count = 0
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(400)
timmy.setheading(0)

for i in range(10+1):
    if count !=0:
        timmy.penup()
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        
        timmy.forward(500)
        timmy.setheading(0)
    for i in range(10):
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.color(random.choice(rgb_colors))
        timmy.dot(20)
        count += 1
screen.exitonclick()


