from gamelib import *
game = Game(800,600,"Tag or Get Tagged")

bk = Image("images/background1.png",game)
bk.resizeTo(game.width,game.height)

game.setBackground(bk)
game.drawText("Timer",10,5)

Luigi = Animation("images/Luigi.png", 8, game, 1000/5, 600/2, 1)
Luigi.resizeBy(-65)
Luigi.moveTo(60,570)

def positionObjects( objects ):
    for i in range(len(objects)):
        x = randint(100,700)
        y = -randint(100, 5000) #Note: negative randint
        objects[i].moveTo(x, y)
        s = randint(4, 8)
        objects[i].setSpeed(s, 180)
        objects[i].visible = True

rainbowpower= []
for i in range(1):
    r = Animation("images/rainbow star.png", 8, game, 1800/8, 200, 1)
    r.resizeBy(-75)
    rainbowpower.append(r)
positionObjects(rainbowpower)

portal1=Animation("images/netherportal1.png",32,game, 1800/9,800/5,1)
portal2=Animation("images/netherportal1.png",32,game, 1800/9,800/5,1)

mariomusic = Sound("sounds/04. Super Mario 1991.mp3",0)

Mario = Animation("images/Mario.png",8,game, 336/8, 40, 1)
Mario.moveTo(30,570)

play = Image("images/play.png",game)
play.resizeBy(-22)

story = Image("Images/story.png",game)
story.resizeBy(-22)
tagorgettagged = Image("images/Tag or get Tagged.png",game)
tagorgettagged.resizeBy(-35)

bullet = Animation("images/plasmaball1.png", 11, game, 32,  32)

howtoplay = Image("images/howtoplay.png",game)
howtoplay.resizeBy(-25)

howtoplayimage = Image("images/howtoplayimage.png",game)
howtoplayimage.resizeTo(game.width, game.height)
howtoplayimage.visible = False



storyimage = Image("images/storyimage.png",game)
storyimage.visible = False
storyimage.resizeTo(game.width, game.height)

portal1.visible = True
portal2.visible = True

portal1.resizeBy(-50)
portal2.resizeBy(-50)

platform = Image("images/platform.png",game)
platform.x= game.width
platform.resizeBy(79)
platform.moveTo(400,555)

platformmario1 = Image("images/platformMario.jpeg",game)

platformmario2 = Image("images/platformMario.jpeg",game)
platformmario3 = Image("images/platformMario.jpeg",game)
platformmario1.resizeBy(-25)
platformmario2.resizeBy(-25)
platformmario3.resizeBy(-25)
platformmario1.moveTo(125,400)
platformmario2.moveTo(670,400)

def LuigiMindset():
  Luigi.draw()
  if keys.Pressed[K_LEFT]:
      Luigi.x -= 5
  if keys.Pressed[K_RIGHT]:
      Luigi.x += 5
  if keys.Pressed[K_UP]:
      Luigi.y -= 5
  if keys.Pressed[K_DOWN]:
      Luigi.y += 5


        
def MarioMindset():
  Mario.draw()
  if keys.Pressed[K_w]:
    Mario.y-=5
  if keys.Pressed[K_s]:
    Mario.y+=5
  if keys.Pressed[K_a]:
    Mario.x-=5
  if keys.Pressed[K_d]:
    Mario.x+=5

while not game.over:
  game.processInput()
  game.scrollBackground("left",4)
  bullet.moveTo(mouse.x, mouse.y)
  howtoplay.moveTo(400,318)
  play.moveTo(400,490)
  story.moveTo(400,400)
  tagorgettagged.moveTo(400,180)
  howtoplayimage.draw()



  mariomusic.play()
  
  storyimage.draw()

  if bullet.collidedWith(story, "rectangle") and mouse.LeftClick:
    storyimage.visible = True

  if bullet.collidedWith(howtoplay, "rectangle") and mouse.LeftClick:
    howtoplayimage.visible = True

  if keys.Pressed[K_SPACE]:
    storyimage.visible = False
    howtoplayimage.visible = False


  if bullet.collidedWith(play, "rectangle") and mouse.LeftClick:
    game.over = True
  game.update(30)

game.over=False

while not game.over:
  game.processInput()
  game.scrollBackground("left",4)
  positionObjects(rainbowpower)



  portal1.y=100
  portal1.x=100

  c=850
  d=200

  portal2.y=C
  portal2.x=d

  if Mario.collidedWith(portal1):
    Mario.x=C
    Mario.y=d

  if Luigi.collidedWith(portal1):
    Luigi.x=C
    Luigi.y=d






  platform.draw()
  
  platformmario1.draw()
  platformmario2.draw()
  platformmario3.draw()

  LuigiMindset()

  MarioMindset()





  game.update(30)


    
  portal1.draw()
  portal2.draw()



    
  
game.quit()
