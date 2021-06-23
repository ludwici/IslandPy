from copy import copy
from typing import Tuple

import pygame
from pygame.color import Color

from IslandPy.Render.ARenderObject import ARenderObject
from IslandPy.Render.UI.FontStyle import FontStyle
from IslandPy.Render.UI.Indents import Indents
from IslandPy.Scenes.AScene import AScene


class TextLabel(ARenderObject):
    __slots__ = ("_text", "_image", "__surface", "_font_style")

    def __init__(self, scene: AScene, text: str = "", position: Tuple[int, int] = (0, 0),
                 font_style: FontStyle = FontStyle()) -> None:
        super().__init__(scene=scene, size=(0, 0), position=position)
        self._font_style = font_style
        self.font_name = font_style.font_name
        self._text = text
        self._image = None
        self.__surface = None
        self.font_style.update_font()
        self.text = text

    def copy_style_from(self, other: "TextLabel") -> None:
        self.font_style = copy(other.font_style)
        self.font_style.update_font()
        self.text = self.text

    @property
    def font_style(self) -> FontStyle:
        return self._font_style

    @font_style.setter
    def font_style(self, font_style: FontStyle) -> None:
        self._font_style = font_style
        self.text = self.text

    @property
    def padding(self) -> Indents:
        return self.font_style.padding

    @padding.setter
    def padding(self, value: Indents) -> None:
        self.font_style.padding = value
        self.text = self.text

    @property
    def alpha(self) -> int:
        return self.font_style.alpha

    @alpha.setter
    def alpha(self, value: int) -> None:
        self.font_style.alpha = value

    @property
    def bold(self) -> bool:
        return self.font_style.bold

    @bold.setter
    def bold(self, value: bool) -> None:
        self.font_style.bold = value
        self.font_style.update_font()

    @property
    def italic(self) -> bool:
        return self.font_style.italic

    @italic.setter
    def italic(self, value: bool) -> None:
        self.font_style.italic = value
        self.font_style.update_font()

    @property
    def font_name(self) -> str:
        return self.font_style.font_name

    @font_name.setter
    def font_name(self, value: str) -> None:
        if not value:
            self.font_style.font_name = pygame.font.get_default_font().removesuffix(".ttf")
        else:
            self.font_style.font_name = value
        self.font_style.update_font()

    @property
    def font_size(self) -> int:
        return self.font_style.font_size

    @font_size.setter
    def font_size(self, value: int) -> None:
        self.font_style.font_size = value
        self.font_style.update_font()
        self.text = self.text

    @property
    def color(self) -> Color:
        return self.font_style.color

    @property
    def bg_color(self) -> Color:
        return self.font_style.bg_color

    @property
    def text(self) -> str:
        return self._text

    @property
    def is_show_bg(self) -> bool:
        return self.font_style.is_show_bg

    @is_show_bg.setter
    def is_show_bg(self, value: bool) -> None:
        self.font_style.is_show_bg = value
        self.text = self.text

    def text_length_by_font(self, text: str) -> int:
        return self.font_style.font.size(text)[0]

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._image = self.font_style.font.render(self._text, True, self.color)

        self.rect.w = self._image.get_rect().w + self.padding.right + self.padding.left
        self.rect.h = self._image.get_rect().h + self.padding.bottom + self.padding.top
        if self.is_show_bg:
            self.__surface = pygame.Surface((self.rect.w, self.rect.h))  # lgtm [py/call/wrong-arguments]
            self.__surface.fill(color=self.bg_color)
            self.__surface.blit(self._image, (self.padding.left, self.padding.top))
            self.__surface.set_alpha(self.alpha)
        # else:
        #     self.rect.w = self._image.get_rect().w + self.padding.right + self.padding.left
        #     self.rect.h = self._image.get_rect().h + self.padding.bottom + self.padding.top

    def draw(self, surface: pygame.Surface) -> None:
        if not self._text or not self.is_draw:
            return

        if self.is_show_bg:
            surface.blit(self.__surface, self.rect)
        else:
            surface.blit(self._image, self.rect)
        super(TextLabel, self).draw(surface)
