import pygame
import time

pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((170, 240,240))

#draw the character
character = pygame.image.load('images\lil_ship.png')
pygame.display.flip()
time.sleep(4)