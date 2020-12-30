import pygame

from IslandPy.Render.ARenderObject import ARenderObject
from IslandPy.Scenes.AScene import AScene


class TextLabel(ARenderObject):
    def __init__(self, scene: AScene, font_size: int, text: str = "", font_name: str = "",
                 position: (int, int) = (0, 0), bold: bool = False, italic: bool = False,
                 color: tuple = (255, 255, 255)) -> None:
        super().__init__(scene=scene, size=(0, 0), position=position)
        self._font_name = font_name
        self._font_size = font_size
        self.bold = bold
        self.italic = italic
        self.font_name = font_name
        self._font.set_bold(self.bold)
        self._font.set_italic(self.italic)
        self._text = text
        self._color = color
        self._image = None
        self.text = text

    @property
    def color(self) -> tuple:
        return self._color

    @color.setter
    def color(self, value: tuple) -> None:
        self._color = value
        self._update_font()

    @property
    def font_name(self) -> str:
        return self._font_name

    @font_name.setter
    def font_name(self, value: str) -> None:
        if not value:
            self._font_name = pygame.font.get_default_font().removesuffix(".ttf")
        else:
            self._font_name = value
        self._update_font()

    @property
    def font_size(self) -> int:
        return self._font_size

    @font_size.setter
    def font_size(self, value: int) -> None:
        self._font_size = value
        self._update_font()

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._image = self._font.render(self._text, True, self._color)
        self.rect.w, self.rect.h = self._image.get_rect().w, self._image.get_rect().h

    def _update_font(self):
        if self._font_name in pygame.font.get_fonts():
            self._font = pygame.font.SysFont(self._font_name, self._font_size)
        else:
            self._font = pygame.font.Font(f"{self._font_name}.ttf", self._font_size)

    def draw(self, surface: pygame.Surface) -> None:
        if not self._text or not self.is_draw:
            return
        surface.blit(self._image, self.rect)
