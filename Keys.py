import pygame
import sys

class Keys:

    def __init__(self):
        """A new program that will display attributes when a key is pressed"""
        pygame.init()
        self.screen = pygame.display.set_mode((300,150))

    def run(self):
        while True:
            self._check_events()

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)




if __name__ == '__main__':
    K = Keys()
    K.run()
