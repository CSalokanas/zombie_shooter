import pygame as pg
from Player import Aidn5
from button import Buttons
from start_menu import StartMenu
import input_box
pg.init()
window = pg.display.set_mode((900,500))
clock = pg.time.Clock()
flag = True
player = Aidn5(window.get_width() / 2, 500)
def main():
    global color_inactive, color_active, color, active, text, done, font
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False


flag1 = True
x = 0
up_pressed, right_pressed, left_pressed = False, False, False
start_flag = True
start_menu = StartMenu(window)
start_button  = start_menu.start_button
while flag :
    keys = pg.key.get_pressed()
    while start_flag:
        start_menu.start_game()
        start_menu.get_difficulty()
        if start_button.check_click() and start_menu.get_difficulty() != "":
            print(start_menu.get_difficulty())
            print("Game Started")
            start_flag = False
            start_button.remove_buttons(window)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False


    pg.display.update()
    player.start(window)


    if not keys[pg.K_a]:
        left_pressed = False
    if not keys[pg.K_d]:
        right_pressed = False
    if not keys[pg.K_w]:
        up_pressed = False

    if keys[pg.K_a] and left_pressed == False:
        print(player.player_pos)
        player.move_left()
        left_pressed = True
        player.character_update(window)
    if keys[pg.K_d] and right_pressed == False:
        print(player.player_pos)
        player.move_right()
        player.character_update(window)
        right_pressed = True
    if (keys[pg.K_w]) and up_pressed == False:
        print(player.player_pos)
        player.move_up()
        player.character_update(window)
        up_pressed = True
    if (pg.key.get_pressed()[pg.K_s]) and down_pressed == False:
        print(player.player_pos)
        player.move_down()
        player.character_update(window)
        down_pressed = True

clock.tick(60)
