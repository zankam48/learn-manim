from manim import *

class CustomAxes(Scene):
    def construct(self):
        ax = Axes(
            x_range=(0, 7),
            y_range=(-1, 1),
            axis_config={"tip_shape": StealthTip}
        )
        p = ax.plot_line_graph(
            x_values=np.linspace(0, 7, 140),
            y_values=np.cumsum(np.random.normal(0, 0.05, 140)),
            add_vertex_dots=False
        ).set(color=RED_C)
        self.add(ax, p)