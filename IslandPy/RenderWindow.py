import os

import pygame
from pygame.rect import Rect
from pygame.time import Clock


class RenderWindow:
    def __init__(self) -> None:
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption("Render Window")
        self.__screen = pygame.display.set_mode((800, 600))
        self.__clock = Clock()
        self.__done = False
        self.__r = Rect(100, 100, 100, 100)

    def start(self) -> None:
        while not self.__done:
            self.__loop()
        pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__done = True

    def draw(self) -> None:
        pygame.draw.rect(self.__screen, (255, 255, 255), self.__r)

    def __loop(self) -> None:
        dt = self.__clock.tick(60)
        self.__screen.fill((34, 34, 35))
        self.handle_events()
        self.draw()
        pygame.display.flip()
