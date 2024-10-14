import random
from collections.abc import Sequence
from dataclasses import dataclass
from typing import TypeAlias

Color: TypeAlias = str


@dataclass
class ColorPalate:
    name: str
    on_color: Sequence[Color]
    off_color: Sequence[Color]

    def get_random_color(self, on_mask: bool) -> Color:
        if on_mask:
            return random.choice(self.on_color)
        return random.choice(self.off_color)


# Protanopia (Red-Weak)
PROTANOPIA = ColorPalate(
    name="Protanopia",
    on_color=["#FF0000", "#D4A190", "#FFA07A"],  # Red shades (seen as brown or grey)
    off_color=["#00FF00", "#1E90FF", "#008080"]  # Green/Blue background
)

# Deuteranopia (Green-Weak)
DEUTERANOPIA = ColorPalate(
    name="Deuteranopia",
    on_color=["#FFCC00", "#FF9900", "#FF6600"],  # Yellow/orange shades (distorted green)
    off_color=["#008000", "#0066CC", "#3399FF"]  # Green/Blue background
)

# Tritanopia (Blue-Yellow Weakness)
TRITANOPIA = ColorPalate(
    name="Tritanopia",
    on_color=["#FFCC00", "#FFFF00", "#FFCC99"],  # Yellow tones (trouble with blue)
    off_color=["#800080", "#0066CC", "#4682B4"]  # Purple/Blue background
)

# Monochromacy (Complete Color Blindness)
MONOCHROMACY = ColorPalate(
    name="Monochromacy",
    on_color=["#666666", "#999999", "#CCCCCC"],  # Grayscale for number
    off_color=["#000000", "#333333", "#666666"]  # Grayscale background
)

# Red-Weak (Protanomaly)
PROTANOMALY = ColorPalate(
    name="Protanomaly",
    on_color=["#FF6347", "#FF4500", "#DC143C"],  # Muted reds
    off_color=["#00FA9A", "#1E90FF", "#4682B4"]  # Greens/Blues background
)

# Green-Weak (Deuteranomaly)
DEUTERANOMALY = ColorPalate(
    name="Deuteranomaly",
    on_color=["#FFFF00", "#FFD700", "#FFA500"],  # Muted yellow/oranges
    off_color=["#228B22", "#0000FF", "#00CED1"]  # Greens/Blues background
)

PALATES = [
    PROTANOPIA,
    DEUTERANOPIA,
    TRITANOPIA,
    MONOCHROMACY,
    PROTANOMALY,
    DEUTERANOMALY
]

# ==============================================================================
#                                manual color palates
# ==============================================================================


GRAY_PINK = ColorPalate(
    name="Gray-Pink",
    on_color=["#CC5267", "#E29E93", "#97506D", "#DE9091"],
    off_color=["#424340", "#B8B9B4", "#A0A199"]
)

GRAY_RED = ColorPalate(
    name="gray-red",
    on_color=[
        "#c45c6b",
        "#bc646b",
        "#c55a6e",
        "#934451",
        "#74383e",
        "#7f3c4d",
        "#a75044"
    ],
    off_color=[
        "#6c6c6b",
        "#7d656c",
        "#6b7253",
        "#53736b",
        "#6c6b7e",
        "#5c736b",
        "#3b4342",
        "#2c3c3c"
    ]
)


MANUAL_PALATES = [
    GRAY_PINK,
    GRAY_RED
]