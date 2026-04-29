from gamelib import *
game = Game(800,600,"Tag or Get Tagged")

bk = Image("images/background1.png",game)
bk.resizeTo(game.width,game.height)

game.setBackground(bk)
game.drawText("Timer",10,5)

Luigi = Animation("images/Luigi.png", 8, game, 490, 446, 1)
Luigi.resizeBy(-65)
Luigi.moveTo(60,570)

def positionObjects( objects ):
    for i in range(len(objects)):
        x = randint(100,700)
        y = -randint(100, 1000) #Note: negative randint
        objects[i].moveTo(x, y)
        s = randint(4, 8)
        objects[i].setSpeed(s, 180)
        objects[i].visible = True

rainbowpower = []
for i in range(1):
    r =Image("images/star.png", game)
    r.resizeBy(-90)
    rainbowpower.append(r)

positionObjects(rainbowpower)

goomba = []
for i in range(5):
    g = Image("images/goomba.png", game)
    g.resizeBy(-80)
    goomba.append(g)

positionObjects(goomba)


# Platforms (using colored rectangles instead of images)
platforms = []
platform1 = Shape("rectangle", game, 200, 20, brown)  # Brown platform
platform1.moveTo(200, 500)
platforms.append(platform1)

platform2 = Shape("rectangle", game, 150, 20, green)  # Green platform
platform2.moveTo(500, 400)
platforms.append(platform2)

platform3 = Shape("rectangle", game, 180, 20, blue)  # Blue platform
platform3.moveTo(100, 300)
platforms.append(platform3)

# Ground platform
ground = Shape("rectangle", game, game.width, 20, gray)  # Gray ground
ground.moveTo(0, game.height - 20)
platforms.append(ground)

portal1=Animation("images/netherportal1.png",32,game, 1800/9,800/5,1)
portal2=Animation("images/netherportal1.png",32,game, 1800/9,800/5,1)

mariomusic = Sound("sounds/04. Super Mario 1991.mp3",0)

Mario = Animation("images/Mario.png",8,game, 336/8, 40, 1)
Mario.moveTo(30,570)

# Tag bar that transfers between Mario and Luigi
tag_bar = Shape("rectangle", game, 40, 8, red)
tag_holder = "Mario"  # Track who has the tag bar

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


astoryimage = Image("images/storyimage.png",game)
storyimage.visible = False
storyimage.resizeTo(game.width, game.height)

portal1.visible = False

def LuigiMindset():
  if keys.Pressed[K_LEFT]:
      Luigi.x -= 5
  if keys.Pressed[K_RIGHT]:
      Luigi.x += 5
  if keys.Pressed[K_UP]:
      Luigi.y -= 5
  if keys.Pressed[K_DOWN]:
      Luigi.y += 5


        
def MarioMindset():
  if keys.Pressed[K_w]:
    Mario.y-=5
  if keys.Pressed[K_s]:
    Mario.y+=5
  if keys.Pressed[K_a]:
    Mario.x-=5
  if keys.Pressed[K_d]:
    Mario.x+=5

def checkPlatformCollision(character):
    """Check if character is standing on any platform"""
    for platform in platforms:
        # Check if character is above platform and close enough to land on it
        if (character.bottom >= platform.top and 
            character.bottom <= platform.top + 10 and  # Small tolerance for landing
            character.left < platform.right and 
            character.right > platform.left):
            # Snap character to platform top
            character.moveTo(character.x, platform.top - character.height)
            return True
    return False

def updateTagBar():
    """Update tag bar position based on who has it"""
    global tag_holder
    if tag_holder == "Mario":
        tag_bar.moveTo(Mario.x - 20, Mario.y - 20)
    else:
        tag_bar.moveTo(Luigi.x - 20, Luigi.y - 20)

def checkTagCollision():
    """Check collision between Mario and Luigi to transfer tag"""
    global tag_holder
    if Mario.collidedWith(Luigi):
        if tag_holder == "Mario":
            tag_holder = "Luigi"
        else:
            tag_holder = "Mario"

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
  portal1.draw()

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

# GAME LOOP
while not game.over:
    game.processInput()
    game.scrollBackground("left",4)

    # Apply gravity to characters
    Mario.y += 2  # Gravity
    Luigi.y += 2  # Gravity
    
    LuigiMindset()
    MarioMindset()

    # Check platform collisions
    checkPlatformCollision(Mario)
    checkPlatformCollision(Luigi)

    # Check tag collision and update tag bar
    checkTagCollision()
    updateTagBar()

    for r in rainbowpower:
        r.move()
        r.draw()

    for g in goomba:
        g.move()
        g.draw()

    # Draw platforms
    for p in platforms:
        p.draw()

    Luigi.draw()
    Mario.draw()
    tag_bar.draw()

    game.update(30)








    
  
game.quit()

