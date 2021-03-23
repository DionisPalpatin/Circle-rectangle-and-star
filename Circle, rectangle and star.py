import pygame as pg
from random import choices
from func_for_crs import Figure
import math, time


size = 800
fps = 60
clock = pg.time.Clock()
current_size = 3
flag = 1
key_press = "rect"


pg.init()
screen = pg.display.set_mode((size, size))


screen.fill((255, 255, 255))


key_press = "circle"
figure = Figure(current_size, key_press)
figure.drawing(screen)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        

    keys = pg.key.get_pressed()
    figure.analizing(screen, keys)
    figure.drawing(screen)


    figure.current_size += flag
    if figure.current_size > 100 or figure.current_size < 3:
        flag *= -1


    pg.display.update()
    clock.tick(fps)