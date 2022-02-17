import turtle, math, time, random

#-------screen and turtle creation----------------#
mywindow = turtle.Screen()
turtle.setup(700,700)
mywindow.bgcolor('black')
mywindow.title('Lunar Lander')

# ----------importing and setting up the map------# add extra maps over the weekend
map = []
mapFile = open('map.txt', 'r')
for line in mapFile:
 temp = line.strip('\n')
 temp = list(temp)
 map.append(temp)
mapFile.close()
for i in range(0, len(map), 1):
 for j in range(0, len(map[i]), 1):
     map[i][j] = int(map[i][j])
print()


#----------------------Player----------------------#
PlayerIcon = turtle.Turtle()
PlayerIcon.penup()
PlayerIcon.pencolor('white')
PlayerIcon.pensize(6)
PlayerIcon.color('white')
PlayerIcon.speed(0)
PlayerIcon.goto(300,300)
PlayerIcon.pendown()
PlayerIcon.goto(300,-300)
PlayerIcon.goto(-300,-300)
PlayerIcon.goto(-300,300)
PlayerIcon.goto(300,300)
PlayerIcon.penup()
PlayerIcon.goto(-290,200)
PlayerIcon.turtlesize(1,1)
PlayerIcon.setheading(0)
#---------------Tutorial Writer---------------#
tutorial = turtle.Turtle()
tutorial.hideturtle()
tutorial.penup()
tutorial.color('white')
tutorial.goto(-50,300)
#-------------------Thruster--------------------#
PlayerThruster = turtle.Turtle()
PlayerThruster.penup()
PlayerThruster.hideturtle()
PlayerThruster.turtlesize(0.2,0.2)
PlayerThruster.color('red')
#----------------------Score--------------------#
Score = turtle.Turtle()
Score.penup()
Score.hideturtle()
Score.color('white')
Score.speed(0)
Score.goto(250,315)
Points = 0
#-----------------speed writers---------------------#
HSwrite = turtle.Turtle()
HSwrite.penup()
HSwrite.hideturtle()
HSwrite.color('white')
HSwrite.speed(0)
HSwrite.goto(-300,325)

