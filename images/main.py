from gamelib import *
game = Game(800,600,"Tag or Get Tagged")

bk = Image("images/background1.png",game)
bk.resizeTo(game.width,game.height)

game.setBackground(bk)
game.drawText("Timer",10,5)

Luigi = Animation("/Luigi.png", 8, game, 1000/5, 600/2, 1)
Luigi.resizeBy(-65)
Luigi.moveTo(60,570)

rainbowpower = Animation("images/rainbow star.png", 8, game, 1800/8, 200, 1)
rainbowpower.resizeBy(-75)
rainbowpower.moveTo(30,100)

portal=Animation("images/nether portal.png",32,game, 1800/9,800/5,1)

Mario = Animation("images/Mario.png",8,game, 336/8, 40, 1)
Mario.moveTo(30,570)

portal.resizeBy(-75)
def LuigiMindset():
  if keys.Pressed[K_LEFT]:
      Luigi.x -= 5
  if keys.Pressed[K_RIGHT]:
      Luigi.x += 5
  if keys.Pressed[K_UP]:
      Luigi.y -= 5
  if keys.Pressed[K_DOWN]:
      Luigi.y += 5

def positionObjects( objects ):
    for i in range(len(objects)):
        x = randint(100,700)
        y = -randint(100, 5000) #Note: negative randint
        objects[i].moveTo(x, y)
        s = randint(4, 8)
        objects[i].setSpeed(s, 180)
        objects[i].visible = True
        
if Mario.collidedWith(rainbowpower):
  Mario.speed+=50

if Mario.collidedWith(rainbowpower):
  if keys.Pressed[K_LEFT]:
      Luigi.x -= 6
  if keys.Pressed[K_RIGHT]:
      Luigi.x += 6

        
def MarioMindset():
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
  Luigi.move()
  rainbowpower.move()
  Mario.move()
  bk.draw()
  portal.draw()
  LuigiMindset()
  MarioMindset()


    

  game.update(30)
game.quit()

