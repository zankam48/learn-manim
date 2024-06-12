from manim import *
import numpy as np
from colour import Color
from manim.scene.scene import Scene

class AllUpdaterTypes(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        pointer = Arrow(ORIGIN, RIGHT).next_to(red_dot, LEFT)

        # place arrow left of dot
        pointer.add_updater(
            lambda mob: mob.next_to(red_dot, LEFT)
        )

        # make dot move 2 munits RIGHT/second
        def shifter(mob, dt):
            mob.shift(2*dt*RIGHT)
        red_dot.add_updater(shifter)

        # scale mobjects depending on distance to ORIGIN
        def scene_scaler(dt):
            for mob in self.mobjects:
                # 1  / (1 + distance)
                mob.set(width=2/(1 + np.linalg.norm(mob.get_center())))
        self.add_updater(scene_scaler)

        self.add(red_dot, pointer)
        self.update_self(0)
        self.wait(5)

class UpdaterAnimation(Scene):
    def construct(self):
        red_dot = Dot(color=RED).shift(LEFT)
        rotating_square = Square()
        rotating_square.add_updater(
            lambda mob, dt: mob.rotate(PI*dt)
        )

        def shifter(mob, dt):
            mob.shift(2*dt*RIGHT)
        red_dot.add_updater(shifter)

        self.add(red_dot, rotating_square)
        self.wait(1)
        red_dot.suspend_updating()
        self.wait(1)

        self.play(
            red_dot.animate.shift(UP),
            rotating_square.animate.move_to([-2, -2, 0])
        )
        self.wait(1)

# value tracker

class ValueTracker(Scene):
    def construct(self):
        a = ValueTracker(1)
        ax = Axes(x_range=[-2, 2, 1], y_range=[-8.5, 8.5, 1], x_length=4, y_length=6)
        parabola = ax.plot(lambda x: x**2, color=RED)
        parabola.add_updater(
            lambda mob: mob.become(ax.plot(lambda x: a.get_value() * x**2, color=RED))
        )
        a_number = DecimalNumber(
            a.get_value(),
            color=RED,
            num_decimal_places=3,
            show_ellipsis=True
        )
        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value()).next_to(parabola, RIGHT)
        )
        self.add(ax, parabola, a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))

class ValueTrackerPlot(Scene):
    def construct(self):
        ax = Axes(x_range=[-2, 2, 1], y_range=[-8.5, 8.5, 1], x_length=4, y_length=6)
        a = ValueTracker(1)

        parabola = ax.plot(lambda x: a.get_value() * x**2, color=RED)
        parabola.add_updater(
            lambda mob: mob.become(ax.plot(lambda x: a.get_value() * x**2, color=RED))
        )
        a_number = DecimalNumber(
            a.get_value(),
            color=RED,
            num_decimal_places=3,
            show_ellipsis=True
        )
        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value()).next_to(parabola, RIGHT)
        )
        self.add(ax, parabola, a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))

from manim import *

class ValueTrackerGPT(Scene):
    def construct(self):
        ax = Axes(x_range=[-2, 2, 1], y_range=[-8.5, 8.5, 1], x_length=4, y_length=6)
        a = ValueTracker(1)  # Moved inside construct

        parabola = always_redraw(lambda: ax.plot(
            lambda x: a.get_value() * x**2, color=RED
        ))

        a_number = always_redraw(lambda: DecimalNumber(
            a.get_value(),
            color=RED,
            num_decimal_places=3,
            show_ellipsis=True
        ).next_to(parabola, RIGHT))

        self.add(ax, parabola, a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))
