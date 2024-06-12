from manim import *
import numpy as np
from colour import Color
from manim.scene.scene import Scene

class Disperse(Animation):
    def __init__(self, mobject, dot_radius=0.05, dot_number=100, **kwargs):
        super().__init__(mobject, **kwargs)
        self.dot_radius = dot_radius
        self.dot_number = dot_number
    
    def begin(self) -> None:
        dots = VGroup(
            *[Dot(radius=self.dot_radius).move_to(self.mobject.point_from_proportion(p))
              for p in np.linspace(0, 1, self.dot_number)]
        )
        for dot in dots:
            dot.initial_position = dot.get_center()
            dot.shift_vector = 2*(dot.get_center() - self.mobject.get_center())
        dots.set_opacity(0)
        self.mobject.add(dots)
        self.dots = dots
        super().begin()
    
    def clean_up_from_scene(self, scene: Scene) -> None:
        super().clean_up_from_scene(scene)
        scene.remove(self.dots)
    
    def interpolate_mobject(self, alpha: float) -> None:
        if alpha <= 0.5:
            self.mobject.set_opacity(1 - 2*alpha, family=False)
            self.dots.set_opacity(2*alpha)
        else:
            self.mobject.set_opacity(0)
            self.dots.set_opacity(2*(1 - alpha))
            for dot in self.dots:
                dot.move_to(dot.initial_position + 2*(alpha - 0.5) * dot.shift_vector)

class CustomAnimationExample(Scene):
    def construct(self):
        st = Star(color=YELLOW, fill_opacity=1).scale(3)
        self.add(st)
        self.wait()
        self.play(Disperse(st, dot_number=200, run_time=4))
