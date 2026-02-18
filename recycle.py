import pgzrun
import random

FONT_option = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTRE_X = WIDTH /2
CENTRE_Y = HEIGHT /2
CENTRE = (CENTRE_X, CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEM = ["bag", "battery", "bottle", "chips"]

game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global items, game_over, game_complete, current_level
    screen.clear()
    screen.blit("background", (0, 0))
    if game_over:
        print("Game over, try again")
    elif game_complete:
        print("Congrats, the game is complete!")
    else:
        for i in items:
            i.draw()

def update():
    global items
    if len(items) == 0
    items = make_items(current_level)

def make_items(number_of_extra_itens)
    items_to_create = get_options_to_create(number_of_extra_itens)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    return new_items