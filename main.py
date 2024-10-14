from contextlib import contextmanager
from time import time

import color_palate
from color_blind_editor import draw_image


@contextmanager
def timer():
    start = time()
    yield
    print(f'It took {time() - start:.3f}s to run the program.')


@timer()
def main() -> None:
    # for palate in color_palate.PALATES:
    #    draw_image('masks/mask2.png', color_palate=palate)
    draw_image('masks/mask2.png', color_palate=color_palate.GRAY_RED)


if __name__ == '__main__':
    main()
