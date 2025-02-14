from manim import *

class NewtonsLawofGravity(Scene):
    def construct(self):
        
        # Texts
        title = Text("Newton's Law of Universal Gravitation").scale(0.9)
        definition = Text(
            "Every point mass attracts every other point mass "
            "by a force acting along the line intersecting both points. "
            "The force is proportional to the product of the two masses "
            "and inversely proportional to the square of the distance between them:",
            t2c={"point mass": YELLOW, "force": BLUE},
        ).scale(0.5).next_to(title, DOWN * 1.5)
        
        formula = MathTex(
            "F =", "G", "{{m_1", "m_2}", "\\over", "{r^2}}").next_to(definition, DOWN)
        formula.set_color_by_tex("G", YELLOW)
        formula.set_color_by_tex("m_1m_2", RED)
        formula.set_color_by_tex("r^2", GREEN)
        
        # Animation
        self.play(Write(title))
        self.wait(1)
        self.play(Write(definition))
        self.wait(1)
        self.play(Write(formula))
        self.wait(3)

        # Explanation of constants and variables
        explanation = VGroup(
            Text("where", font_size=36),
            MathTex("F", "=", "\\text{Force between masses}").set_color(BLUE),
            MathTex("G", "=", "\\text{Gravitational Constant}").set_color(YELLOW),
            MathTex("m_1, m_2", "=", "\\text{Masses}").set_color(RED),
            MathTex("r", "=", "\\text{Distance between masses}").set_color(GREEN),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(formula, DOWN)

        self.play(Write(explanation))
        self.wait(2)
        
        # Visual demonstration
        mass1 = Circle(color=RED, fill_opacity=0.5).scale(0.5)
        mass1_label = MathTex("m_1").next_to(mass1, UP)
        mass2 = Circle(color=RED, fill_opacity=0.5).scale(0.5)
        mass2_label = MathTex("m_2").next_to(mass2, UP)
        distance_line = Line(mass1.get_center(), mass2.get_center()).set_color(WHITE)
        distance_label = MathTex("r").set_color(GREEN).move_to(distance_line.get_center() + UP * 0.2)
        
        self.play(
            FadeOut(explanation),
            FadeIn(mass1, shift=LEFT*3),
            FadeIn(mass2_label, shift=RIGHT*3),
            FadeIn(mass1_label),
            FadeIn(mass2),
        )
        self.wait(1)
        self.play(Create(distance_line), Write(distance_label))
        self.wait(2)
        
        # Summary
        summary = Text(
            "The force of gravity decreases with the square of the distance, "
            "but increases with the product of the masses.",
            color=BLUE,
        ).scale(0.5).next_to(formula, DOWN * 3)
        
        self.play(FadeIn(summary))
        self.wait(2)

        self.play(FadeOut(mass1, mass2, mass1_label, mass2_label, distance_line, distance_label, summary))
        self.wait(1)

        # End
        self.play(FadeOut(title), FadeOut(definition), FadeOut(formula))
        self.wait(1)

# To render the scene, uncomment the below line and run the script with 'manim' command.
# scene = NewtonsLawofGravity()
# scene.render()