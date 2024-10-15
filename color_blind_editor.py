from pathlib import Path
from typing import Optional, Tuple, Literal

import plots
from color_palate import ColorPalate, Color, PROTANOPIA
from grid import Circle, CircleGrid
from image_mask import ImageMask
from randoms import get_random_circle, SPREAD_CEIL

RATE_DELTA = 0.2
MAX_ATTEMPTS = 1000
LAYER_LIMIT = 2500


class ColorBlindEditor:

    def __init__(
            self,
            *,
            reference_radius: float,
            radius_unit: Literal["abs", "per"],
            color_palate: ColorPalate,
            layers: int
    ):
        self._grid: Optional[CircleGrid] = None
        self._image_mask: Optional[ImageMask] = None

        self._radius_unit = radius_unit
        self._reference_radius = reference_radius
        self._palate = color_palate
        self._layers_num = layers

    def create(self, mask_path: str, dest_path: str) -> None:
        self._image_mask = ImageMask(mask_path)

        if self._radius_unit == "per":
            self._reference_radius = self._image_mask.size[0] * self._reference_radius

        max_radius = self._reference_radius * SPREAD_CEIL
        self._grid = CircleGrid(*self._image_mask.size, cell_size=max_radius)

        self._create_image()
        plots.plot(self._grid, dest_path)

    def _create_image(self) -> None:
        for _ in range(self._layers_num):
            self._create_layer()
            self._reference_radius -= RATE_DELTA * self._reference_radius

    def _create_layer(self, *, layer_limit: int = LAYER_LIMIT) -> None:
        while layer_limit > 0:
            random_circle = self._get_random_valid_circle(self._reference_radius)
            if random_circle is None:
                return

            random_circle.color = self._get_random_color(random_circle.center)
            self._grid.add(random_circle)
            layer_limit -= 1

    def _get_random_valid_circle(self, radius: float, *, attempts: int = MAX_ATTEMPTS) -> Optional[Circle]:
        while attempts > 0:
            random_circle = get_random_circle(*self._image_mask.size, reference_radius=radius)
            if not self._grid.inside_circle(random_circle):
                return random_circle
            attempts -= 1
        return None

    def _get_random_color(self, center: Tuple[int, int]) -> Color:
        on_mask = self._image_mask.on_mask(*center)
        return self._palate.get_random_color(on_mask)


def generate_output_file_name(mask_path: str, color_palate: ColorPalate) -> str:
    mask_path = Path(mask_path)
    return "images/" + mask_path.stem + "_" + color_palate.name + mask_path.suffix


def draw_image(
        mask_path: Path | str,
        dest_path: Path | str = None,
        *,
        reference_radius: int = 0.011,
        radius_unit: Literal["abs", "per"] = "per",
        color_palate: ColorPalate = PROTANOPIA,
        layers: int = 5
) -> None:
    if dest_path is None:
        dest_path = generate_output_file_name(mask_path, color_palate)
        print(dest_path)

    cbe = ColorBlindEditor(
        radius_unit=radius_unit,
        reference_radius=reference_radius,
        color_palate=color_palate,
        layers=layers)
    cbe.create(mask_path, dest_path)
