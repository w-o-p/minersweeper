import pygame
from const import FPS, WIDTH, HEIGHT
from board import Board


def main(screen, wc, hc):
    clock = pygame.time.Clock()
    x, y = 250, 250
    r = 20
    must_pos = (x, y)
    move = 'none'

    f1 = pygame.font.Font(None, 100)

    board = Board(8, 8)
    board.set_view(int(440 * wc), int(20 * hc), int(130 * hc))

    running = True
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # quit()

        screen.fill('black')

        board.render(screen)

        pygame.display.update()
