import random
from collections.abc import Sequence
from dataclasses import dataclass
from typing import TypeAlias

Color: TypeAlias = str


@dataclass
class ColorPalate:
    on_color: Sequence[Color]
    off_color: Sequence[Color]

    def get_random_color(self, on_mask: bool) -> Color:
        if on_mask:
            return random.choice(self.on_color)
        return random.choice(self.off_color)


RED_GREEN = ColorPalate(
    on_color=("#00FF00", "#00CC00", "#008000"),
    off_color=("#FF0000", "#CC0000", "#800000")
)
