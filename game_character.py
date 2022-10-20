import pygame
import time

pygame.init()
screen = pygame.display.set_mode((150,150))
screen.fill((170, 240,240))

#draw the character
character = pygame.image.load('images/lil_ship.png')

character_rect = character.get_rect()
screen_rect = screen.get_rect()
character_rect.center = screen_rect.center #move the plane to the middle

#draw ('blit') the character graphic onto the screen.
screen.blit(character, character_rect)

pygame.display.flip()
time.sleep(4)