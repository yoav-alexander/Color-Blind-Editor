import math
from dataclasses import dataclass
from itertools import chain
from typing import List, Tuple, Optional, Iterable, Iterator

from color_palate import Color

TOUCH_SEPARATION = 2
SAFETY_FACTOR = 2.5
# EPSILON = 0.01  # small value to detect touching circles
POSITION_VECTOR = [(0, 0), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)]


@dataclass(slots=True)
class Circle:
    x: int
    y: int
    radius: float
    color: Optional[Color] = None

    @property
    def center(self) -> Tuple[int, int]:
        return self.x, self.y


class CircleGrid:

    def __init__(self, width: int, height: int, cell_size: float):
        self._cell_size = cell_size * SAFETY_FACTOR
        self._height = int(height / cell_size)
        self._width = int(width / cell_size)

        self._grid = self.setup_grid()

    def setup_grid(self) -> List[List[List[Circle]]]:
        return [[[] for _ in range(self._width + 1)] for _ in range(self._height + 1)]

    def inside_circle(self, circle: Circle) -> bool:
        return any(
            self._are_intersecting(check_circle, circle)
            for check_circle in self._get_possible_intersections(circle)
        )

    def _get_possible_intersections(self, circle: Circle) -> Iterable[Circle]:
        cell_x, cell_y = int(circle.x // self._cell_size), int(circle.y // self._cell_size)
        return chain(*(
            self._grid[cell_y + y][cell_x + x]
            for x, y in POSITION_VECTOR
            if self._height > cell_y + y >= 0 and self._width > cell_x + x >= 0
        ))

    @staticmethod
    def _are_intersecting(c1: Circle, c2: Circle) -> bool:
        return math.sqrt((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2) <= TOUCH_SEPARATION + c1.radius + c2.radius

    def add(self, circle: Circle) -> None:
        assert circle.radius <= self._cell_size
        cell_x, cell_y = int(circle.x // self._cell_size), int(circle.y // self._cell_size)
        self._grid[cell_y][cell_x].append(circle)

    def __iter__(self) -> Iterator[Circle]:
        return iter(chain(*[chain(*row) for row in self._grid]))
