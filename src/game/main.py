# -*- coding: utf-8 -*-
"""
This module contains the main logic for Conway's Game of Life.

The game evolves in steps, where at each step the board state
changes based on some rules. This module provides functionalities
to initialize the game board, evolve it through steps, and display it.
"""
import random
from typing import List, Set

import pygame  # type: ignore

from . import settings
from .models import Grid, Position
from .settings import GRID_HEIGHT, GRID_WIDTH, TILE_SIZE

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

clock = pygame.time.Clock()


def gen(num: int) -> Set[Position]:
    """Generates a number of random positions to display on the grid."""

    return set([Position(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for _ in range(num)])


def adjust_grid(positions: Set[Position]) -> Set[Position]:
    """Implements game logic."""

    all_neighbors: Set[Position] = set()
    new_positions: Set[Position] = set()

    # deletes necessary cells
    for position in positions:
        neighbours = get_neighbors(position)
        all_neighbors.update(neighbours)

        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) in [2, 3]:
            new_positions.add(position)

    # creates necessary cells
    for position in all_neighbors:
        neighbours = get_neighbors(position)

        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) == 3:
            new_positions.add(position)

    return new_positions


def get_neighbors(position: Position) -> List[Position]:
    """Returns a list of all neighboring cells for a given position"""

    x, y = position.x, position.y
    neighbors: List[Position] = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append(Position(x + dx, y + dy))

    return neighbors


def run() -> None:
    """Responsible for creating the main game loop"""

    running = True
    playing = False
    count = 0

    grid = Grid()
    positions: Set[Position] = set()
    while running:
        # Regulates the speed of the game loop setting a max FPS
        clock.tick(settings.FPS)

        if playing:
            count += 1

        if count >= settings.FREQUENCY:
            count = 0
            positions = adjust_grid(positions)

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = Position(col, row)
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(4, 10) * GRID_WIDTH)

        screen.fill(settings.GREY)
        grid.draw_grid(positions, screen)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    run()
