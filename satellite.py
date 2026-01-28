import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []
next_satellite = 0

start_time = 0
total_time = 0
end_time = 0

number_of_satellite = 8

def create_satellites():
    global start_time
    for count in range(0, number_of_satellite):
        satellite = Actor("satellite")
        satellite.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        
        satellite.append(satellite)
        start_time = time()


def 