VSwrite = turtle.Turtle()
VSwrite.penup()
VSwrite.hideturtle()
VSwrite.color('white')
VSwrite.speed(0)
VSwrite.goto(-300,305)
#--------------------Announcer-----------------------#
Announcer  = turtle.Turtle()
Announcer.penup()
Announcer.hideturtle()
Announcer.color('white')
Announcer.speed(0)
Announcer.goto(-70,250)
#----------------Fuel and Writer--------------------#
Fuel = 10000
Fuelwrite = turtle.Turtle()
Fuelwrite.penup()
Fuelwrite.hideturtle()
Fuelwrite.color('white')
Fuelwrite.speed(0)
Fuelwrite.goto(-50,305)
#---------------------Gameover----------------------#
Gameover = turtle.Turtle()
Gameover.penup()
Gameover.hideturtle()
Gameover.color('white')
Gameover.speed(0)
Gameover.goto(-70,0)
#-------------------Functions-----------------------#
def thrust():
  global yVect, xVect, Fuel
  if yVect <= 1and Fuel > 0:
      Fuel -= 1
      PlayerThruster.showturtle()
      if PlayerIcon.heading() == 90:
          yVect += 0.02
      if PlayerIcon.heading() > 90 and PlayerIcon.heading() <= 100 and xVect < 1.5:
          xVect -= 0.0021
          yVect += 0.016
      if PlayerIcon.heading() > 100 and PlayerIcon.heading() <= 110 and xVect < 1.5:
          xVect -= 0.0047
          yVect += 0.01
      if PlayerIcon.heading() > 110 and PlayerIcon.heading() <= 120 and xVect < 1.5:
          xVect -= 0.0085
          yVect += 0.0085
      if PlayerIcon.heading() > 120 and PlayerIcon.heading() <= 130 and xVect < 1.5:
          xVect -= 0.013
          yVect += 0.0072
      if PlayerIcon.heading() > 130 and PlayerIcon.heading() <= 140 and xVect < 1.5:
          xVect -= 0.024
          yVect += 0.0057
      if PlayerIcon.heading() > 140 and PlayerIcon.heading() <= 150 and xVect < 1.5:
          xVect -= 0.037
          yVect += 0.0043
      if PlayerIcon.heading() > 150 and PlayerIcon.heading() <= 160 and xVect < 1.5:
          xVect -= 0.055
          yVect += 0.0024
      if PlayerIcon.heading() > 160 and PlayerIcon.heading() <= 170 and xVect < 1.5:
          xVect -= 0.08
          yVect += 0.0015
      if PlayerIcon.heading() > 170 and PlayerIcon.heading() <= 180 and xVect < 1.5:
          xVect -= 0.1
      if PlayerIcon.heading() < 90 and PlayerIcon.heading() >= 80 and xVect > -1.5:
          xVect += 0.0021
          yVect += 0.016
      if PlayerIcon.heading() < 80 and PlayerIcon.heading() >= 70 and xVect > -1.5:
          xVect += 0.0047
          yVect += 0.01
      if PlayerIcon.heading() < 70 and PlayerIcon.heading() >= 60 and xVect > -1.5:
          xVect += 0.0085
          yVect += 0.0085
      if PlayerIcon.heading() < 60 and PlayerIcon.heading() >= 50 and xVect > -1.5:
          xVect += 0.013
          yVect += 0.0072
      if PlayerIcon.heading() < 50 and PlayerIcon.heading() >= 40 and xVect > -1.5:
          xVect += 0.024
          yVect += 0.0057
      if PlayerIcon.heading() < 40 and PlayerIcon.heading() >= 30 and xVect > -1.5:
          xVect += 0.037
          yVect += 0.0043
      if PlayerIcon.heading() < 30 and PlayerIcon.heading() >= 20 and xVect > -1.5:
          xVect += 0.055
          yVect += 0.0024
      if PlayerIcon.heading() < 20 and PlayerIcon.heading() >= 10 and xVect > -1.5:
          xVect += 0.08
          yVect += 0.0015
      if PlayerIcon.heading() < 10 and PlayerIcon.heading() >= 0 and xVect > -1.5:
          xVect += 0.1
  return

def Begin():
    global StartUpSequence
    StartUpSequence = False
    return

def right():
   if PlayerIcon.heading() <= 180 and PlayerIcon.heading() > 0:
       PlayerIcon.right(5)
   return

def left():
   if PlayerIcon.heading() >= 0 and PlayerIcon.heading() < 180:
       PlayerIcon.left(5)
   return

def quit():
   global qFlag
   qFlag = True
   return

def edgeWrap(t,r):
   if t.xcor() > 360 + r or t.xcor() < -360 - r:
       t.hideturtle()
       t.setx(-1 * t.xcor())
       t.showturtle()
   return

def Crash(Land, LandRadius, Player, PlayerRadius):
      global  yVect, xVect, Fuel,qFlag
      dist = ((Land.xcor() - Player.xcor()) ** 2 + (Land.ycor() - Player.ycor()) ** 2) ** 0.5
      if dist < int(LandRadius) + int(PlayerRadius) and (PlayerIcon.heading() < 85 or PlayerIcon.heading() > 95) or (yVect < -0.6 and dist < int(LandRadius) + int(PlayerRadius)):
        FuelLoss = random.randint(2000,3000)
        w2 = 'CRASH LANDING -' + str(round(FuelLoss/10))
        Fuel -= FuelLoss
        Announcer.write(w2)
        time.sleep(2)
        Announcer.clear()
        if Fuel <= 0:
            Fuel = 0
            Gameover.write('GAMEOVER', font=('Arial', 20, 'normal'))
            qFlag = True
        PlayerIcon.goto(-300,200)
        PlayerIcon.setheading(0)
        yVect = 0
        xVect = 20
      return

