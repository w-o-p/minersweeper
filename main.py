# ГЛАВНЫЙ ФАЙЛ


from button import Button
from const import FPS, WIDTH, HEIGHT
from game import main
import pygame
import os
import subprocess
import sqlite3

pygame.init()

color = (0, 0, 0)
text_color = 'white'

# size = width, height = WIDTH, HEIGHT
# x, y = list(map(int, input().split()))
screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
size = width, height = screen.get_width(), screen.get_height()
wc, hc = width / WIDTH, height / HEIGHT  # коэффиценты отношения пользовательского разрешения экрана к стандартному
print(size)
clock = pygame.time.Clock()
pygame.mouse.set_cursor(*pygame.cursors.tri_left)

f1 = pygame.font.Font(None, int(60 * hc))  # TODO придумать как изменять размер шрифта
# еще exe не может шрифт загрузить почему то
f1.set_italic(True)
f2 = pygame.font.Font(None, 32)
# screen.fill(color)
# language = 'rus'

text1 = f1.render('Начать игру', True, text_color)
start_game_btn = Button((100 * wc, 150 * hc), text1, text_color)

# filename = 'sounds/mario_sound.mp3'
# audio_turn_off = True
# pygame.mixer.music.load(filename)
# pygame.mixer.music.set_volume(0.5)
# if not audio_turn_off:
#    pygame.mixer.music.play(-1)

# если надо до цикла отобразить объекты на экране
screen.fill('black')

# главный цикл
if __name__ == '__main__':
    while True:

        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

        # --------
        # изменение объектов и многое др.
        # --------
        screen.fill(color)

        start_game_btn.render(screen)

        pygame.draw.line(screen, 'white', [960 * wc, 0 * hc], [960 * wc, 1080 * hc])

        if start_game_btn.mouse_check(pygame.mouse.get_pos()):
            start_game_btn.change_color('red')
        elif start_game_btn.color == 'red':
            start_game_btn.change_color('white')

        pressed = pygame.mouse.get_pressed()
        if pressed[0]:  # обработка нажатий левой кнопки мыши
            x1, y1 = pygame.mouse.get_pos()
            if start_game_btn.mouse_check((x1, y1)):
                main(screen, wc, hc)

        # обновление экрана
        pygame.display.update()
