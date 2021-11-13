import turtle as t

score = 0
def turn_up():
    player.left(5)
    ex.left(5)
def turn_down():
    player.right(5)
    ex.right(5)
def fire():
    global score
    ang = player.heading()
    while(1):
        
        player.forward(15)
        
        if player.distance(coin)<40:
            score+=1
            play()
            break

        if(player.distance(floor1)<50 and player.ycor()>floor1.ycor()and player.ycor() - floor1.ycor()<40):
            player.shape(frog_img1)
            player.setheading(ang)
            ex.setheading(player.heading())
            ex.goto(expoint())
            break           
        if(player.distance(floor2)<50 and player.ycor()>floor2.ycor()and player.ycor() - floor2.ycor()<40):
            player.shape(frog_img1)
            player.setheading(ang)
            ex.setheading(player.heading())
            ex.goto(expoint())    
            break
        if(player.distance(floor3)<50 and player.ycor()>floor2.ycor()and player.ycor() - floor3.ycor()<40):
            player.shape(frog_img1)
            player.setheading(ang)
            ex.setheading(player.heading())
            ex.goto(expoint())            
            break
        if(player.distance(floor4)<50 and player.ycor()>floor2.ycor()and player.ycor() - floor4.ycor()<40):
            player.shape(frog_img1)
            player.setheading(ang)
            ex.setheading(player.heading())
            ex.goto(expoint())
            break
        if(player.distance(floor5)<50 and player.ycor()>floor2.ycor()and player.ycor() - floor5.ycor()<40):
            player.shape(frog_img1)
            player.setheading(ang)
            ex.setheading(player.heading())
            ex.goto(expoint())
            break 
        if(player.ycor()<-500):
            player.goto(startpoint())
            player.setheading(ang)
            player.shape(frog_img1)
            ex.setheading(ang)
            ex.goto(expoint())
            break
        if player.distance(spike)<50:
            player.goto(startpoint())
            player.setheading(ang)
            player.shape(frog_img1)
            ex.setheading(ang)
            ex.goto(expoint())
            break
        if player.heading()>271 and player.heading() <300:
            player.setheading(270)
            player.forward(500)
        elif ang>=0 and ang<=90:
            player.shape(frog_img2)
            player.right(5)
        elif ang>90 and ang<=180:
            player.shape(frog_img3)
            player.left(5)


def startpoint():
    return (-350,-300)
    #return (350,-350)
def expoint():
    return (player.xcor()+50,player.ycor()+50)

def play():
    global score
    player.shape(frog_img1)
    player.goto(startpoint())
    player.setheading(0)
    ex.goto(expoint())
    ex.setheading(player.heading())
    if score==0:
        stage2()
    elif score == 1:
        stage2()
    elif score == 2:
        stage3()
    elif score == 3:
        thx()

    
    

    
sc = t.Screen()
sc.setup(1000,1000)
sc.title("Pirate_Frog")
frog_img1 = 'frog1.gif'
frog_img2 = 'frog2.gif'
frog_img3 = 'frog3.gif'
floor_img = 'floor.gif'
spike_img = 'bomb.gif'
coin_img = 'box.gif'
sc.addshape(frog_img1)
sc.addshape(frog_img2)
sc.addshape(frog_img3)
sc.addshape(floor_img)
sc.addshape(spike_img)
sc.addshape(coin_img)


player = t.Turtle()#플레이어
player.shape(frog_img1)
player.up()
player.setheading(0)
player.color("green")
player.goto(startpoint())

ex = t.Turtle()
ex.shape("turtle")
ex.up()
ex.setheading(0)
ex.goto(expoint())


floor1 = t.Turtle()#바닥, 오브젝트설정
floor1.shape(floor_img)
floor2 = t.Turtle()
floor2.shape(floor_img)
floor2.up()
floor3 = t.Turtle()
floor3.shape(floor_img)
floor3.up()
floor4 = t.Turtle()
floor4.shape(floor_img)
floor4.up()
floor5 = t.Turtle()
floor5.shape(floor_img)
floor5.up()
coin = t.Turtle()
coin.shape(coin_img)
coin.penup()

spike = t.Turtle()
spike.shape(spike_img)
spike.up()


#stage1 floor 3개만 사용
#stage1
def stage1():
    
    floor1.pensize(5)
    floor1.up()
    floor1.goto(-400,-350)
    floor1.down()
    floor1.goto(-300,-350)

    floor1.up()
    floor1.goto(-150,-350)   
    
    floor2.goto(150,-350)
    
    floor3.goto(350,-350)

    floor4.ht()
    floor5.ht()
    spike.ht()
    coin.goto(floor3.xcor(),floor3.ycor()+55)

        

#stage2
def stage2():
    floor1.pensize(5)
    floor1.up()#
    floor1.goto(-400,-350)
    floor1.down()
    floor1.goto(-300,-350)

    floor1.up()#
    floor1.goto(-200,-250)

    floor2.goto(0,-170)

    floor3.goto(200,-200)

    floor4.st()
    floor4.goto(350,-100)

    floor5.ht()

    spike.st()
    spike.goto(200,-25)

    coin.goto(floor4.xcor(),floor4.ycor()+55)

def stage3():
    floor1.pensize(5)
    floor1.up()#
    floor1.goto(-400,-350)
    floor1.down()
    floor1.goto(-300,-350)

    floor1.up()
    floor1.goto(-50,-250)

    floor2.goto(150,-100)

    floor3.goto(0,70)

    floor4.goto(-200,200)

    floor5.st()
    floor5.goto(0,300)

    coin.goto(floor5.xcor(),floor5.ycor()+55)
    
    spike.goto(-100,300)


def thx():
    floor1.ht()
    floor2.ht()
    floor3.ht()
    floor4.ht()
    floor5.ht()
    spike.ht()
    coin.ht()
    ex.ht()
    player.goto(0,0)
    t.ht()
    t.up()
    t.goto(0,50)
    t.color("green")
    t.write("플레이해주셔서 감사하다옳",font=("Consolas", 20))
play()





t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.onkeypress(fire,"space")
t.listen()
