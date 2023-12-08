from typing import Iterable

import pygame
from pygame_widgets.widget import WidgetBase


def show_widgets(widgets: Iterable[WidgetBase]) -> None:
    for widget in widgets:
        widget.show()


def hide_widgets(widgets: Iterable[WidgetBase]) -> None:
    for widget in widgets:
        widget.hide()


def events_handler(events: Iterable[pygame.event.Event]) -> bool:
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                from main_menu import main_menu
                main_menu()