def SafeLanding(Land, LandRadius, Player, PlayerRadius):
    global yVect, xVect, Points, Fuel, qFlag
    dist = ((Land.xcor() - Player.xcor()) ** 2 + (Land.ycor() - Player.ycor()) ** 2) ** 0.5
    if (dist < int(LandRadius) + int(PlayerRadius)) and PlayerIcon.heading() >= 85 and PlayerIcon.heading() <= 95 and yVect >= -0.8:
        if yVect < -0.4:
            w1 = 'ROUGH LANDING -50 FUEL'
            Announcer.write(w1)
            Fuel -= 500
        time.sleep(2)
        Announcer.clear()
        if Fuel <= 0:
            Fuel = 0
            Gameover.write('GAMEOVER', font=('Arial', 20, 'normal'))
            qFlag = True
        PlayerIcon.goto(-300,200)
        PlayerIcon.setheading(0)
        Points += 1
        yVect = 0
        xVect = 20
    return

def SafeLanding2(Land, LandRadius, Player, PlayerRadius):
    global yVect, xVect, Points, Fuel, qFlag
    dist = ((Land.xcor() - Player.xcor()) ** 2 + (Land.ycor() - Player.ycor()) ** 2) ** 0.5
    if (dist < int(LandRadius) + int(
            PlayerRadius)) and PlayerIcon.heading() >= 85 and PlayerIcon.heading() <= 95 and yVect >= -0.8:
        if yVect < -0.4:
            w1 = 'ROUGH LANDING -50 FUEL'
            Announcer.write(w1)
            Fuel -= 500
        time.sleep(2)
        Announcer.clear()
        if Fuel <= 0:
            Fuel = 0
            Gameover.write(Gameover.write('GAMEOVER', font=('Arial', 20, 'normal')))
            qFlag = True
        PlayerIcon.goto(-300, 200)
        PlayerIcon.setheading(0)
        Points += 2
        yVect = 0
        xVect = 20
    return

def SafeLanding3(Land, LandRadius, Player, PlayerRadius):
    global yVect, xVect, Points, Fuel, qFlag
    dist = ((Land.xcor() - Player.xcor()) ** 2 + (Land.ycor() - Player.ycor()) ** 2) ** 0.5
    if (dist < int(LandRadius) + int(
            PlayerRadius)) and PlayerIcon.heading() >= 85 and PlayerIcon.heading() <= 95 and yVect >= -0.8:
        if yVect < -0.4:
            w1 = 'ROUGH LANDING -50 FUEL'
            Announcer.write(w1)
            Fuel -= 500
        time.sleep(2)
        Announcer.clear()
        if Fuel <= 0:
            Fuel = 0
            Gameover.write(Gameover.write('GAMEOVER', font=('Arial', 20, 'normal')))
            qFlag = True
        PlayerIcon.goto(-300, 200)
        PlayerIcon.setheading(0)
        Points += 3
        yVect = 0
        xVect = 20
    return

def SafeLanding4(Land, LandRadius, Player, PlayerRadius):
    global yVect, xVect, Points, Fuel, qFlag
    dist = ((Land.xcor() - Player.xcor()) ** 2 + (Land.ycor() - Player.ycor()) ** 2) ** 0.5
    if (dist < int(LandRadius) + int(
            PlayerRadius)) and PlayerIcon.heading() >= 85 and PlayerIcon.heading() <= 95 and yVect >= -0.8:
        if yVect < -0.4:
            w1 = 'ROUGH LANDING -50 FUEL'
            Announcer.write(w1)
            Fuel -= 500
        time.sleep(2)
        Announcer.clear()
        if Fuel <= 0:
            Fuel = 0
            Gameover.write(Gameover.write('GAMEOVER', font=('Arial', 20, 'normal')))
            qFlag = True
        PlayerIcon.goto(-300, 200)
        PlayerIcon.setheading(0)
        Points += 4
        yVect = 0
        xVect = 20
    return

