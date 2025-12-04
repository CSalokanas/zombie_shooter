import pygame as pg
from button import Buttons


class StartMenu(Buttons):
    def __init__(self, window):
        self.start_button = Buttons("Start",window, x_pos= 799, y_pos=window.get_height()/2, borders=True, text_size=20, button_color="white", text_color="black", size_x=100,size_y=50)
        super().__init__(screen=window,text="a")
        self.easy_button = Buttons("Easy",window, x_pos=0, y_pos=0, borders=True, text_size=20, button_color="green", text_color="black", size_x=100,size_y=50, border_color="green", aliases=True)
        self.medium_button = Buttons("Medium",window, x_pos=400, y_pos=0, borders=True, text_size=20, button_color="orange", text_color="black", size_x=100,size_y=50, border_color="orange")
        self.hard_button = Buttons("Hard",window, x_pos=800, y_pos=0, borders=True, text_size=20, button_color="red", text_color="black",size_x=100,size_y=50, border_color="red")
        self.button_list = [self.start_button, self.easy_button, self.medium_button, self.hard_button]
        self.difficulty = ""
    def start_game(self):
        for button in self.button_list:
            button.draw()
        pg.display.update()

    def get_difficulty(self):
        if self.easy_button.check_click():
            self.difficulty = "Easy"
        elif self.medium_button.check_click():
            self.difficulty = "Medium"
        elif self.hard_button.check_click():
            self.difficulty = "Hard"
        return self.difficulty

