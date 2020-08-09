import turtle
import random

Score =  

wn = turtle.Screen()
wn.bgcolor('green')
wn.title('by super coding')
wn.tracer(0)



player = turtle.Turtle()
player.penup()
player.speed(0)
player.shape('circle')
player.shapesize(1.5)
player.color('blue')
player.goto(0, -250)
player.direction = 'stop'



enemys = []

for x in range(10):
   enemy = turtle.Turtle()
   enemy.penup()
   enemy.speed(0)
   enemy.shape('circle')
   enemy.color('red')
   enemy.fd(150)
   enemy.speed(random.randint(1,4))
   enemys.append(enemy)



powers_ups = []

for x in range(10):
   power_up = turtle.Turtle()
   power_up.penup()
   power_up.speed(0)
   power_up.shape('circle')
   power_up.color('yellow')
   power_up.backward(150)
   power_up.speed(random.randint(1,4))
   powers_ups.append(power_up)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))





def left():
    player.direction = "left"

    
def right():
    player.direction = "right"


    

wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
   wn.update()


   if player.direction == "left":
      player.setx(player.xcor() - 3)
    
   if player.direction == "right":
      player.setx(player.xcor() + 3)









wn.mainloop()import turtle
import random

Score =  

wn = turtle.Screen()
wn.bgcolor('green')
wn.title('by super coding')
wn.tracer(0)



player = turtle.Turtle()
player.penup()
player.speed(0)
player.shape('circle')
player.shapesize(1.5)
player.color('blue')
player.goto(0, -250)
player.direction = 'stop'



enemys = []

for x in range(10):
   enemy = turtle.Turtle()
   enemy.penup()
   enemy.speed(0)
   enemy.shape('circle')
   enemy.color('red')
   enemy.fd(150)
   enemy.speed(random.randint(1,4))
   enemys.append(enemy)



powers_ups = []

for x in range(10):
   power_up = turtle.Turtle()
   power_up.penup()
   power_up.speed(0)
   power_up.shape('circle')
   power_up.color('yellow')
   power_up.backward(150)
   power_up.speed(random.randint(1,4))
   powers_ups.append(power_up)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))





def left():
    player.direction = "left"

    
def right():
    player.direction = "right"


    

wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
   wn.update()


   if player.direction == "left":
      player.setx(player.xcor() - 3)
    
   if player.direction == "right":
      player.setx(player.xcor() + 3)









wn.mainloop()