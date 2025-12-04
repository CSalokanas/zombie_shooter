import pygame

class Buttons:
    def __init__(self, text, screen, size_x=150, size_y=50, font="freesansbold.ttf", text_size=20,button_color ="gray",x_pos=0,y_pos=0, text_color="white", text_shadow = False, aliases = True, borders = False, line_thickness = 2, border_color = "red"):

         self.Size_X = size_x
         self.Size_Y = size_y
         self.Color = button_color
         self.Text = text
         self.Text_Size = text_size
         self.Text_Color = text_color
         self.Position_X = x_pos
         self.Position_Y = y_pos
         self.Font = font
         self.Screen = screen
         self.Text_Shadow = text_shadow
         self.aliases = aliases
         self.Borders = borders
         self.Line_Thickness = line_thickness
         self.Border_Color = border_color
         self.font = pygame.font.Font(font, text_size)
         self.text = self.font.render(text,aliases, text_color)
         self.shadow_text = self.font.render(text, aliases, "black")
    def draw(self):
        if self.Borders:
            button_rect = pygame.rect.Rect(self.Position_X-self.Line_Thickness, self.Position_Y-self.Line_Thickness,
                                           self.Size_X+self.Line_Thickness*2, self.Size_Y+self.Line_Thickness*2)
            pygame.draw.rect(surface=self.Screen, color=self.Border_Color, rect=button_rect)

        button_rect = pygame.rect.Rect(self.Position_X, self.Position_Y, self.Size_X, self.Size_Y)
        pygame.draw.rect(surface=self.Screen, color=self.Color, rect=button_rect)
        if self.Text_Shadow:

            self.Screen.blit(self.shadow_text,
                                           (self.Position_X + self.Size_X / 2 + 2, self.Position_Y + 12))
            self.Screen.blit(self.text,
                                           (self.Position_X + self.Size_X / 2-10, self.Position_Y + 10))
        else:
            self.Screen.blit(self.text,
                                           (self.Position_X + self.Size_X / 2-10, self.Position_Y + 10))
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_just_pressed()[0]:
            if self.Position_X < mouse_pos[0] < self.Size_X + self.Position_X:
                if self.Position_Y < mouse_pos[1] < self.Size_Y + self.Position_Y:
                    return True
        return False
    def text_shadow(self):
        self.text = self.font.render(self.Text, self.aliases, "black")
    def image_button(self):
        pass
    def remove_buttons(self,window):
        window.fill((0,0,0))
        pygame.display.flip()