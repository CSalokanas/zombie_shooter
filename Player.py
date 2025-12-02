import pygame as pg

class Aidn5(pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.pressed_a = False
        self.pressed_d = False
        self.x1 = x
        self.y1 = y
        self.player_pos = (self.x1, self.y1)
        self.speed = 10
        self.pen_up = True


        #penup varient
        self.pen_down = True  # Start with pen down
        self.trail_positions = []  # Store trail points
        self.trail_color = (0, 255, 0)
        self.trail_width = 3

    def clear_trail(self):
        self.trail_positions.clear()

    def start(self, screen):
        pg.draw.circle(screen, "white", self.player_pos, 10)

    def move_left(self):
        self.x1 -= self.speed

    def move_right(self):
        self.x1 += self.speed

    def move_up(self):
        self.y1 -= self.speed

    def move_down(self):
        self.y1 += self.speed

    def character_update(self, screen):
        self.player_pos = (self.x1, self.y1)
        pg.draw.circle(screen, "white", self.player_pos, 10)