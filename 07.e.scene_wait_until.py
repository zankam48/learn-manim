from manim import *

class CircleInGrid(Scene):
    def construct(self):
        dots = VGroup(*[
            Dot() for _ in range(16*9)
        ]).arrange_in_grid(9, 16, buff=1)
        self.add(dots)

        growing_circle = Circle(0.1, color=PURPLE_D, fill_opacity=0.25).shift(0.1*LEFT + 0.3*UP)
        self.add(growing_circle)
        growing_circle.add_updater(lambda c, dt: c.scale_to_fit_width(c.width + dt))

        def number_of_dots_in_circle():
            return len([
                dot for dot in dots
                if np.linalg.norm(dot.get_center() - growing_circle.get_center()) < growing_circle.width/2
            ])
        
        for _ in range(15):
            dots_inside = number_of_dots_in_circle()
            self.wait_until(lambda: number_of_dots_in_circle() != dots_inside)
            growing_circle.suspend_updating()
            self.wait(0.5)
            growing_circle.resume_updating()