import random
from collections.abc import Sequence
from typing import TypeAlias

import yaml
from pydantic import BaseModel

Color: TypeAlias = str


class ColorPalate(BaseModel):
    name: str
    subject: Sequence[Color]
    background: Sequence[Color]

    def get_random_color(self, on_mask: bool) -> Color:
        if on_mask:
            return random.choice(self.subject)
        return random.choice(self.background)


def load_palate(palate_data: dict) -> ColorPalate:
    return ColorPalate(name=palate_data["name"], **palate_data["colors"])


def read_yaml(yaml_path: str) -> dict[str, ColorPalate]:
    with open(yaml_path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    color_palates = [load_palate(palate) for palate in data["palates"]]
    return {palate.name: palate for palate in color_palates}


palates = read_yaml("palates.yaml")
