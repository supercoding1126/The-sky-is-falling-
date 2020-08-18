import turtle
import random
import time

Score = 0
Lives = 3

falling = True
game = True




wn = turtle.Screen()
wn.bgcolor('green')
wn.title('by super coding')
wn.bgpic('/Users/shining/Desktop/space1.gif')
wn.setup(width=800, height=600)
wn.tracer(0)




turtle.addshape('/Users/shining/Desktop/rocket1.gif')
turtle.addshape('/Users/shining/Desktop/rock.gif')
turtle.addshape('/Users/shining/Desktop/gas.gif')


player = turtle.Turtle()
player.penup()
player.speed(0)
player.shape('/Users/shining/Desktop/rocket1.gif')
player.shapesize(1.5)
player.color('blue')
player.goto(0, -250)
player.direction = 'stop'



enemys = []

for x in range(10):
   enemy = turtle.Turtle()
   enemy.penup()
   enemy.speed(0)
   enemy.shape('/Users/shining/Desktop/rock.gif')
   enemy.color('red')
   enemy.fd(150)
   enemy.speed = (random.randint(1,4))
   enemys.append(enemy)



powers_ups = []

for x in range(10):
   power_up = turtle.Turtle()
   power_up.penup()
   power_up.speed(0)
   power_up.shape('/Users/shining/Desktop/gas.gif')
   power_up.color('yellow')
   power_up.backward(150)
   power_up.speed = (random.randint(1,4))
   powers_ups.append(power_up)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.color('red')
pen.goto(0, 260)
pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))





def left():
   player.direction = "left"


def right():
   player.direction = "right"




wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while game == True:
   while falling == True:
      wn.update()



      if player.direction == "left":
         player.setx(player.xcor() - 3)
         
      if player.direction == "right":
         player.setx(player.xcor() + 3)


      for power_up in powers_ups:
         power_up.sety(power_up.ycor() - power_up.speed)

         if power_up.ycor() < -300:
            power_up.goto(random.randint(-300, 300), random.randint(400, 800))

         if player.distance(power_up) < 40:
            Score += 10
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(Score, Lives), align="center", font=("Courier", 24, "normal"))
            power_up.goto(random.randint(-300, 300), random.randint(400, 800))

      for enemy in enemys:
         enemy.sety(enemy.ycor() - enemy.speed)


         if player.distance(enemy) < 40:
            Score -= 10
            Lives -= 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(Score, Lives), align="center", font=("Courier", 24, "normal"))
            enemy.goto(random.randint(-300, 300), random.randint(400, 800))


         if enemy.ycor() < -300:
            enemy.goto(random.randint(-300, 300), random.randint(400, 800))








      if player.xcor() < -390:
            player.setx(-390)

      if Lives <= 0:
         pen.clear()
         pen.write("Game Over your score: {}".format(Score), align="center", font=("Courier", 24, "normal"))
         time.sleep(5)
         falling = False
   Score = 0
   Lives = 3

   player.goto(0, -250)
   player.direction = 'Stop'
   pen.clear()
   pen.write("Score: {}  Lives: {}".format(Score, Lives), align="center", font=("Courier", 24, "normal"))
   falling = True

























wn.mainloop()