import pygame


class Button:
    def __init__(self, coord, text, text_color):
        self.x = coord[0] - 10
        self.y = coord[1] - 10
        self.w = text.get_width() + 20
        self.h = text.get_height() + 20
        self.border_width = 3
        self.color = text_color
        self.text = text

    def render(self, surf):
        pygame.draw.rect(surf, self.color, (self.x, self.y, self.w, self.h), self.border_width)
        surf.blit(self.text, (self.x + 10, self.y + 10))

    def mouse_check(self, tup):
        x, y = tup
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            return True
        return False

    def change_color(self, color):
        self.color = color
