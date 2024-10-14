import random
from typing import Tuple

import numpy as np

from grid import Circle

MU = 1
SIGMA = 0.2
DELTA = 0.1
SPREAD_CEIL = MU + DELTA
SPREAD_FLOOR = MU - DELTA


def get_random_circle(
        width: int,
        height: int,
        reference_radius: float
) -> Circle:
    return Circle(
        *random_position(width, height),
        radius=random_size(reference_radius)
    )


def random_size(radius: float) -> float:
    noise = np.clip(np.random.normal(MU, SIGMA), SPREAD_FLOOR, SPREAD_CEIL)
    return radius * noise


def random_position(width: int, height: int) -> Tuple[int, int]:
    return (
        random.randint(0, width - 1),
        random.randint(0, height - 1)
    )
