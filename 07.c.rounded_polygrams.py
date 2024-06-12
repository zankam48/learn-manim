from manim import *

class RoundedPolygrams(Scene):
    def construct(self):
        st1 = Star().scale(2).round_corners((0.4, 0.1))
        st2 = Star().scale(2).round_corners((0.1, 0.4))
        st3 = Star().scale(2).round_corners((0.3, 0.3))
        stars = VGroup(st1, st2, st3).arrange(RIGHT)

        # poly = RegularPolygon

        self.add(stars)