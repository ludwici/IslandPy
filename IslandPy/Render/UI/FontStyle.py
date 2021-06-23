import pygame.font
from pygame import Color

from IslandPy.Render.UI.Indents import Indents


class FontStyle:
    def __init__(self, font_size: int = 1, font_name: str = "", bold: bool = False, italic: bool = False,
                 alpha: int = 255, color: Color = Color(255, 255, 255), bg_color: Color = Color(0, 0, 0),
                 is_show_bg: bool = False, padding: Indents = Indents()) -> None:
        self.font = None
        self.font_size = font_size
        self.font_name = font_name
        self.bold = bold
        self.italic = italic
        self.alpha = alpha
        self.color = color
        self.bg_color = bg_color
        self.is_show_bg = is_show_bg
        self.padding = padding

    def update_font(self) -> None:
        if self.font_name in pygame.font.get_fonts():
            self.font = pygame.font.SysFont(self.font_name, self.font_size)
        else:
            self.font = pygame.font.Font(f"{self.font_name}.ttf", self.font_size)

        self.font.set_bold(self.bold)
        self.font.set_italic(self.italic)
