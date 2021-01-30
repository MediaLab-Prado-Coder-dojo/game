import pygame
# import time
# import random

de setup():
    global game_display
    pygame.init()
    display_width = 800
    display_height = 600
    white = (255,255,255)
    black = (0,0,0)
    width = 10
    game_display = pygame.display.set_mode((display_width, display_height))
    game_display.fill(black)


def graficas(points):
    global game_display
    print(points)
    pygame.display.
    if points.__len__() > 1:
        pygame.draw.lines(game_display, white, False, points, width)

    else:
        pygame.draw.circle(game_display, white, points[0], width)
        print("no mames")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