mywindow.listen()
mywindow.onkeypress(thrust,'Up')
mywindow.onkeypress(right, 'Right')
mywindow.onkeypress(left, 'Left')
mywindow.onkey(Begin, 'space')
mywindow.onkey(quit,'q')

#-----------------Tutorial Startup---------------------#
turtorial = True
tutorial.goto(-140,255)
tutorial.write("LUNAR LANDER", font=("Arial",22,"normal"))
tutorial.goto(-200,210)
tutorial.write("Controls", font=("Arial",14,"normal"))
tutorial.goto(-180,195)
tutorial.write("\'<-\' and \'->\' keys to adjust the heading of space ship")
tutorial.goto(-180,180)
tutorial.write("\'↑\' key to apply thrusters")
tutorial.goto(-200,75)
tutorial.write("How To Play", font=("Arial",14,"normal"))
tutorial.goto(-180,60)
tutorial.write("- Navigate your spaceship to land safely")
tutorial.goto(-180,45)
tutorial.write("on the moon below")
tutorial.goto(-180,30)
tutorial.write("- To ensure a smooth landing, land with controlled speed")
tutorial.goto(-180,15)
tutorial.write("- Land your spaceship pointing upward")
tutorial.goto(-200,-85)
tutorial.write("Bonus", font=("Arial",14,"normal"))
tutorial.goto(-180,-100)
tutorial.write("- You may land on any surface of the map")
tutorial.goto(-180,-115)
tutorial.write("- Coloured land awards additional points! (2,3,4)")

tutorial.goto(-110, -200)
spce = "Press SpaceBar To Begin"
tutorial.write(spce, font=("Arial",14,"normal"))
StartUpSequence = True
while StartUpSequence == True:
    tutorial.goto(0,0)
#-----------------Lunar Land---------------------#
LandSpots = []
LandIndex = -1
LandSizes = []
LandMult2 = []
LandIndex2 = -1
LandSizes2 = []
LandMult3 = []
LandIndex3 = -1
LandSizes3 = []
LandMult4 = []
LandIndex4 = -1
LandSizes4 = []
# ---------------drawing the grid----------------#
gridSquare = turtle.Turtle()
gridSquare.speed(0)
gridSquare.penup()
gridSquare.shape('square')
gridSquare.turtlesize(1, 1)
gridSquare.fillcolor('black')
mywindow.tracer(0, 0)

for i in range(0, 29, 1):  # our row counter
 for j in range(0, 29, 1):  # columns
     x = int(20 * (j - 14))
     y = int(20 * (14 - i))
     gridSquare.goto(x, y)
     if map[i][j] == 0:
         gridSquare.fillcolor('black')
         gridSquare.stamp()
     if map[i][j] == 1:
         gridSquare.fillcolor('white')
         gridSquare.stamp()
         LandIndex += 1
         LandSpots.append(turtle.Turtle())
         LandSpots[LandIndex].speed(0)
         LandSpots[LandIndex].hideturtle()
         LandSpots[LandIndex].shape('square')
         LandSpots[LandIndex].penup()
         LandSize = 10
         LandSizes.append(LandSize)
         LandSpots[LandIndex].turtlesize(LandSize / 10, LandSize / 10)
         LandSpots[LandIndex].goto(x,y)
     if map[i][j] == 2:
         gridSquare.fillcolor('#567ca9')
         gridSquare.stamp()
         LandIndex2 += 1
         LandMult2.append(turtle.Turtle())
         LandMult2[LandIndex2].speed(0)
         LandMult2[LandIndex2].hideturtle()
         LandMult2[LandIndex2].shape('square')
         LandMult2[LandIndex2].penup()
         LandSize2 = 10
         LandSizes2.append(LandSize2)
         LandMult2[LandIndex2].turtlesize(LandSize2 / 10, LandSize2 / 10)
         LandMult2[LandIndex2].goto(x,y)
     if map[i][j] == 3:
         gridSquare.fillcolor('#575caa')
         gridSquare.stamp()
         LandIndex3 += 1
         LandMult3.append(turtle.Turtle())
         LandMult3[LandIndex3].speed(0)
         LandMult3[LandIndex3].hideturtle()
         LandMult3[LandIndex3].shape('square')
         LandMult3[LandIndex3].penup()
         LandSize3 = 10
         LandSizes3.append(LandSize3)
         LandMult3[LandIndex3].turtlesize(LandSize3 / 10, LandSize3 / 10)
         LandMult3[LandIndex3].goto(x,y)
     if map[i][j] == 4:
         gridSquare.fillcolor('#2d1663')
         gridSquare.stamp()
         LandIndex4 += 1
         LandMult4.append(turtle.Turtle())
         LandMult4[LandIndex4].speed(0)
         LandMult4[LandIndex4].hideturtle()
         LandMult4[LandIndex4].shape('square')
         LandMult4[LandIndex4].penup()
         LandSize4 = 10
         LandSizes4.append(LandSize4)
         LandMult4[LandIndex4].turtlesize(LandSize4 / 10, LandSize4 / 10)
         LandMult4[LandIndex4].goto(x,y)
     gridSquare.stamp()
 mywindow.update()

