from typing import Tuple

from matplotlib import image as mpimg

BLACK_CUTOFF = 0.3


class ImageMask:

    def __init__(self, mask_path):
        self._image = mpimg.imread(mask_path)
        self._height, self._width, *_ = self._image.shape

    @property
    def size(self) -> Tuple[int, int]:
        return self._width, self._height

    def on_mask(self, x: int, y: int) -> bool:
        r, g, b, _ = self._image[y][x]
        return r < BLACK_CUTOFF and g < BLACK_CUTOFF and b < BLACK_CUTOFF
