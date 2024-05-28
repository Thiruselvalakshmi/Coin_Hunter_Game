import turtle
import random
sea=turtle.Screen()
sea.bgpic("D:\MY DETAILS (THIRU)\LMES\game3\Sea.gif")
sea.setup(650,650)
sea.addshape("D:\MY DETAILS (THIRU)\LMES\game3\Coin.gif")
sea.addshape("D:\MY DETAILS (THIRU)\LMES\game3\lft.gif")
sea.addshape("D:\MY DETAILS (THIRU)\LMES\game3\Rgt.gif")
sea.title("~$~$~$~COIN HUNTER~$~$~$~")
chances=3
hunter=turtle.Turtle()
hunter.shape("D:\MY DETAILS (THIRU)\LMES\game3\lft.gif")
hunter.penup()
hunter.goto(-100,-150)

coin=turtle.Turtle()
coin.shape("D:\MY DETAILS (THIRU)\LMES\game3\Coin.gif")
coin.speed(1000)
coin.penup()
coin.goto(-280,280)

scoreboard=turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-100,200)
scoreboard.write("Score : 0",font=("Courier",25,"bold"))
score=0

chances=turtle.Turtle()
chances.hideturtle()
chances.penup()
chances.goto(-100,240)
chances.write("Chances : 3",font=("Courier",25,"bold"))
chance = 3
def right():
    hunter.shape("D:\MY DETAILS (THIRU)\LMES\game3\Rgt.gif")
    hunter.forward(5)

def left():
    hunter.shape("D:\MY DETAILS (THIRU)\LMES\game3\lft.gif")
    hunter.backward(5)

turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()
def move():
        y=coin.ycor()
        y-=2
        coin.sety(y)
        
while True:
    sea.update()
    move()
    if coin.ycor() < -280:
        chance-=1
        chances.clear()
        chances.write("Chances : {}".format(chance),font=("Courier",25,"bold"))
        if chance == 0:
             chances.clear()
             chances.goto(-240,240)
             chances.write("Sorry!!! You lost",font=("Courier",35,"bold"))
             break
             #exit(0)
        x=random.randint(-280,280)
        coin.goto(x,280)
    if coin.distance(hunter) < 50:
         scoreboard.clear()
         score=score + 1
         scoreboard.write("Score : {}".format(score),font=("Courier",25,"bold"))
         x=random.randint(-280,280)
         coin.goto(x,280)
    

turtle.done()