#---------------------------------------------------------------
yVect = 0
xVect = 20

#-------------------frame rate definition----------------
FPS = 60
refreshEvery = 1/FPS
startofInterval = time.clock()
mywindow.tracer(0,0)
qFlag = False
while qFlag == False:
    endofInterval = time.clock()
    if endofInterval - startofInterval >= refreshEvery:
        PlayerThruster.goto(PlayerIcon.xcor(),PlayerIcon.ycor())
        PlayerThruster.setheading(PlayerIcon.heading())
        PlayerThruster.hideturtle()
        if yVect >= -1.2:
              yVect -= 0.01
        if xVect > 1.5:
            xVectNew = xVect*0.9
            xVect = xVectNew
            xVect -= 0.00075
        if xVect > 0:
            xVect -= 0.00075
        if xVect < -1.5:
            xVectNew = xVect * 0.9
            xVect = xVectNew
            xVect += 0.00075
        if xVect < 0:
            xVect += 0.00075
        for i in range(0,LandIndex,1):
             Crash(LandSpots[i], LandSizes[i], PlayerIcon, 12)
             SafeLanding(LandSpots[i], LandSizes[i], PlayerIcon, 12)
        for i in range(0,LandIndex2,1):
             Crash(LandMult2[i], LandSizes2[i], PlayerIcon, 12)
             SafeLanding2(LandMult2[i], LandSizes2[i], PlayerIcon, 12)
        for i in range(0,LandIndex3,1):
             Crash(LandMult3[i], LandSizes3[i], PlayerIcon, 12)
             SafeLanding3(LandMult3[i], LandSizes3[i], PlayerIcon, 12)
        for i in range(0,LandIndex4,1):
             Crash(LandMult4[i], LandSizes4[i], PlayerIcon, 12)
             SafeLanding4(LandMult4[i], LandSizes4[i], PlayerIcon, 12)
        HSwrite.clear()
        s = 'Horizontal Speed: ' + str(round(xVect*10,1))
        HSwrite.write(s)
        VSwrite.clear()
        s2 = 'Vertical Speed: ' + str(round(yVect*10))
        VSwrite.write(s2)
        Score.clear()
        NewScore = 'Score: ' + str(Points)
        Score.write(NewScore)
        Fuelwrite.clear()
        s3 = 'Fuel ' + str(round(Fuel/10))
        Fuelwrite.write(s3)
        PlayerIcon.sety(PlayerIcon.ycor() + yVect)
        PlayerIcon.setx(PlayerIcon.xcor() + xVect)
        edgeWrap(PlayerIcon, 20)
        mywindow.update()
        startofInterval = time.clock()
while qFlag == True:
    xVect = 2
    PlayerIcon.setx(PlayerIcon.xcor() + xVect)
    edgeWrap(PlayerIcon, 20)
    Gameover.write('GAMEOVER', font=('Arial', 20, 'normal'))
    mywindow.update()
#-------close window-------------------------------
mywindow.bye()