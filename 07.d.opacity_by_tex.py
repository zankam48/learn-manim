from manim import *

class TexOpacityExample(Scene):
    def construct(self):
        equation = MathTex(
            r"\Gamma(1 - z) \Gamma(z) = \frac{\pi}{\sin \pi z}",
            substrings_to_isolate=["z"],
        ).scale(2)
        self.play(Write(equation))
        self.wait()
        equation.save_state()
        self.play(
            equation.animate.set_opacity_by_tex("z", opacity=1, remaining_opacity=0.25)
        )
        self.wait()
        self.play(Restore(equation))
        self.wait()