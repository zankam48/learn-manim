from manim import *

config.verbosity = "WARNING"

class DiGraphEX(Scene):
    def construct(self):
        D = DiGraph(
            [0, 1, 2, 3, 4, 5],
            [
                (0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
                (1, 3), (2, 0), (2, 4), (3, 5), 
            ],
            layout={
                0: 1*LEFT + 1*DOWN,
                1: 2*LEFT + 2*UP,
                2: 2*RIGHT + 2*DOWN,
                3: 2*RIGHT + 2*UP,
                4: 2*LEFT + 2*DOWN,
                5: 1*RIGHT + 3*UP,
            },
            labels=True,
            edge_config={
                "tip_config": {"tip_shape": StealthTip},
            }
        ).center()
        self.play(Create(D))
        self.wait()
        self.play(
            D.animate.change_layout('circular')
        )
        self.wait()

