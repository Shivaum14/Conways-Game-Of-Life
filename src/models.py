# -*- coding: utf-8 -*-
"""This module defines the models used the game/simulation"""
from typing import Any

from pydantic import BaseModel, validator

from src.settings import GRID_HEIGHT, GRID_WIDTH


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
