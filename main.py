import pygame as pg
pg.init()
window = pg.display.set_mode((800,600))
clock = pg.time.Clock()
flag = True

while flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False

clock.tick(60)
