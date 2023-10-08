# -*- coding: utf-8 -*-
"""This module defines the models used the game/simulation"""
from typing import Any, Set

import pygame  # type: ignore
from pydantic import BaseModel, validator

from . import settings
from .settings import GRID_HEIGHT, GRID_WIDTH, TILE_SIZE


class Position(BaseModel):
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x=x, y=y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    @validator("x")
    def validate_x_within_range(cls, v: int) -> int:
        if 0 <= v <= GRID_WIDTH:
            return v
        raise ValueError(f"X coordinate is out of range (0 - {GRID_WIDTH})")

    @validator("y")
    def validate_y_within_range(cls, v: int) -> int:
        if 0 <= v <= GRID_HEIGHT:
            return v
        raise ValueError(f"Y coordinate is out of range (0 - {GRID_HEIGHT})")


class Grid(BaseModel):
    grid_width: int = GRID_WIDTH
    grid_height: int = GRID_HEIGHT
    tile_size: int = TILE_SIZE

    def draw_grid(self, positions: Set[Position], screen: pygame.Surface) -> None:
        """Draws a the grid and displays all active cells."""

        for position in positions:
            col, row = position.x, position.y
            top_left = (col * TILE_SIZE, row * TILE_SIZE)
            pygame.draw.rect(
                screen,
                settings.YELLOW,
                (*top_left, TILE_SIZE, TILE_SIZE),
            )

        for row in range(GRID_HEIGHT):
            pygame.draw.line(
                screen,
                settings.BLACK,
                (0, row * TILE_SIZE),
                (settings.WIDTH, row * TILE_SIZE),
            )

        for col in range(GRID_WIDTH):
            pygame.draw.line(
                screen,
                settings.BLACK,
                (col * TILE_SIZE, 0),
                (col * TILE_SIZE, settings.HEIGHT),
            )
