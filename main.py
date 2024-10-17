from contextlib import contextmanager
from time import time

from color_blind_editor import draw_image
from color_palate import palates


@contextmanager
def timer():
    start = time()
    yield
    print(f'It took {time() - start:.3f}s to run the program.')


@timer()
def main() -> None:
    # for palate in color_palate.PALATES:
    #    draw_image('masks/mask2.png', color_palate=palate)
    draw_image('masks/mask2.png', color_palate=palates["Gray-Red"])


if __name__ == '__main__':
    main()
