import pgzrun
from random import randint

title = "bee game"

width = 500
height = 500
score = 0
game_over = False

bee = Actor('bee')
bee.pos = (200,200)
flower = Actor('flower')
flower.pos = (430,50)

def draw():
    screen.clear()
    screen.blit("background bee game", (0, 0))
    bee.draw()
    flower.draw()
    screen.draw.text("score: "+str(score), color = "black", topleft = (10, 10))
    if game_over:
        screen.fill("white")
        screen.draw.text("Game Over. Your score is: "+str(score), color = "red", fontsize = "40", midtop = (250, 50))
def place_flower():
    flower.x = randint(70, width-70)
    flower.y = randint(70, height-70)

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        bee.x = bee.x -2
    if keyboard.right:
        bee.x = bee.x +2
    if keyboard.up:
        bee.y = bee.y -2
    if keyboard.down:
        bee.y = bee.y +2

    flower_collected = bee.colliderect(flower)

    if flower_collected:
        score = score +10
        place_flower()

clock.schedule(time_up, 60.0)

pgzrun.go()