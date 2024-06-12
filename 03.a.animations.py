from manim import *

from colour import Color

class BasicAnimation(Scene):
    def construct(self):
        polys = VGroup(
            *[RegularPolygon(5, radius=1, fill_opacity=0.5, 
                            color=BLUE) for j in range(5)]
        ).arrange(RIGHT)

        self.play(DrawBorderThenFill(polys), run_time=2)
        self.play(
            Rotate(polys[0], PI, rate_func=lambda t: t), # linear func
            Rotate(polys[1], PI, rate_func=smooth), # default behavior
            Rotate(polys[2], PI, rate_func=lambda t: np.sin(t*PI)),
            Rotate(polys[3], PI, rate_func=there_and_back),
            Rotate(polys[4], PI, rate_func=lambda t: 1 - abs(1 - 2*t)),
            run_time=2
        )
        self.wait()

class ConflictingAnimations(Scene):
    def construct(self):
        s = Square()
        self.add(s)
        self.play(Rotate(s, PI), Rotate(s, -PI), run_time=3)

def myHSV(hue, s = 0.96, v = 0.98):
            # hue should be in degrees i.e. 0 to 360
            return ManimColor.from_hsv([hue/360,s,v])

class LaggingGroup(Scene):
    def construct(self):
        squares = VGroup(*[Square(color=myHSV(j*20, 0.7, 0.5), fill_opacity=0.8) for j in range(20)])
        squares.arrange_in_grid(4, 5).scale(0.75)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.15))

class AnimateSyntax(Scene):
    def construct(self):
        s = Square(color=GREEN, fill_opacity=0.5)
        c = Circle(color=BLUE, fill_opacity=0.5)
        self.add(s, c)

        self.play(s.animate.shift(UP), c.animate.shift(DOWN))
        self.play(VGroup(s, c).animate.arrange(RIGHT, buff=1))
        self.play(c.animate(rate_func=linear).shift(RIGHT).scale(2))
    
class AnimateProblem(Scene):
     def construct(self):
          left_square = Square()
          right_square = Square()
          VGroup(left_square, right_square).arrange(RIGHT, buff=1)
          self.add(left_square, right_square)
          self.play(left_square.animate.rotate(PI), Rotate(right_square, PI), run_time=2)
          self.wait()

class AnimationMechanism(Scene):
    def construct(self):
        c = Circle()

        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2*RIGHT, UP).scale(0.5)

        self.add(c)
        self.wait()
        self.play(MoveToTarget(c))

        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(3))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4))
        self.wait()
        self.play(Restore(s), run_time=2)

        self.wait()

class SimpleCustomAnimation(Scene):
    def construct(self):
        def spiral_out(mobject, t):
            radius = 4
            angle = 2*t * 2*PI
            mobject.move_to(radius*(np.cos(angle)*RIGHT + np.sin(angle)*UP))
            mobject.set_color(color=BLUE)
            mobject.set_opacity(1-t)
        
        d = Dot(color=WHITE)
        self.add(d)
        self.play(UpdateFromAlphaFunc(d, spiral_out, run_time=3))