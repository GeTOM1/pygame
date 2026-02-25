import pgzrun
from random import randint

title = "pokemon game"

width = 500
height = 500
score = 0
game_over = False

ash = Actor('Ash2')
ash.pos = (200,200)
pica = Actor('Pica2')
pica.pos = (430,50)

def draw():
    screen.clear()
    screen.blit("background pokemon game", (0, 0))
    ash.draw()
    pica.draw()
    screen.draw.text("score: "+str(score), color = "black", topleft = (10, 10))
    if game_over:
        screen.fill("white")
        screen.draw.text("Game Over. Your score is: "+str(score), color = "red", fontsize = "40", midtop = (250, 50))
def place_pica():
    pica.x = randint(70, width-70)
    pica.y = randint(70, height-70)

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        ash.x = ash.x -2
    if keyboard.right:
        ash.x = ash.x +2
    if keyboard.up:
        ash.y = ash.y -2
    if keyboard.down:
        ash.y = ash.y +2

    flower_collected = ash.colliderect(pica)

    if flower_collected:
        score = score +10
        place_pica()

clock.schedule(time_up, 60.0)

pgzrun.go()