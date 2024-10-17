from matplotlib import pyplot as plt

from grid import CircleGrid, Circle


def plot_circle(circle: Circle) -> None:
    circle_plot = plt.Circle(circle.center, circle.radius, color=circle.color)
    plt.gca().add_patch(circle_plot)


def plot(grid: CircleGrid, dest_path: str) -> None:
    for circle in grid:
        plot_circle(circle)

    plt.axis("off")
    plt.gca().set_aspect('equal')
    plt.gca().invert_yaxis()
    plt.style.use("dark_background")
    plt.autoscale(True, tight=True)
    plt.savefig(dest_path, bbox_inches='tight', pad_inches=-0.1)
    plt.close('all')


def __debug_plot(grid: CircleGrid, dest_path: str) -> None:
    c = Circle(250, 170, 2.1, color="black")
    for circle in grid:
        plot_circle(Circle(circle.x, circle.y, circle.radius, color="orange"))
    for circle in grid._get_possible_intersections(c):
        plot_circle(Circle(circle.x, circle.y, circle.radius, color="blue"))
    plot_circle(c)
    plt.gca().set_aspect('equal')
    plt.gca().invert_yaxis()
    plt.autoscale(True)
    plt.savefig(dest_path, bbox_inches='tight', pad_inches=0)
