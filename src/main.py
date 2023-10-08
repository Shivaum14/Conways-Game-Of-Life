# -*- coding: utf-8 -*-
"""This module is responsible for implementing the game loop."""
from typing import Set

import pygame  # type: ignore

from src import settings
from src.models import Position

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

clock = pygame.time.Clock()


def draw_grid(positions: Set[Position]) -> None:
    for position in positions:
        col, row = position.x, position.y
        top_left = (col * settings.TILE_SIZE, row * settings.TILE_SIZE)
        pygame.draw.rect(
            screen,
            settings.YELLOW,
            (*top_left, settings.TILE_SIZE, settings.TILE_SIZE),
        )

    for row in range(settings.GRID_HEIGHT):
        pygame.draw.line(
            screen,
            settings.BLACK,
            (0, row * settings.TILE_SIZE),
            (settings.WIDTH, row * settings.TILE_SIZE),
        )

    for col in range(settings.GRID_WIDTH):
        pygame.draw.line(
            screen,
            settings.BLACK,
            (col * settings.TILE_SIZE, 0),
            (col * settings.TILE_SIZE, settings.HEIGHT),
        )
    pass


def main() -> None:
    """Responsible for creating the main game loop"""
    running = True

    positions: Set[Position] = set()
    positions.add(Position(10, 10))
    while running:
        # Regulates the speed of the game loop setting a max FPS
        clock.tick(settings.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(settings.GREY)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
