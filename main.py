import pygame

from IslandPy.Render.UI.Button import Button, ButtonState, ButtonEventType
from IslandPy.Render.UI.FontStyle import FontStyle
from IslandPy.Render.UI.Indents import Indents
from IslandPy.Render.UI.MultilineTextLabel import MultilineTextLabel
from IslandPy.Render.UI.TextLabel import TextLabel
from IslandPy.RenderWindow import RenderWindow
from IslandPy.Scenes.AScene import AScene


class CustomScene(AScene):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.count = 0
        self.label = TextLabel(scene=self, font_style=FontStyle(font_size=14, is_show_bg=False, bg_color=pygame.Color(125, 125, 125),
                                                                padding=Indents(left=10, top=5, bottom=5, right=10)),
                               text="Count: 0")
        self.b = Button(scene=self, size=(50, 10), state=ButtonState.NORMAL, position=(0, self.label.rect.bottom),
                        default_image_path="res/btn.png")
        self.b.actions[ButtonEventType.ON_HOVER_ON].handler = lambda: self.show()
        self.b.actions[ButtonEventType.ON_HOVER_OUT].handler = lambda: self.hide()
        self.label2 = MultilineTextLabel(scene=self, line_length=150, line_spacing=2, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", position=(0, 200))
        self.label2.copy_style_from(self.label)
        self.label2.padding = Indents(10, 10, 10, 10)
        # self.label2.hide()
        # self.label2.set_position_by_center(pygame.display.get_window_size())

        # self.ml_text = MultilineTextLabel(scene=self, line_length=140, text=self.label2.text, position=(0, 200))
        # self.ml_text.set_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

        # self.t = TextLabel(scene=self, font_size=14, text="Test", padding=Indents(left=10))
        # self.t.set_position((self.label.rect.right, 0))

    def hide(self) -> None:
        for o in self.objects:
            o.show_bounds = False

    def show(self) -> None:
        for o in self.objects:
            o.show_bounds = True

    def update(self, dt) -> None:
        super(CustomScene, self).update(dt)
        self.label.text = f"Count: {self.count}"
        self.label.move((self.count, 0))

    def handle_events(self, event: pygame.event.Event) -> None:
        super(CustomScene, self).handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.count += 1
                # self.label2.padding = Indents(self.count, self.count, self.count, self.count)
                # self.label2.font_size += self.count
                # self.change_scene("RectScene")
                # self.label.font_size = self.count
                self.label.is_show_bg = not self.label.is_show_bg
                self.label2.is_show_bg = not self.label2.is_show_bg


def main() -> None:
    # t1 = TestScene("RectScene")
    # c1.next_scenes[t1.name] = t1
    r = RenderWindow(bg_color=(32, 33, 36))
    r.fps = 75
    c1 = CustomScene("LabelScene")
    r.start(c1)


if __name__ == '__main__':
    main()
