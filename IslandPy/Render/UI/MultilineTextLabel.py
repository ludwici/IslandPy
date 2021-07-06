from collections import deque
from typing import Tuple

import pygame

from IslandPy.Render.UI.FontStyle import FontStyle
from IslandPy.Render.UI.TextLabel import TextLabel
from IslandPy.Scenes.AScene import AScene


class MultilineTextLabel(TextLabel):
    __slots__ = ("_rendered_text", "_line_length", "_line_spacing")

    def __init__(self, scene: AScene, text: str = "", line_length: int = 1, line_spacing: int = 2,
                 position: Tuple[int, int] = (0, 0), font_style: FontStyle = FontStyle()) -> None:
        self._rendered_text = []
        self._line_length = line_length
        self._line_spacing = line_spacing
        super().__init__(scene, text=text, position=position, font_style=font_style)

    def copy_style_from(self, other) -> None:
        if isinstance(other, MultilineTextLabel):
            self._line_length = other.line_length
            self._line_spacing = other.line_spacing
        super().copy_style_from(other)

    def draw(self, surface: pygame.Surface) -> None:
        super(MultilineTextLabel, self).draw(surface)

    def __add_new_line(self, text: str) -> None:
        render_text = self.font_style.font.render(text, True, self.color)
        self._rendered_text.append(render_text)

    @TextLabel.text.setter
    def text(self, value: str) -> None:
        self._text = value

        tmp = deque(self._text.split())
        str_tmp = ""
        size = 0
        self._rendered_text.clear()
        while tmp:
            t = tmp.popleft()
            size += self.font_style.font.size(t)[0]
            if size >= self.line_length:
                size = self.font_style.font.size(t)[0]
                self.__add_new_line(str_tmp)
                str_tmp = t + " "
            else:
                str_tmp += t + " "
        self.__add_new_line(str_tmp)
        self.rect.w = max([r.get_width() for r in self._rendered_text]) + self.padding.right + self.padding.left
        self.rect.h = sum([r.get_height() + self.line_spacing for r in self._rendered_text]) + self.padding.bottom + self.padding.top
        self._surface = pygame.Surface((self.rect.w, self.rect.h))
        self._surface.fill(color=self.bg_color)
        pos_y = self.padding.top
        for r in self._rendered_text:
            self._surface.blit(r, (self.padding.left, pos_y))
            pos_y += r.get_height() + self.line_spacing

        if self.is_show_bg:
            self._surface.set_colorkey(self.bg_color)
        else:
            self._surface.set_colorkey((0, 0, 0))

    @property
    def line_length(self) -> int:
        return self._line_length

    @property
    def line_spacing(self) -> int:
        return self._line_spacing

    @property
    def line_count(self) -> int:
        return len(self._rendered_text)
