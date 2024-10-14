from contextlib import contextmanager
from time import time

from color_blind_editor import draw_image


@contextmanager
def timer():
    start = time()
    yield
    print(f'It took {time() - start:.3f}s to run the program.')


@timer()
def main() -> None:
    draw_image('masks/mask2.png', 'images/dest.png')


if __name__ == '__main__':
    main()
