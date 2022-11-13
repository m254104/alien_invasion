import pygame
import sys

from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 700))
star = pygame.image.load('images/explosion3.png')
screen_rect = screen.get_rect()
star_rect = star.get_rect()


def draw_star():
        screen.blit(star, (randint(0, 700), randint(0, 700)))

x = 0
while x < 100:
    draw_star()
    pygame.display.flip()
    x += 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()



