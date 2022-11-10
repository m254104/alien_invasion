import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((800, 700))
star = pygame.image.load('images/laserYellow_burst.png')
screen_rect = screen.get_rect()
star_rect = star.get_rect()

space = screen_rect.width // star_rect.width

def draw_stars():
    for y in range(space):
        for x in range(space):
            screen.blit(star, (x * star_rect.width, y * star_rect.height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    draw_stars()
    pygame.display.flip()