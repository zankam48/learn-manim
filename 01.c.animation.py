from manim import *
from manimpango import *

class MyScene(Scene):
    
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x)**2, color=RED)
        area = ax.get_area(curve, x_range=(-2, 0))
        self.play(Create(ax, run_time=1), Create(curve, run_time=3))
        self.play(FadeIn(area))
        self.wait(2)

class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.2)
        self.play(ReplacementTransform(green_square, blue_circle))
        self.play(Indicate(blue_circle))
        self.play(FadeOut(blue_circle))