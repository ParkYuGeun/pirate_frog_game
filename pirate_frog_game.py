import turtle as t
def turn_up():
    player.left(2)
def turn_down():
    player.right(2)
def fire():
    ang = player.heading()
    while(1):
        player.shape("arrow")
        player.forward(25)
        player.right(5)
        if(player.distance(floor)<50 and player.ycor() - floor.ycor() <5 ):
            player.shape("turtle")
            break
        elif(player.ycor()<-500):
            player.goto(startpoint())
            player.setheading(ang)
            player.shape("turtle")
            break

def startpoint():
    return (-351,-350)


sc = t.Screen()
sc.setup(1000,1000)
sc.title("Pirate_Frog")
frog_img1 = 'frog1.gif'
frog_img2 = 'frog2.gif'
floor_img = 'floor.gif'
sc.addshape(frog_img1)
sc.addshape(frog_img2)
sc.addshape(floor_img)


player = t.Turtle()
# player.shape(frog_img1) 개구리 사진 크기 줄이고 다시 활성화
player.up()
player.goto(startpoint())

floor = t.Turtle()
#floor.ht()
floor.shape("square")
floor.pensize(5)
floor.up()#
floor.goto(-400,-350)
floor.down()
floor.goto(-300,-350)

target = -150
floor.up()#
floor.goto(target,-350)
floor.down()





coin = t.Turtle()
coin.shape("circle")
coin.color("Yellow")



t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")
t.listen()
