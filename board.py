import pygame
import random

FPS = 50


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color = 'white'
        self.border_width = 1

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pygame.draw.rect(screen, self.color, (
                    self.left + self.cell_size * j, self.top + self.cell_size * i,
                    self.cell_size, self.cell_size), self.border_width)
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, 'black', (
                        self.left + self.cell_size * j +
                        self.border_width // 2 + self.border_width % 2,
                        self.top + self.cell_size * i +
                        self.border_width // 2 + self.border_width % 2,
                        self.cell_size - self.border_width - self.border_width % 2,
                        self.cell_size - self.border_width - self.border_width % 2))
                elif self.board[i][j] == 1:
                    pygame.draw.rect(screen, 'red', (
                        self.left + self.cell_size * j +
                        self.border_width // 2 + self.border_width % 2,
                        self.top + self.cell_size * i +
                        self.border_width // 2 + self.border_width % 2,
                        self.cell_size - self.border_width - self.border_width % 2,
                        self.cell_size - self.border_width - self.border_width % 2))
                elif self.board[i][j] == 2:
                    pygame.draw.rect(screen, 'blue', (
                        self.left + self.cell_size * j +
                        self.border_width // 2 + self.border_width % 2,
                        self.top + self.cell_size * i +
                        self.border_width // 2 + self.border_width % 2,
                        self.cell_size - self.border_width - self.border_width % 2,
                        self.cell_size - self.border_width - self.border_width % 2))

    def get_cell(self, pos):
        x, y = pos
        xb = (x - self.left) // self.cell_size
        if xb > self.width - 1 or xb < 0:
            return None
        yb = (y - self.top) // self.cell_size
        if yb > self.height - 1 or yb < 0:
            return None
        cell = (xb, yb)
        return cell

    def on_click(self, cell_coords):
        x, y = cell_coords
        if self.board[y][x] == 0:
            self.board[y][x] = 1
        elif self.board[y][x] == 1:
            self.board[y][x] = 2
        elif self.board[y][x] == 2:
            self.board[y][x] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        # print(cell)
        if cell:
            self.on_click(cell)
