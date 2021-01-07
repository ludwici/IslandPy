import pygame

from IslandPy.Render.UI.Button import Button, ButtonState
from IslandPy.Render.UI.Indents import Indents
from IslandPy.Render.UI.TextLabel import TextLabel
from IslandPy.RenderWindow import RenderWindow
from IslandPy.Scenes.AScene import AScene
from IslandPy.Scenes.TestScene import TestScene


class CustomScene(AScene):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.count = 0
        self.label = TextLabel(scene=self, font_size=14, text="Count: 0",
                               padding=Indents(left=10, top=5, bottom=5, right=10), can_show_bg=True)
        self.b = Button(scene=self, size=(50, 10), state=ButtonState.NORMAL, position=(0, self.label.rect.bottom),
                        default_image_path="res/btn.png")
        # self.t = TextLabel(scene=self, font_size=14, text="Test", padding=Indents(left=10))
        # self.t.set_position((self.label.rect.right, 0))

    def update(self, dt) -> None:
        super(CustomScene, self).update(dt)
        self.label.text = f"Count: {self.count}"
        self.label.move((self.count, 0))

    def handle_events(self, event: pygame.event.Event) -> None:
        super(CustomScene, self).handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.count += 1
                # self.change_scene("RectScene")
                # self.label.font_size = self.count
                # self.label.can_show_bg = not self.label.can_show_bg


def main() -> None:
    # t1 = TestScene("RectScene")
    # c1.next_scenes[t1.name] = t1
    r = RenderWindow()
    c1 = CustomScene("LabelScene")
    r.start(c1)


if __name__ == '__main__':
    main()
