import turtle as t
import random
timmy = t.Turtle()
screen = t.Screen()
screen.setup(width=500,height=400)
userbet = screen.textinput(title="Make Your bet!",prompt="which turtle gonna win!:")
colorlst = ["red","green","yellow","blue","brown","purple"]
timmy.penup()
count = 180
turtlelst = []
for i in colorlst:
    timmy = t.Turtle(shape="turtle")
    timmy.penup()
    timmy.color(i)
    timmy.goto(x=-230,y=count)
    count = count -60
    turtlelst.append(timmy)

if userbet:
    flag = True
    while flag:
        
        for i in turtlelst:
            speed = random.randint(1,10)
            i.penup()
            i.forward(speed)
            if i.xcor() > 230:
                flag = False
                if userbet == i.pencolor():
                    print("You Won. The",i.pencolor(),"won")
                else:
                    print("You Lost. The",i.pencolor(),"won")






screen.exitonclick()