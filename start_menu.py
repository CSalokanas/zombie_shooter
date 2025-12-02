import pygame
from button import Buttons
class StartMenu(Buttons,):
    def __init__(self):
        super().__init__()
        self.window = pygame.display.set_mode((800,600))
        self.start_button = Buttons("Start",self.window, x_pos= (self.window.get_width()), y_pos=self.window.get_height()-10, borders=True, text_size=10, button_color="white", text_color="black")

    def start_game(self):
        self.start_button.draw()
