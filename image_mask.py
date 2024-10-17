
from matplotlib import image as mpimg

BLACK_CUTOFF = 0.3


class ImageMask:

    def __init__(self, mask_path: str):
        self._image = mpimg.imread(mask_path)
        self._height, self._width, *_ = self._image.shape

    @property
    def size(self) -> tuple[int, int]:
        return self._width, self._height

    def on_mask(self, x: int, y: int) -> bool:
        assert 0 <= x < self._width and 0 <= y < self._height
        r, g, b, _ = self._image[y][x]
        return r < BLACK_CUTOFF and g < BLACK_CUTOFF and b < BLACK_CUTOFF
