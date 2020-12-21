import pygame
from pygame.rect import Rect

from IslandPy.Scene import Scene


class RenderObject:
    def __init__(self, scene: Scene, size: (int, int), position: (int, int) = (0, 0)) -> None:
        self.__speed = 1
        self.__is_draw = True
        self.scene = scene
        self.scene.objects.append(self)
        self._rect = Rect((position[0], position[1], size[0], size[1]))

    @property
    def is_draw(self) -> bool:
        return self.__is_draw

    def show(self) -> None:
        self.__is_draw = True

    def hide(self) -> None:
        self.__is_draw = False

    def update(self, dt) -> None:
        if self._rect.x > 300 or self._rect.x < 0:
            self.__speed = -self.__speed
        move = self.__speed
        self._rect.x += move

    def handle_events(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.__speed = abs(self.__speed)
            if event.key == pygame.K_a:
                self.__speed *= -1

    def draw(self, surface: pygame.Surface) -> None:
        if self.__is_draw:
            pygame.draw.rect(surface, (255, 255, 255), self._rect)
