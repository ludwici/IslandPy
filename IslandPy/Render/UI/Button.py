import os
from typing import Tuple

import pygame
from flags import Flags
from IslandPy.Render.ARenderObject import ARenderObject
from IslandPy.Scenes.AScene import AScene


class ButtonEventType(Flags):
    ON_CLICK_LB = 1
    ON_CLICK_RB = 2
    ON_HOVER_ON = 4
    ON_HOVER_OUT = 8


class ButtonState(Flags):
    LOCKED = 1
    NORMAL = 2
    HOVERED = 4
    SELECTED = 8


class ButtonAction:
    def __init__(self, handler=None) -> None:
        self.handler = handler

    def do(self) -> None:
        if self.handler:
            self.handler()


class Button(ARenderObject):
    def __init__(self, scene: AScene, size: (int, int), default_image_path: str,
                 state: ButtonState = ButtonState.NORMAL, position: Tuple[int, int] = (0, 0)) -> None:
        super().__init__(scene=scene, size=size, position=position)
        self._current_image = None
        self._state = state
        self._images = {}
        self.set_image_by_state(state=ButtonState.NORMAL, path=default_image_path)
        self._current_image = self._images[self._state]

        self.actions = {ButtonEventType.ON_CLICK_LB: ButtonAction(), ButtonEventType.ON_CLICK_RB: ButtonAction(),
                        ButtonEventType.ON_HOVER_ON: ButtonAction(), ButtonEventType.ON_HOVER_OUT: ButtonAction()}

        self.__can_handle_event = True
        self.__can_call_out = False

        self.state = state

    def set_image_by_state(self, state, path: str) -> None:
        ext = os.path.splitext(path)[1]
        if ext == ".png":
            self._images[state] = pygame.image.load(path).convert_alpha()
        else:
            self._images[state] = pygame.image.load(path)

    def stop_events(self) -> None:
        self.__can_handle_event = False

    def start_events(self) -> None:
        self.__can_handle_event = True

    @property
    def is_can_handle_events(self) -> bool:
        return self.__can_handle_event

    @property
    def state(self) -> ButtonState:
        return self._state

    @state.setter
    def state(self, value: ButtonState) -> None:
        self._state = value
        try:
            if self.state & ButtonState.HOVERED or self.state & ButtonState.SELECTED:
                value = [s for s in ButtonState(value)][-1]
            self._current_image = self._images[value]
        except KeyError:
            self._current_image = self._images[ButtonState.NORMAL]

        self.rect.width = self._current_image.get_rect().width
        self.rect.height = self._current_image.get_rect().height

    @classmethod
    def register_event(cls, state):
        def process(handler):
            def wrapper(*args):
                args[0].add_action({state: lambda: handler(*args)})
                # args[0].actions[state] = lambda: handler(*args) <--- new system
            return wrapper
        return process

    def lock(self) -> None:
        self.state = ButtonState.LOCKED

    def unlock(self) -> None:
        self.state = ButtonState.NORMAL

    def unselect(self) -> None:
        self.state = ButtonState.NORMAL

    def select(self) -> None:
        self.state = ButtonState.SELECTED

    @property
    def is_locked(self) -> bool:
        return self.state == ButtonState.LOCKED

    @property
    def is_selected(self) -> bool:
        return self.state == ButtonState.SELECTED

    def on_hover_on(self) -> None:
        self.state |= ButtonState.HOVERED
        self.__can_call_out = True
        self.actions[ButtonEventType.ON_HOVER_ON].do()

    def on_hover_out(self) -> None:
        self.state ^= ButtonState.HOVERED
        self.actions[ButtonEventType.ON_HOVER_OUT].do()
        self.__can_call_out = False

    def on_click_lb(self) -> None:
        self.actions[ButtonEventType.ON_CLICK_LB].do()

    def on_click_rb(self) -> None:
        self.actions[ButtonEventType.ON_CLICK_RB].do()

    def handle_events(self, event: pygame.event.Event) -> None:
        if self.is_locked or not self.__can_handle_event:
            return

        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.on_hover_on()
            else:
                if self.__can_call_out:
                    self.on_hover_out()

        if event.type == pygame.MOUSEBUTTONUP and self.state & ButtonState.HOVERED:
            if event.button == 1:
                self.on_click_lb()
            elif event.button == 3:
                self.on_click_rb()

    def draw(self, surface: pygame.Surface) -> None:
        if self.is_draw:
            surface.blit(self._current_image, self.rect)
        super(Button, self).draw(surface)
