# The sky is falling
# By SuperCoding
# Python 3.8.5
# Mac os

import turtle
import random

Score = 0
Lives = 3

wn = turtle.Screen()
wn.bgcolor('green')
wn.title('by super coding')
wn.setup(width=800, height=600)
wn.tracer(0)




player = turtle.Turtle()
player.penup()
player.speed(0)
player.shape('circle')
player.shapesize(1.5)
player.color('blue')
player.goto(0, -250)





enemy = turtle.Turtle()
enemy.penup()
enemy.speed(0)
enemy.shape('circle')
enemy.color('red')
enemy.fd(150)
enemy.speed = (random.randint(1,4))
enemys.append(enemy)




power_up = turtle.Turtle()
power_up.penup()
power_up.speed(0)
power_up.shape('circle')
power_up.color('yellow')
power_up.backward(150)
power_up.speed = (random.randint(1,4))
powers_ups.append(power_up)








   
   

      










wn.mainloop()
