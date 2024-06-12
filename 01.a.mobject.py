from manim import *

class MyScene(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.1)
        green_square = Square(color=GREEN)
        green_square.next_to(blue_circle, RIGHT)
        self.add(blue_circle, green_square)