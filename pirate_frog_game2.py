import turtle as t
def turn_up():
    player.left(2)
def turn_down():
    player.right(2)
def fire():
    ang = player.heading()
    while(1):
        player.shape("arrow")
        player.forward(15)
        if ang>=0 and ang<=90:
            player.right(5)
        else:
            player.left(5)
        if(player.distance(floor1)<50 and player.ycor() - floor1.ycor() <5 ):
            player.shape("turtle")
            break
        if(player.distance(floor2)<50 and player.ycor() - floor2.ycor() <5 ):
            player.shape("turtle")
            break
        if(player.distance(floor3)<50 and player.ycor() - floor3.ycor() <5 ):
            player.shape("turtle")
            break 
        elif(player.ycor()<-500):
            player.goto(startpoint())
            player.setheading(ang)
            player.shape("turtle")
            break
        if player.distance(coin)<20:
            sc.clear()
            player.goto(startpoint())
            break
        
            
            
def startpoint():

    return (-351,-350)
    #return (350,-350)


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
player.setheading(90)
player.color("green")
player.goto(startpoint())

#stage1 floor 3개만 사용
floor1 = t.Turtle()
floor1.shape("square")
floor1.pensize(5)
floor1.up()#
floor1.goto(-400,-350)
floor1.down()
floor1.goto(-300,-350)

floor1.up()#
floor1.goto(-150,-350)
floor1.down()

floor2 = t.Turtle()
floor2.shape("square")
floor2.up()#
floor2.goto(150,-350)
floor2.down()

floor3 = t.Turtle()
floor3.shape("square")
floor3.up()#
floor3.goto(350,-350)
floor3.down()

coin = t.Turtle()
coin.shape("circle")
coin.color("Yellow")
coin.penup()
coin.goto(floor3.xcor(),floor3.ycor()+20)




t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")
t.listen()
