import pygame

from IslandPy.RenderObject import RenderObject
from IslandPy.Scene import Scene


class TestScene(Scene):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.r1 = RenderObject(scene=self, size=(100, 100), position=(0, 0))
        self.r2 = RenderObject(scene=self, size=(100, 100), position=(300, 120))

    def handle_events(self, event: pygame.event.Event) -> None:
        super().handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.r1.is_draw:
                    self.r1.hide()
                else:
                    self.r1.show()
