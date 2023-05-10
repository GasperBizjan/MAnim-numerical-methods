from manimlib.imports import *
import os
import pyclbr

# v cmd vpišemo: "cd C:\Program Files (x86)\MAnim\manim-master" brez " " (pomik v ustrezno mapo)
# v cmd vpišemo inicializacijski ukaz (npr. "python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl") za začetek scene
# iz # python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl lahko odstranimo l za HD render
# Vsaka scena je definirana z svojim Class-om


class Title(Scene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py Title -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        # 1 NASLOV
        naslov1 = TextMobject("Numerično reševanje diferencialnih enačb").set_color(
            YELLOW).scale(1.2).shift(2.8*UP)
        naslov2 = TextMobject("- začetni problem -").set_color(
            YELLOW).scale(1.10).shift(2.1*UP)
        naslov31 = TextMobject("Eulerjeva eksplicitna metoda").set_color(
            RED).scale(0.9).shift(1.8*DOWN+3.5*LEFT)
        naslov32 = TextMobject("Eulerjeva implicitna metoda").set_color(
            RED).scale(0.9).shift(1.8*DOWN+3.5*RIGHT)

        # 2 AVTORJI
        avtor1 = TextMobject("prof. dr. Janko Slavič")
        avtor2 = TextMobject("Gašper Bizjan")
        p1 = VGroup(avtor1, avtor2)
        p1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF).scale(0.7)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(naslov1))
        self.play(Write(naslov2))
        self.wait(1)
        self.play(
            Write(naslov31),
            Write(naslov32)
        )
        self.wait(2)
        self.play(
            Write(avtor1.shift(3.1*DOWN+5.0*LEFT)),
            Write(avtor2.next_to(avtor1, DOWN).shift(0.6*LEFT)),
        )
        self.wait(2)
        self.play(FadeOut(p1))
        self.play(FadeOut(naslov1), FadeOut(naslov2),
                  FadeOut(naslov31), FadeOut(naslov32))
        self.wait(5)


class Uvod(Scene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py Uvod -pl
    ### KONSTRUKCIJA VSEH OBJEKTOV ###
    def construct(self):
        vrstica1 = TextMobject("Rešujemo ", "diferencialno enačbo ").set_color_by_tex(
            "diferencialno enačbo", YELLOW)
        en1 = TexMobject("y'", "=", "f(", "t", ",", "y", ")", ",")
        en1.set_color_by_tex_to_color_map({
            "y'": RED, "f(": RED, "t": GREEN, "y": YELLOW, ")": RED
        })
        vrstica2 = TextMobject("pri ", "začetnem pogoju").set_color_by_tex(
            "začetnem pogoju", YELLOW)
        en2 = TexMobject("y(", "t_0", ")", "=", "y_0", ".")
        en2.set_color_by_tex_to_color_map({
            "y(": YELLOW, "f(": RED, "t_0": TEAL, ")": YELLOW, "y_0": TEAL
        })

    ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(vrstica1.shift(3*UP+3*LEFT)))
        self.play(Write(en1.shift(2*UP)))
        self.wait(3)
        self.play(Write(vrstica2.shift(4*LEFT)))
        self.play(Write(en2.shift(1*DOWN)))
        self.wait(5)


class KonkretniPrimer(Scene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py KonkretniPrimer -pl
    ### KONSTRUKCIJA VSEH OBJEKTOV ###
    def construct(self):
        ## Slika ##
        # žoga
        ball1 = Circle(color=BLUE, opacity=0.5,
                       fill_color=BLUE, fill_opacity=1)
        ball2 = Circle(color=BLUE, fill_color=WHITE, fill_opacity=0.5).scale(
            0.7).shift(0.1*UP+0.2*LEFT)
        ball3 = Circle(color=WHITE, fill_color=WHITE, fill_opacity=1).scale(
            0.2).shift(0.4*UP+0.4*LEFT)
        ball = VGroup(ball1, ball2, ball3).scale(1.1).shift(UP)
        # vektorji
        line_g = Arrow(UP, DOWN)
        g = TexMobject("\\vec g").shift(1.1*DOWN)
        vec_g = VGroup(line_g, g).shift(2*LEFT+1.5*UP).set_color(GREEN)
        line_v = Arrow(UP, DOWN)
        v = TexMobject("\\vec v").shift(1.1*DOWN)
        vec_v = VGroup(line_v, v).shift(2*DOWN).set_color(YELLOW)
        line_cv = Arrow(DOWN, UP)
        cv = TexMobject("c \, \\vec v").shift(0.5*DOWN+0.5*LEFT)
        vec_cv = VGroup(line_cv, cv).shift(0.5*LEFT).set_color(YELLOW)
        line_mg = Arrow(UP, DOWN)
        mg = TexMobject("m \, \\vec g").shift(0.5*DOWN+0.7*RIGHT)
        vec_mg = VGroup(line_mg, mg).shift(0.5*RIGHT).set_color(RED)
        slika = VGroup(ball, vec_g, vec_v, vec_cv, vec_mg)
        # dejanske količine
        masa = TexMobject("m = 1 \\textrm{ kg}").shift(0.6*LEFT).set_color(RED)
        gravitacija = TexMobject(
            "g = 9.81\\textrm{m/s}^2").shift(0.6*DOWN).set_color(RED)
        faktor_c = TexMobject(
            "c=0.5 \\textrm{ kg/s}").shift(1.3*DOWN).set_color(RED)
        enote = VGroup(masa, gravitacija, faktor_c).shift(1.7*DOWN+2.8*RIGHT)

        ## enačbe ##
        en11 = TexMobject("\\sum_i ").shift(1.3*LEFT+0.2*DOWN)
        en12 = TexMobject("\\vec F_i = ", "m \,", " \\vec a")
        en12.set_color_by_tex_to_color_map(
            {"\\vec F_i =": WHITE, "m \,": RED, "\\vec a": YELLOW})
        en1 = VGroup(en11, en12).shift(2.2*UP+1.15*RIGHT)

        m21 = TexMobject("m").set_color(RED)
        g2 = TexMobject("\\vec g").next_to(m21, 0.5*RIGHT).set_color(RED)
        minus2 = TexMobject("-").next_to(g2, 0.5*RIGHT)
        c2 = TexMobject("c").next_to(minus2, 0.5*RIGHT).set_color(RED)
        v2 = TexMobject("\\vec v").next_to(c2, 0.5*RIGHT).set_color(YELLOW)
        enacaj2 = TexMobject("=").next_to(v2, 0.5*RIGHT)
        m22 = TexMobject("m").next_to(enacaj2, 0.5*RIGHT).set_color(RED)
        a2 = TexMobject("\\vec a").next_to(m22, 0.5*RIGHT).set_color(YELLOW)
        v2.shift(0.06*UP)
        a2.shift(0.06*UP)
        en2 = VGroup(m21, g2, minus2, c2, v2, enacaj2,
                     m22, a2).shift(1*UP+LEFT)

        v2_odv = TexMobject("\\vec v^{'} ").set_color(
            YELLOW).move_to(m22, RIGHT).shift(0.15*UP+0.43*RIGHT)

        g3 = TexMobject(r"\begin{pmatrix} 0 \\ g \end{pmatrix}").set_color(
            RED).shift(UP+1.25*LEFT)
        v3 = TexMobject(r"\begin{pmatrix} 0 \\ v \end{pmatrix}").set_color(
            YELLOW).shift(UP+0.4*RIGHT)
        v3_odv = TexMobject(r"\begin{pmatrix} 0 \\ v' \end{pmatrix}").set_color(
            YELLOW).shift(UP+2.3*RIGHT)

        en4 = TexMobject("m \, g", "-", "c\,", "v", "=", "m \,",
                         "v'").shift(0.2*DOWN+0.5*RIGHT)
        en4.set_color_by_tex_to_color_map({
            "m \, g": RED, "c\,": RED, "v": YELLOW, "m \,": RED, "v'": YELLOW
        })

        # analitična rešitev
        tekst1 = TextMobject("Glede na ", "začetni pogoj", ":")
        tekst1.set_color_by_tex("začetni pogoj", YELLOW).scale(
            0.8).shift(1.45*LEFT+2*UP)
        zp = TexMobject(
            "v(0)=0 \\textrm{ m/s},").scale(0.8).shift(2*RIGHT+2*UP).set_color(YELLOW)
        tekst2 = TextMobject(
            "ima zgornja diferencialna enačba ", "analitično rešitev", ":")
        tekst2.set_color_by_tex("analitično rešitev", YELLOW).scale(
            0.8).shift(1*RIGHT+1.5*UP)
        en5 = TexMobject(
            "v(", "t", ")", "=", "\\frac{m\,g}{c}", "\\left(1 -", "e^{-", "\\frac{c}{m}",  "t}", "\\right)")
        en5.shift(1.0*LEFT+0.5*UP)
        en5.set_color_by_tex_to_color_map({
            "v(": YELLOW,
            "t": GREEN,
            ")": YELLOW,
            "=": WHITE,
            "\\frac{m\,g}{c}": RED,
            "\\left(1 -": WHITE,
            "e^{-": WHITE,
            "\\frac{c}{m}": RED,
            "t}": GREEN,
            "\\right)": WHITE
        })

    ### ANIMIRANJE OBJEKTOV ###
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py KonkretniPrimer -pl
        self.play(DrawBorderThenFill(ball))
        self.play(GrowArrow(line_g), Write(g))
        self.play(GrowArrow(line_v), Write(v))
        self.play(GrowArrow(line_cv), Write(cv))
        self.play(GrowArrow(line_mg), Write(mg))
        self.wait(2)
        self.play(Write(enote))
        self.wait(2)
        self.play(FadeOut(enote), ApplyMethod(slika.scale, 0.7))
        self.play(ApplyMethod(slika.shift, 5*LEFT+2*UP))
        self.play(Write(en1))
        self.wait(1)
        self.play(Write(en2))
        self.wait(1)
        self.play(Transform(a2, v2_odv))
        self.wait(1)
        self.play(
            FadeOut(en1),
            ApplyMethod(m21.shift, 0.95*LEFT),
            ApplyMethod(c2.shift, 0.5*LEFT),
            ApplyMethod(minus2.shift, 0.5*LEFT),
            Transform(g2, g3),
            Transform(v2, v3),
            Transform(a2, v3_odv)
        )
        self.wait(1)
        self.play(Transform(en2, en4))
        self.wait(1)
        self.play(ApplyMethod(en2.shift, 3*UP+2.35*LEFT), Write(tekst1))
        self.play(Write(tekst2), Write(zp))
        self.play(Write(en5))
        self.wait(5)


class KonkretniPrimerAnalitika(GraphScene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py KonkretniPrimerAnalitika -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 11,
        "x_axis_width": 10,
        "x_tick_frequency": 10,
        "x_axis_label": "$t$",
        "y_min": 0,
        "y_max": 25,
        "y_tick_frequency": 5,
        "y_axis_height": 6,
        "graph_origin": 6*LEFT+3*DOWN,
        "axes_color": WHITE,
        "y_axis_label": "$v(t)$",
        "x_labeled_nums": list(np.arange(0, 12, 2)),
        "y_labeled_nums": range(0, 50, 5),
        "exclude_zero_label": True,
        "default_graph_colors": [YELLOW],
        "x_label_decimals": 0,
    }

    def analiticna_resitev(self, t):
        m = 1
        c = 0.5
        g = 9.81
        return m*g/c*(1-np.e**(-c/m*t))

    # KONSTRUKCIJA VSEH OBJEKTOV ##

    def construct(self):
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        analit_graph = self.get_graph(self.analiticna_resitev)
        analit_lab = self.get_graph_label(analit_graph, label=f"v_a(t)")

        ### ANIMIRANJE OBJEKTOV ###
        self.setup_axes(animate=True, hideaxes=False)
        self.play(ShowCreation(analit_graph),
                  ShowCreation(analit_lab.shift(UP+2*LEFT)))
        self.wait(5)


class PrehodMedMetodamiEksplicitna(Scene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py PrehodMedMetodamiEksplicitna -pl
    def construct(self):
        # 1 NASLOV
        naslov1 = TextMobject("Numerično reševanje diferencialnih enačb").set_color(
            YELLOW).scale(1.2).shift(2.8*UP)
        naslov2 = TextMobject("- začetni problem -").set_color(
            YELLOW).scale(1.10).shift(2.1*UP)
        naslov31 = TextMobject("Eulerjeva eksplicitna metoda").set_color(
            RED).scale(0.9).shift(1.8*DOWN+3.5*LEFT)
        naslov32 = TextMobject("Eulerjeva implicitna metoda").set_color(
            RED).scale(0.9).shift(1.8*DOWN+3.5*RIGHT)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(naslov1), Write(naslov2),
                  Write(naslov31), Write(naslov32))
        self.wait(1)
        self.play(FadeOut(naslov1), FadeOut(naslov2),
                  FadeOut(naslov32))
        self.play(ApplyMethod(naslov31.shift, 3.5*RIGHT+1*DOWN))
        self.play(ApplyMethod(naslov31.scale, 1.4))
        self.wait(5)


class EksplicitnaMetodaIzpeljava(Scene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py EksplicitnaMetodaIzpeljava -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        vrstica1 = TextMobject("Eksplicitna Eulerjeva metoda ", "temelji na razvoju funkcije ", r"$y$", " v", " Taylorjevo vrsto", ":"
                               ).set_color_by_tex_to_color_map({
                                   "Eksplicitna Eulerjeva metoda ": YELLOW,
                                   r"$y$": YELLOW,
                                   " Taylorjevo vrsto": BLUE,
                               }).scale(0.8).shift(3*UP)

        en1 = TexMobject(
            "y(", "t", "+", "h", ")", "=",
            "y(", "t", ")", "+",
            "y'(", "t", ",", "y(", "t", ")", ")", "h", "+", "O^2", "[", "h^2", "]")
        en1.set_color_by_tex_to_color_map({
            "y(": YELLOW, ")": YELLOW, "(": YELLOW,
            "[": BLUE, "]": BLUE,
            "+": WHITE, "-": WHITE, "=": WHITE,
            "t": GREEN, "h": BLUE,
            "O^2": BLUE
        })
        en21 = TexMobject("y(", "t", "+", "h", ")")
        en21.set_color_by_tex_to_color_map(
            {"y(": YELLOW, ")": YELLOW, "(": YELLOW, "t": GREEN, "h": BLUE})
        en22 = TexMobject(
            "=",
            "y(", "t", ")", "+",
            "y'(", "t", ",", "y(", "t", ")", ")", "h")
        en22.set_color_by_tex_to_color_map({
            "y(": YELLOW, ")": YELLOW, "(": YELLOW,
            "[": BLUE, "]": BLUE,
            "+": WHITE, "-": WHITE, "=": WHITE,
            "t": GREEN, "h": BLUE,
            "O^2": BLUE
        })
        en23 = TexMobject(
            "+", "O^2", "[", "h^2", "]")
        en23.set_color_by_tex_to_color_map({
            "y(": YELLOW, ")": YELLOW, "(": YELLOW,
            "[": BLUE, "]": BLUE,
            "+": WHITE, "-": WHITE, "=": WHITE,
            "t": GREEN, "h": BLUE,
            "O^2": BLUE
        })
        en2 = VGroup(en21, en22, en23)
        en2.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF/2)

        # podtekst
        line_11 = Line((0, 0, 0), (0, -1/2, 0)).shift(0.5*UP+0.75*LEFT)
        line_12 = Arrow(LEFT, RIGHT)
        tekst_1 = TextMobject("odvodi višjih redov").shift(
            2.8*RIGHT).scale(0.9)
        podpis1 = VGroup(line_11, line_12, tekst_1)
        podpis1.scale(0.9).set_color(BLUE).shift(2.3*RIGHT+1.2*UP)

        line_21 = Line((0, 0, 0), (0, -1.5, 0)).shift(1.5 *
                                                      UP+0.75*LEFT).set_color(YELLOW)
        line_22 = Arrow(LEFT, RIGHT).set_color(YELLOW)
        tekst_2 = TextMobject("odvod prvega reda").shift(
            2.8*RIGHT).scale(0.9).set_color(YELLOW)
        tekst_22 = TexMobject("y'(", "t", ")=", "f(", "t", ",", "y", ")").shift(
            2.8*RIGHT+0.5*DOWN)
        tekst_22.set_color_by_tex_to_color_map(
            {"y'(": YELLOW, "t": GREEN, ")=": YELLOW, "y": YELLOW, "f(": RED, ").": RED})
        podpis2 = VGroup(line_21, line_22, tekst_2, tekst_22)
        podpis2.scale(0.9).shift(0.5*LEFT+0.3*UP)

        line_31 = Arrow(UP, 2*DOWN)
        tekst_3 = TexMobject("\\textrm{časovni korak } h").shift(
            2.1*DOWN).scale(0.9)
        podpis3 = VGroup(line_31, tekst_3)
        podpis3.scale(0.9).set_color(BLUE).shift(3.95*LEFT+1.1*UP)
        # časovnica
        cas = Arrow((-3, 0, 0), (3, 0, 0))
        dot1 = Dot().shift(2.1*LEFT)
        dot2 = Dot().shift(1.8*RIGHT)
        dot = VGroup(dot1, dot2)
        ti1 = TexMobject("t_i").next_to(dot1, UP)
        ti2 = TexMobject("t_{i+1}").next_to(dot2, UP)
        oklepaj = Brace(dot, DOWN)
        h = TexMobject("h").next_to(oklepaj, DOWN)
        casovnica = VGroup(cas, dot, ti1, ti2, oklepaj,
                           h).set_color(BLUE).shift(3*LEFT+2*DOWN)

        en4 = TexMobject("\\cancel{+O^2[h^2]}").set_color(BLUE)

        # diskretna oblika
        vrstica2 = TextMobject(
            "Eksplicitna Eulerjeva metoda ", "v ", "diskretni obliki", ":")
        vrstica2.set_color_by_tex("Eksplicitna Eulerjeva metoda ", YELLOW).set_color_by_tex(
            "diskretni obliki", BLUE)
        vrstica2.shift(3*UP+2.7*LEFT).scale(0.8)

        en5 = TexMobject("y_{i+1}", "=", "y_i", "+",
                         "f(", "t_i", ",", "y_i", ")", "h")
        en5.shift(2.00*UP+4.0*LEFT)
        en5.set_color_by_tex_to_color_map({
            "y_{i+1}": YELLOW,
            "y_i": TEAL,
            "f(": RED,
            "t_i": GREEN,
            ")": RED,
            "h": BLUE
        })

        vrstica3 = TextMobject("Koraki Eulerjeve metode:").scale(
            0.8).shift(0.7*UP+LEFT*4).set_color(YELLOW)
        vrstica41 = TexMobject("\\textrm{1.", "Postavimo }", "\,i=0:",
                               "\,t_0,", "\,y_0", "=", "y(", "t_0", ")").shift(2.95*LEFT)
        vrstica41.set_color_by_tex_to_color_map({
            "\\textrm{1.": RED, "\,i=0:": BLUE, "\,t_0,": TEAL, "\,y_0": TEAL, "y(": YELLOW, ")": YELLOW
        })
        vrstica42 = TexMobject("\\textrm{2.}", "\\textrm{ Izračun vrednosti funkcije pri }",
                               "\,t_{i+1}=t_i+", "h.").shift(1.65*LEFT+0.6*DOWN)
        vrstica42.set_color_by_tex_to_color_map({
            "\\textrm{2.}": RED, "\,t_{i+1}=t_i+": TEAL, "h": BLUE
        })
        vrstica43 = TexMobject(
            "\\textrm{3. }", "\,i=i+1").shift(1.2*DOWN+5.45*LEFT)
        vrstica43.set_color_by_tex_to_color_map({
            "\\textrm{3.": RED, "\,i=i+1": TEAL
        })
        vrstica4 = VGroup(vrstica41, vrstica42, vrstica43).scale(0.8)

        l1 = Line((-5.5, 0.5, 0), (2, 0.5, 0))
        l2 = Line((2, 0.5, 0), (2, 1, 0))
        l3 = Arrow((2.25, 1, 0), (0, 1, 0))
        l = VGroup(l1, l2, l3).set_color(BLUE).shift(1.6*DOWN+2.3*RIGHT)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py EksplicitnaMetodaIzpeljava -pl
        self.play(Write(vrstica1))
        self.wait(1)
        self.play(Write(en2.shift(2*UP+1.3*LEFT)))
        self.play(ShowCreation(podpis1))
        self.play(ShowCreation(podpis2))
        self.play(ShowCreation(podpis3))
        self.play(ShowCreation(cas))
        self.play(ShowCreation(dot1), Write(ti1))
        self.play(ShowCreation(oklepaj), ShowCreation(h))
        self.play(ShowCreation(dot2), Write(ti2))
        self.wait(2)
        self.play(Transform(en23, en4.shift(2*UP+2.00*RIGHT)))
        self.wait(1)
        self.play(FadeOut(en23), FadeOut(podpis1))
        self.play(Transform(vrstica1, vrstica2))
        self.wait(1)
        self.play(
            Transform(en21, en5), Transform(en22, en5),
            FadeOut(podpis2), FadeOut(podpis3),
            ApplyMethod(casovnica.shift, 4*UP+5*RIGHT)
        )
        self.play(Write(vrstica3))
        self.play(Write(vrstica4))
        self.play(ShowCreation(l))
        self.wait(5)


class IzrisEksplicitna(GraphScene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py IzrisEksplicitna -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 2,
        "x_axis_width": 8,
        "x_tick_frequency": 0.25,
        "x_axis_label": "",
        "y_min": 0,
        "y_max": 15,
        "y_tick_frequency": 1,
        "y_axis_height": 4.5,
        "graph_origin": 5.4*LEFT+2.4*DOWN,
        "y_axis_label": "",
        "x_labeled_nums": list(np.arange(0, 2.1, 0.5)),
        "y_labeled_nums": range(0, 16, 5),
        "exclude_zero_label": True,
        "default_graph_colors": [YELLOW],
        "x_label_decimals": 1,
    }

    def get_point_to_graph(
        self,
        x, graph,
        line_class=SmallDot,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_line_to_graph(
        self,
        x1, x2, graph,
        line_class=Line,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x1, graph),
            self.input_to_graph_point(x2, graph),
            **line_kwargs
        )

    def get_v_dashed_line_to_graph(
        self,
        x, graph,
        line_class=DashedLine,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.coords_to_point(x, 0),
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_h_dashed_line_to_graph(
        self,
        x, y, graph,
        line_class=DashedLine,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x, graph),
            self.coords_to_point(0, y),
            **line_kwargs
        )

    def analiticna_resitev(self, t):
        m = 1
        c = 0.5
        g = 9.81
        return m*g/c*(1-np.e**(-c/m*t))

    def interpolacija(self, t):
        return -0.0510937*t**4 + 0.562031*t**3 - 3.20613*t**2 + 11.2789*t

    def f_zračni_upor(t, y, g=9.81, m=1., c=0.5):
        return g-c*y/m

    def euler(f, t, y0, *args, **kwargs):
        y = np.zeros_like(t)
        y[0] = y0
        h = t[1]-t[0]
        for i in range(len(t)-1):
            y[i+1] = y[i] + f(t[i], y[i], *args, **kwargs) * h
        return y

    t = np.linspace(0, 2, 5)
    v_rez = euler(f_zračni_upor, t, y0=0)

    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        # pretvorba primera v shemo
        vrstica1 = TextMobject(
            "Diferencialno enačbo padajočega telesa pretvorimo v ustrezno obliko:")
        vrstica1.scale(0.8)
        vrstica2 = TextMobject(
            "in jo uporabimo v Eulerjevi eksplicitni metodi:")
        vrstica2.scale(0.8)
        en1 = TexMobject("m \, g", "-", "c \,", "v", "=", "m \,", "v'")
        en1.set_color_by_tex_to_color_map({
            "m \, g": RED, "c \,": RED, "v": YELLOW, "m \,": RED, "v'": YELLOW
        })
        en2 = TexMobject("v'", "=", "g", "-", "\\frac{c}{m}", "v")
        en2.set_color_by_tex_to_color_map({
            "g": RED, "frac{c}{m}": RED, "v": YELLOW, "m": RED, "v'": YELLOW
        })
        en31 = TexMobject("v", "=", "v(", "t_i", ")", "=", "y_i")
        en31.set_color_by_tex_to_color_map(
            {"v": YELLOW, "t_i": TEAL, ")": YELLOW, "y_i": TEAL})
        en32 = TexMobject("v'", "=", "y'", "=", "f(", "t_i",
                          ",", "y_i", ")").shift(0.8*DOWN+0.3*RIGHT)
        en32.set_color_by_tex_to_color_map(
            {"v'": YELLOW, "y'": YELLOW, "f(": RED, "t_i": TEAL, "y_i": TEAL, ")": RED})
        en3 = VGroup(en31, en32)

        en41 = TexMobject("y_{i+1}", "=", "y_i", "+",
                          "f(", "t_i", ",", "y_i", ")", "h")
        en41.set_color_by_tex_to_color_map({
            "y_{i+1}": YELLOW,
            "y_i": TEAL,
            "f(": RED,
            "t_i": GREEN,
            ")": RED,
            "h": BLUE
        })
        en42 = TexMobject("v_{i+1}", "=", "v_i", "+",
                          "\\big(", "g-\\frac{c}{m}", "v_i", "\\big)", "h")
        en42.set_color_by_tex_to_color_map({
            "v_{i+1}": YELLOW,
            "v_i": TEAL,
            "g-\\frac{c}{m}": RED,
            "\\big(": RED,
            "\\big)": RED,
            "h": BLUE
        }).shift(0.9*DOWN+0.35*RIGHT)
        en4 = VGroup(en41, en42).shift(DOWN)

        ## PRVA ITERACIJA ##
        # Zgornji tekst
        i1 = TexMobject(
            "i=0:", "\,v_0=v(t_0=0\\textrm{ s})=0\\textrm{ m/s}", "\\textrm{ (Začetni pogoj)}")
        i1.set_color_by_tex_to_color_map(
            {"i=0:": BLUE, "\,v_0=v(t_0=0\\textrm{ s})=0\\textrm{ m/s}": TEAL})
        i1.shift(3.6*UP+2.6*LEFT).scale(0.8)
        izracun11 = TexMobject(
            "= \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, +",
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)",
            "\cdot", "0.5\\textrm{ s}"
        )
        izracun11.scale(0.8).set_color_by_tex_to_color_map({
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)": RED,
            "0.5\\textrm{ s}": BLUE
        })
        v11 = TextMobject(
            "0\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.65*LEFT)
        v12 = TextMobject(
            "0\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.7*RIGHT)
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        # osi
        x_os = TexMobject("t\\textrm{ [s]}").scale(
            0.8).shift(2.4*DOWN+3.3*RIGHT)
        y_os = TexMobject(
            "v(t)\\textrm{ [m/s]}").scale(0.8).rotate(PI/2).shift(6.3*LEFT)
        analit_graph = self.get_graph(self.analiticna_resitev)
        dashed_analit_graph = DashedVMobject(analit_graph).set_color(WHITE)
        analit_lab = self.get_graph_label(
            analit_graph, label=f"v_a(t)").set_color(WHITE)
        interpolacija_graf = self.get_graph(self.interpolacija)
        #
        x0 = 0.01
        x1 = 0.5
        y0 = 0
        tocka1L = self.get_point_to_graph(x0, interpolacija_graf, color=TEAL)
        linija1Lv = self.get_v_dashed_line_to_graph(
            x0, interpolacija_graf, color=TEAL)
        linija1Lh = self.get_h_dashed_line_to_graph(
            x0, self.interpolacija(x0), interpolacija_graf, color=TEAL)
        tocka1D = self.get_point_to_graph(x1, interpolacija_graf, color=YELLOW)
        linija1Dv = self.get_v_dashed_line_to_graph(
            x1, interpolacija_graf, color=BLUE)
        linija1Dh = self.get_h_dashed_line_to_graph(
            x1, self.interpolacija(x1), interpolacija_graf, color=YELLOW)
        presecisce1 = self.input_to_graph_point(x0, interpolacija_graf)
        ravna_linija1 = Line(
            presecisce1, (presecisce1[0]+1.22, presecisce1[1], 0)).set_color(RED)
        kot1 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle1 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot1
        )
        angle1.add_tip().scale(0.6).shift(9.7*LEFT+2.60*DOWN).set_color(RED)
        angle_label1 = TexMobject("v_0'").set_color(RED)
        angle_label1.scale(0.8).next_to(angle1, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka1L, tocka1D).set_color(RED)
        #
        input_triangle_p1 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p1 = RegularPolygon(n=3, start_angle=0).set_color(TEAL)
        input_triangle_p2 = input_triangle_p1.copy().set_color(TEAL)
        output_triangle_p2 = RegularPolygon(
            n=3, start_angle=TAU / 2).set_color(YELLOW)
        for triangle in input_triangle_p1, output_triangle_p1, input_triangle_p2, output_triangle_p2:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p2.set_fill(YELLOW, 1)
        x_label_p1 = TexMobject("t_0").scale(0.8).set_color(TEAL)
        output_label_p1 = TexMobject("v_0").scale(0.8).set_color(TEAL)
        x_label_p2 = TexMobject("t_1").scale(0.8).set_color(TEAL)
        output_label_p2 = TexMobject(
            "v_1=4,9\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        output_label_p22 = TexMobject(
            "v_1=4,9\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p1.next_to(linija1Lv, DOWN)
        x_label_p2.next_to(linija1Dv, RIGHT)
        output_label_p1.next_to(linija1Lh, LEFT)
        output_label_p2.next_to(linija1Dh, UP)
        output_label_p22.next_to(linija1Dh, UP)
        input_triangle_p1.next_to(linija1Lv, DOWN, buff=0)
        input_triangle_p2.next_to(linija1Dv, DOWN, buff=0)
        output_triangle_p1.next_to(linija1Lh, LEFT, buff=0)
        output_triangle_p2.next_to(linija1Dh, LEFT, buff=0).shift(0.15*RIGHT)
        h_oklepaj = Brace(VGroup(input_triangle_p1, input_triangle_p2), DOWN).shift(
            0.3*DOWN).set_color(BLUE)
        h_napis = h_oklepaj.get_text("$h$").scale(
            0.8).shift(0.2*UP).set_color(BLUE)

        ## DRUGA ITERACIJA ##
        # Zgornji tekst
        i2 = TexMobject("i=1:").set_color(BLUE)
        i2.shift(3.6*UP+6.2*LEFT).scale(0.8)
        izracun2 = TexMobject(
            "= \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, +",
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)",
            "\cdot", "0.5\\textrm{ s}"
        )
        izracun2.scale(0.8).shift(2.9*UP+2.65*RIGHT).set_color_by_tex_to_color_map({
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)": RED,
            "0.5\\textrm{ s}": BLUE})
        v21 = TextMobject(
            "4.9\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.55*LEFT)
        v22 = TextMobject(
            "4.9\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.95*RIGHT)
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        analit_graph = self.get_graph(self.analiticna_resitev)
        dashed_analit_graph = DashedVMobject(analit_graph).set_color(WHITE)
        analit_lab = self.get_graph_label(
            analit_graph, label=f"v_a(t)").set_color(WHITE)
        interpolacija_graf = self.get_graph(self.interpolacija)
        #
        x0 = 0.5
        x1 = 1.0
        y0 = 4.905
        tocka2L = self.get_point_to_graph(x0, interpolacija_graf, color=TEAL)
        linija2Lv = self.get_v_dashed_line_to_graph(
            x0, interpolacija_graf, color=TEAL)
        linija2Lh = self.get_h_dashed_line_to_graph(
            x0, self.interpolacija(x0), interpolacija_graf, color=TEAL)
        tocka2D = self.get_point_to_graph(x1, interpolacija_graf, color=YELLOW)
        linija2Dv = self.get_v_dashed_line_to_graph(
            x1, interpolacija_graf, color=BLUE)
        linija2Dh = self.get_h_dashed_line_to_graph(
            x1, self.interpolacija(x1), interpolacija_graf, color=YELLOW)
        presecisce2 = self.input_to_graph_point(x0, interpolacija_graf)
        ravna_linija2 = Line(
            presecisce2, (presecisce2[0]+1.22, presecisce2[1], 0)).set_color(RED)
        kot2 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle2 = Arc(
            radius=5.5,
            start_angle=0.05,
            angle=kot2-0.05
        )
        angle2.add_tip().scale(0.6).shift(7.65*LEFT+1.38*DOWN).set_color(RED)
        angle_label2 = TexMobject("v_1'").set_color(RED)
        angle_label2.scale(0.8).next_to(angle2, RIGHT).shift(0.2*LEFT)
        linija_odvod2 = Line(tocka2L, tocka2D).set_color(RED)
        #
        input_triangle_p3 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p3 = RegularPolygon(n=3, start_angle=0).set_color(TEAL)
        input_triangle_p4 = input_triangle_p1.copy().set_color(TEAL)
        output_triangle_p4 = RegularPolygon(
            n=3, start_angle=TAU / 2).set_color(YELLOW)
        for triangle in input_triangle_p3, output_triangle_p3, input_triangle_p4, output_triangle_p4:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p4.set_fill(YELLOW, 1)
        x_label_p3 = TexMobject("t_1").scale(0.8).set_color(TEAL)
        output_label_p3 = TexMobject("v_1").scale(0.8).set_color(TEAL)
        x_label_p4 = TexMobject("t_2").scale(0.8).set_color(TEAL)
        output_label_p4 = TexMobject(
            "v_2=8.6\\textrm{ m/s}").scale(0.7).set_color(YELLOW)
        output_label_p42 = TexMobject(
            "v_2=8.6\\textrm{ m/s}").scale(0.7).set_color(YELLOW)
        x_label_p3.next_to(linija2Lv, RIGHT)
        x_label_p4.next_to(linija2Dv, RIGHT)
        output_label_p3.next_to(linija2Lh, UP)
        output_label_p4.next_to(linija2Dh, UP)
        output_label_p42.next_to(linija2Dh, UP)
        input_triangle_p3.next_to(linija2Lv, DOWN, buff=0)
        input_triangle_p4.next_to(linija2Dv, DOWN, buff=0)
        output_triangle_p3.next_to(linija2Lh, LEFT, buff=0)
        output_triangle_p4.next_to(linija2Dh, LEFT, buff=0).shift(0.15*RIGHT)

        ## TRETJA ITERACIJA ##
        # Zgornji tekst
        i3 = TexMobject("i=2:").set_color(BLUE)
        i3.shift(3.6*UP+6.2*LEFT).scale(0.8)
        v31 = TextMobject(
            "8.6\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.55*LEFT)
        v32 = TextMobject(
            "8.6\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.95*RIGHT)
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        analit_graph = self.get_graph(self.analiticna_resitev)
        dashed_analit_graph = DashedVMobject(analit_graph).set_color(WHITE)
        analit_lab = self.get_graph_label(
            analit_graph, label=f"v_a(t)").set_color(WHITE)
        interpolacija_graf = self.get_graph(self.interpolacija)
        #
        x0 = 1.0
        x1 = 1.5
        y0 = 8.58375
        tocka3L = self.get_point_to_graph(x0, interpolacija_graf, color=TEAL)
        linija3Lv = self.get_v_dashed_line_to_graph(
            x0, interpolacija_graf, color=TEAL)
        linija3Lh = self.get_h_dashed_line_to_graph(
            x0, self.interpolacija(x0), interpolacija_graf, color=TEAL)
        tocka3D = self.get_point_to_graph(x1, interpolacija_graf, color=YELLOW)
        linija3Dv = self.get_v_dashed_line_to_graph(
            x1, interpolacija_graf, color=BLUE)
        linija3Dh = self.get_h_dashed_line_to_graph(
            x1, self.interpolacija(x1), interpolacija_graf, color=YELLOW)
        presecisce3 = self.input_to_graph_point(x0, interpolacija_graf)
        ravna_linija3 = Line(
            presecisce3, (presecisce3[0]+1.22, presecisce3[1], 0)).set_color(RED)
        kot3 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle3 = Arc(
            radius=5.5,
            start_angle=0.05,
            angle=kot3-0.08
        )
        angle3.add_tip().scale(0.6).shift(5.65*LEFT+0.25*DOWN).set_color(RED)
        angle_label3 = TexMobject("v_2'").set_color(RED)
        angle_label3.scale(0.8).next_to(angle3, RIGHT).shift(0.2*LEFT)
        linija_odvod3 = Line(tocka3L, tocka3D).set_color(RED)
        #
        input_triangle_p5 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p5 = RegularPolygon(n=3, start_angle=0).set_color(TEAL)
        input_triangle_p6 = input_triangle_p5.copy().set_color(TEAL)
        output_triangle_p6 = RegularPolygon(
            n=3, start_angle=TAU / 2).set_color(YELLOW)
        for triangle in input_triangle_p5, output_triangle_p5, input_triangle_p6, output_triangle_p6:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p6.set_fill(YELLOW, 1)
        x_label_p5 = TexMobject("t_2").scale(0.8).set_color(TEAL)
        output_label_p5 = TexMobject("v_2").scale(0.8).set_color(TEAL)
        x_label_p6 = TexMobject("t_3").scale(0.8).set_color(TEAL)
        output_label_p6 = TexMobject(
            "v_3=11.\\textrm{ m/s}").scale(0.8).set_color(YELLOW)
        output_label_p62 = TexMobject(
            "v_3=11.\\textrm{ m/s}").scale(0.8).set_color(YELLOW)
        x_label_p5.next_to(linija3Lv, RIGHT)
        x_label_p6.next_to(linija3Dv, RIGHT)
        output_label_p5.next_to(linija3Lh, UP)
        output_label_p6.next_to(linija3Dh, UP)
        output_label_p62.next_to(linija3Dh, UP)
        input_triangle_p5.next_to(linija3Lv, DOWN, buff=0)
        input_triangle_p6.next_to(linija3Dv, DOWN, buff=0)
        output_triangle_p5.next_to(linija3Lh, LEFT, buff=0)
        output_triangle_p6.next_to(linija3Dh, LEFT, buff=0).shift(0.15*RIGHT)

        ## ČETRTA ITERACIJA ##
        # Zgornji tekst
        i4 = TexMobject("i=3:").set_color(BLUE)
        i4.shift(3.6*UP+6.2*LEFT).scale(0.8)
        v41 = TextMobject(
            "11.\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.55*LEFT)
        v42 = TextMobject(
            "11.\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.95*RIGHT)
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        analit_graph = self.get_graph(self.analiticna_resitev)
        dashed_analit_graph = DashedVMobject(analit_graph).set_color(WHITE)
        analit_lab = self.get_graph_label(
            analit_graph, label=f"v_a(t)").set_color(WHITE)
        interpolacija_graf = self.get_graph(self.interpolacija)
        #
        x0 = 1.5
        x1 = 2.0
        y0 = 11.3428125
        tocka4L = self.get_point_to_graph(x0, interpolacija_graf, color=TEAL)
        linija4Lv = self.get_v_dashed_line_to_graph(
            x0, interpolacija_graf, color=TEAL)
        linija4Lh = self.get_h_dashed_line_to_graph(
            x0, self.interpolacija(x0), interpolacija_graf, color=TEAL)
        tocka4D = self.get_point_to_graph(x1, interpolacija_graf, color=YELLOW)
        linija4Dv = self.get_v_dashed_line_to_graph(
            x1, interpolacija_graf, color=BLUE)
        linija4Dh = self.get_h_dashed_line_to_graph(
            x1, self.interpolacija(x1), interpolacija_graf, color=YELLOW)
        presecisce4 = self.input_to_graph_point(x0, interpolacija_graf)
        ravna_linija4 = Line(
            presecisce4, (presecisce4[0]+1.22, presecisce4[1], 0)).set_color(RED)
        kot4 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle4 = Arc(
            radius=5.5,
            start_angle=0.05,
            angle=kot4-0.08
        )
        angle4.add_tip().scale(0.6).shift(3.65*LEFT+0.55*UP).set_color(RED)
        angle_label4 = TexMobject("v_3'").set_color(RED)
        angle_label4.scale(0.8).next_to(angle4, RIGHT).shift(0.2*LEFT)
        linija_odvod4 = Line(tocka4L, tocka4D).set_color(RED)
        #
        input_triangle_p7 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p7 = RegularPolygon(n=3, start_angle=0).set_color(TEAL)
        input_triangle_p8 = input_triangle_p7.copy().set_color(TEAL)
        output_triangle_p8 = RegularPolygon(
            n=3, start_angle=TAU / 2).set_color(YELLOW)
        for triangle in input_triangle_p7, output_triangle_p7, input_triangle_p8, output_triangle_p8:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p8.set_fill(YELLOW, 1)
        x_label_p7 = TexMobject("t_3").scale(0.8).set_color(TEAL)
        output_label_p7 = TexMobject("v_3").scale(0.8).set_color(TEAL)
        x_label_p8 = TexMobject("t_4").scale(0.8).set_color(TEAL)
        output_label_p8 = TexMobject(
            "v_4=13.4\\textrm{ m/s}").scale(0.8).set_color(YELLOW)
        x_label_p7.next_to(linija4Lv, RIGHT)
        x_label_p8.next_to(linija4Dv, RIGHT)
        output_label_p7.next_to(linija4Lh, UP)
        output_label_p8.next_to(linija4Dh, UP)
        input_triangle_p7.next_to(linija4Lv, DOWN, buff=0)
        input_triangle_p8.next_to(linija4Dv, DOWN, buff=0)
        output_triangle_p7.next_to(linija4Lh, LEFT, buff=0)
        output_triangle_p8.next_to(linija4Dh, LEFT, buff=0).shift(0.15*RIGHT)

        ## Zaključek iteracij ##
        interp_lab = self.get_graph_label(interpolacija_graf, label=f"v_e(t)")

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py IzrisEksplicitna -pl
        self.play(Write(vrstica1.shift(3.2*UP+0.8*LEFT)))
        self.play(Write(en1.shift(2.2*UP+LEFT)))
        self.wait(2)
        self.play(Transform(en1, en2.shift(2.2*UP)))
        self.wait(2)
        self.play(Write(vrstica2.shift(1.0*UP+2.8*LEFT)))
        self.play(Write(en3.shift(UP+3*RIGHT)))
        self.wait(2)
        self.play(Write(en41))
        self.wait(2)
        self.play(Transform(en41, en42))
        self.wait(2)
        self.play(FadeOut(en1), FadeOut(vrstica1), FadeOut(
            vrstica2), FadeOut(en3))
        # prva iteracija
        self.play(Write(i1), ApplyMethod(en41.scale, 0.8))
        self.play(ApplyMethod(en41.shift, 4.8*UP+4.0*LEFT))
        self.play(Write(izracun11.shift(2.9*UP+2.5*RIGHT)),
                  Write(v11), Write(v12))
        self.wait(3)
        self.setup_axes(animate=True, hideaxes=False)
        self.play(Write(x_os), Write(y_os))
        self.play(ShowCreation(dashed_analit_graph),
                  ShowCreation(analit_lab))
        self.play(
            DrawBorderThenFill(input_triangle_p1),
            DrawBorderThenFill(output_triangle_p1),
            Write(x_label_p1),
            Write(output_label_p1),
            ShowCreation(tocka1L)
        )
        self.play(ShowCreation(h_oklepaj), Write(h_napis))
        self.play(
            Write(ravna_linija1),
            ShowCreation(angle1),
            Write(angle_label1),
        )
        self.play(
            Write(linija_odvod),
            DrawBorderThenFill(input_triangle_p2),
            Write(x_label_p2),
            ShowCreation(linija1Dv)
        )
        self.play(
            DrawBorderThenFill(output_triangle_p2),
            Write(output_label_p2),
            ShowCreation(linija1Dh),
            ShowCreation(tocka1D)
        )
        self.wait(3)
        # druga iteracija
        self.play(Transform(i1, i2))
        self.play(
            FadeOut(input_triangle_p1),
            FadeOut(output_triangle_p1),
            FadeOut(x_label_p1),
            FadeOut(output_label_p1),
            Uncreate(ravna_linija1),
            Uncreate(angle1),
            Uncreate(angle_label1)
        )
        self.play(
            Transform(input_triangle_p2, input_triangle_p3),
            Transform(output_triangle_p2, output_triangle_p3),
            Transform(x_label_p2, x_label_p3),
            Transform(tocka1D, tocka2L),
            Transform(linija1Dv, linija2Lv),
            Transform(linija1Dh, linija2Lh)
        )
        self.wait(1)
        self.play(
            Transform(izracun11, izracun2),
            Transform(output_label_p2, v21),
            Transform(output_label_p22, v22),
            Transform(v11, v21),
            Transform(v12, v22),
            Write(output_label_p3)
        )
        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT),
            ApplyMethod(linija_odvod.set_color, YELLOW),
            ApplyMethod(tocka1L.set_color, YELLOW)
        )
        self.play(
            Write(ravna_linija2),
            ShowCreation(angle2),
            Write(angle_label2),
        )
        self.play(
            Write(linija_odvod2),
            DrawBorderThenFill(input_triangle_p4),
            Write(x_label_p4),
            ShowCreation(linija2Dv)
        )
        self.play(
            DrawBorderThenFill(output_triangle_p4),
            Write(output_label_p4),
            ShowCreation(linija2Dh),
            ShowCreation(tocka2D)
        )
        self.wait(3)

        # tretja iteracija
        self.play(Transform(i1, i3))
        self.play(
            FadeOut(input_triangle_p3),
            FadeOut(output_triangle_p3),
            FadeOut(x_label_p3),
            FadeOut(output_label_p3),
            Uncreate(ravna_linija2),
            Uncreate(angle2),
            Uncreate(angle_label2)
        )
        self.play(
            Transform(input_triangle_p4, input_triangle_p5),
            Transform(output_triangle_p4, output_triangle_p5),
            Transform(x_label_p4, x_label_p5),
            Transform(tocka2D, tocka3L),
            Transform(linija2Dv, linija3Lv),
            Transform(linija2Dh, linija3Lh)
        )
        self.play(
            Transform(output_label_p4, v31),
            Transform(output_label_p42, v32),
            Transform(v11, v31),
            Transform(v12, v32),
            Write(output_label_p5)
        )

        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT),
            ApplyMethod(linija_odvod2.set_color, YELLOW),
            ApplyMethod(tocka2L.set_color, YELLOW),
            FadeOut(linija1Dv), FadeOut(linija1Dh),
            FadeOut(input_triangle_p2), FadeOut(output_triangle_p2),
            FadeOut(x_label_p2), FadeOut(
                output_label_p2), FadeOut(output_label_p22),
        )
        self.play(
            Write(ravna_linija3),
            ShowCreation(angle3),
            Write(angle_label3),
        )
        self.play(
            Write(linija_odvod3),
            DrawBorderThenFill(input_triangle_p6),
            Write(x_label_p6),
            ShowCreation(linija3Dv)
        )
        self.play(
            DrawBorderThenFill(output_triangle_p6),
            Write(output_label_p6),
            ShowCreation(linija3Dh),
            ShowCreation(tocka3D)
        )
        self.wait(3)
        # četrta iteracija
        self.play(Transform(i1, i4))
        self.play(
            FadeOut(input_triangle_p5),
            FadeOut(output_triangle_p5),
            FadeOut(x_label_p5),
            FadeOut(output_label_p5),
            Uncreate(ravna_linija3),
            Uncreate(angle3),
            Uncreate(angle_label3)
        )
        self.play(
            Transform(input_triangle_p6, input_triangle_p7),
            Transform(output_triangle_p6, output_triangle_p7),
            Transform(x_label_p6, x_label_p7),
            Transform(tocka3D, tocka4L),
            Transform(linija3Dv, linija4Lv),
            Transform(linija3Dh, linija4Lh)
        )
        self.play(
            Transform(output_label_p6, v41),
            Transform(output_label_p62, v42),
            Transform(v11, v41),
            Transform(v12, v42),
            Write(output_label_p7.shift(0.1*DOWN))
        )
        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT),
            ApplyMethod(linija_odvod3.set_color, YELLOW),
            ApplyMethod(tocka3L.set_color, YELLOW),
            FadeOut(linija2Dv), FadeOut(linija2Dh),
            FadeOut(input_triangle_p4), FadeOut(output_triangle_p4),
            FadeOut(x_label_p4), FadeOut(
                output_label_p4), FadeOut(output_label_p42),
        )
        self.play(
            Write(ravna_linija4),
            ShowCreation(angle4),
            Write(angle_label4),
        )
        self.play(
            Write(linija_odvod4),
            DrawBorderThenFill(input_triangle_p8),
            Write(x_label_p8),
            ShowCreation(linija4Dv)
        )
        self.play(
            DrawBorderThenFill(output_triangle_p8),
            Write(output_label_p8),
            ShowCreation(linija4Dh),
            ShowCreation(tocka4D)
        )
        self.wait(3)

        # zaključek iteracije
        self.play(
            FadeOut(input_triangle_p7),
            FadeOut(output_triangle_p7),
            FadeOut(x_label_p7),
            FadeOut(output_label_p7),
            FadeOut(input_triangle_p8),
            FadeOut(output_triangle_p8),
            FadeOut(x_label_p8),
            FadeOut(output_label_p8),
            FadeOut(linija4Dh),
            FadeOut(linija4Dv),
            Uncreate(ravna_linija4),
            Uncreate(angle4),
            Uncreate(angle_label4),
            FadeOut(h_oklepaj),
            FadeOut(h_napis),
            ApplyMethod(linija_odvod4.set_color, YELLOW),
            ApplyMethod(tocka4L.set_color, YELLOW),
            FadeOut(linija3Dv), FadeOut(linija3Dh),
            FadeOut(input_triangle_p6), FadeOut(output_triangle_p6),
            FadeOut(x_label_p6), FadeOut(
                output_label_p6), FadeOut(output_label_p62),
            FadeOut(i1),
            FadeOut(v11),
            FadeOut(v12),
            FadeOut(izracun11),
            FadeOut(en41)
        )
        self.play(ShowCreation(interp_lab.shift(0.4*UP)))

        self.wait(5)


class PrehodMedMetodamiImplicitna(Scene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py PrehodMedMetodamiImplicitna -pl
    def construct(self):
        # 1 NASLOV
        naslov1 = TextMobject("Numerično reševanje diferencialnih enačb").set_color(
            YELLOW).scale(1.2).shift(2.8*UP)
        naslov2 = TextMobject("- začetni problem -").set_color(
            YELLOW).scale(1.10).shift(2.1*UP)
        naslov31 = TextMobject("Eulerjeva eksplicitna metoda").set_color(
            RED).scale(0.9).shift(1.8*DOWN+3.5*LEFT)
        naslov32 = TextMobject("Eulerjeva implicitna metoda").set_color(
            RED).scale(0.9).shift(1.8*DOWN+3.5*RIGHT)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(naslov1), Write(naslov2),
                  Write(naslov31), Write(naslov32))
        self.wait(1)
        self.play(FadeOut(naslov1), FadeOut(naslov2),
                  FadeOut(naslov31))
        self.play(ApplyMethod(naslov32.shift, 3.5*LEFT+1*DOWN))
        self.play(ApplyMethod(naslov32.scale, 1.4))
        self.wait(5)


class ImplicitnaMetodaIzpeljava(Scene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py ImplicitnaMetodaIzpeljava -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        # časovnica
        cas = Arrow((-3, 0, 0), (3, 0, 0))
        dot1 = Dot().shift(2.1*LEFT)
        dot2 = Dot().shift(1.8*RIGHT)
        dot = VGroup(dot1, dot2)
        ti1 = TexMobject("t_i").next_to(dot1, UP)
        ti2 = TexMobject("t_{i+1}").next_to(dot2, UP)
        oklepaj = Brace(dot, DOWN)
        h = TexMobject("h").next_to(oklepaj, DOWN)
        casovnica = VGroup(cas, dot, ti1, ti2, oklepaj,
                           h).set_color(BLUE).shift(3*LEFT+2*DOWN)
        casovnica.shift(4*UP+5*RIGHT)

        # diskretna oblika
        vrstica2 = TextMobject(
            "Implicitna Eulerjeva metoda ", "v ", "diskretni obliki", ":")
        vrstica2.set_color_by_tex("Implicitna Eulerjeva metoda ", YELLOW).set_color_by_tex(
            "diskretni obliki", BLUE)
        vrstica2.shift(3*UP+2.7*LEFT).scale(0.8)

        en51 = TexMobject("y_{i+1}", "=", "y_i", "+",
                          "f(", "t_i", ",", "y_i", ")", "h")
        en51.shift(2.00*UP+4.0*LEFT)
        en51.set_color_by_tex_to_color_map({
            "y_{i+1}": YELLOW,
            "y_i": TEAL,
            "f(": RED,
            "t_{i+1}": GREEN,
            ")": RED,
            "h": BLUE
        })

        en52 = TexMobject("y_{i+1}", "=", "y_i", "+",
                          "f(", "t_{i+1}", ",", "y_{i+1}", ")", "h")
        en52.shift(2.00*UP+4.0*LEFT)
        en52.set_color_by_tex_to_color_map({
            "y_{i+1}": YELLOW,
            "y_i": TEAL,
            "f(": RED,
            "t_{i+1}": GREEN,
            ")": RED,
            "h": BLUE
        })

        vrstica3 = TextMobject("Koraki implicitne metode:").scale(
            0.8).shift(0.7*UP+LEFT*4).set_color(YELLOW)
        vrstica41 = TexMobject("\\textrm{1.", "Postavimo }", "\,i=0:",
                               "\,t_0,", "\,y_0", "=", "y(", "t_0", ")").shift(2.95*LEFT)
        vrstica41.set_color_by_tex_to_color_map({
            "\\textrm{1.": RED, "\,i=0:": BLUE, "\,t_0,": TEAL, "\,y_0": TEAL, "y(": YELLOW, ")": YELLOW
        })
        vrstica42 = TexMobject(
            "\\textrm{2.}", "\\textrm{ Reševanje nelinearne enačbe za }", "\,y_{i+1}").shift(2.52*LEFT+0.6*DOWN)
        vrstica42.set_color_by_tex_to_color_map({
            "\\textrm{2.}": RED, "\,y_{i+1}": YELLOW
        })
        vrstica44 = TexMobject(
            "\\textrm{3. }", "\,i=i+1").shift(1.2*DOWN+5.5*LEFT)
        vrstica44.set_color_by_tex_to_color_map(
            {"\\textrm{3.": RED, "\,i=i+1": TEAL})
        vrstica4 = VGroup(vrstica41, vrstica42, vrstica44).scale(0.8)

        l1 = Line((-5.5, 1.0, 0), (2, 1.0, 0))
        l2 = Line((2, 1, 0), (2, 1.5, 0))
        l3 = Arrow((2.25, 1.5, 0), (0, 1.5, 0))
        l = VGroup(l1, l2, l3).set_color(BLUE).shift(2.1*DOWN+2.3*RIGHT)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py ImplicitnaMetodaIzpeljava -pl
        self.play(Write(vrstica2))
        self.play(Write(en51))
        self.wait(1)
        self.play(Transform(en51, en52))
        self.wait(1)
        self.play(ShowCreation(casovnica))
        self.play(Write(vrstica3))
        self.play(Write(vrstica4))
        self.play(ShowCreation(l))
        self.wait(5)

class IzrisImplicitna(GraphScene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py IzrisImplicitna -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 2,
        "x_axis_width": 8,
        "x_tick_frequency": 0.25,
        "x_axis_label": "",
        "y_min": 0,
        "y_max": 15,
        "y_tick_frequency": 1,
        "y_axis_height": 4.5,
        "graph_origin": 5.4*LEFT+2.4*DOWN,
        "y_axis_label": "",
        "x_labeled_nums": list(np.arange(0, 2.1, 0.5)),
        "y_labeled_nums": range(0, 16, 5),
        "exclude_zero_label": True,
        "default_graph_colors": [YELLOW],
        "x_label_decimals": 1,
    }

    def get_point_to_graph(
        self,
        x, graph,
        line_class=SmallDot,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_line_to_graph(
        self,
        x1, x2, graph,
        line_class=Line,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x1, graph),
            self.input_to_graph_point(x2, graph),
            **line_kwargs
        )

    def get_v_dashed_line_to_graph(
        self,
        x, graph,
        line_class=DashedLine,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.coords_to_point(x, 0),
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_h_dashed_line_to_graph(
        self,
        x, y, graph,
        line_class=DashedLine,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.coords_to_point(0, y),
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def analiticna_resitev(self, t):
        m = 1
        c = 0.5
        g = 9.81
        return m*g/c*(1-np.e**(-c/m*t))

    def interpolacija(self, t):
        return -0.0510937*t**4 + 0.562031*t**3 - 3.20613*t**2 + 11.2789*t

    def f_zračni_upor(t, y, g=9.81, m=1., c=0.5):
        return g-c*y/m

    def euler(f, t, y0, *args, **kwargs):
        y = np.zeros_like(t)
        y[0] = y0
        h = t[1]-t[0]
        for i in range(len(t)-1):
            y[i+1] = y[i] + f(t[i], y[i], *args, **kwargs) * h
        return y

    t = np.linspace(0, 2, 5)
    v_rez = euler(f_zračni_upor, t, y0=0)

    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        # pretvorba primera v shemo
        vrstica1 = TextMobject(
            "Diferencialno enačbo padajočega telesa pretvorimo v ustrezno obliko:")
        vrstica1.scale(0.8)
        vrstica2 = TextMobject(
            "in jo uporabimo v Eulerjevi implicitni metodi:")
        vrstica2.scale(0.8)
        en1 = TexMobject("m \, g", "-", "c \,", "v", "=", "m \,", "v'")
        en1.set_color_by_tex_to_color_map({
            "m \, g": RED, "c \,": RED, "v": YELLOW, "m \,": RED, "v'": YELLOW
        })
        en2 = TexMobject("v'", "=", "g", "-", "\\frac{c}{m}", "v")
        en2.set_color_by_tex_to_color_map({
            "g": RED, "frac{c}{m}": RED, "v": YELLOW, "m": RED, "v'": YELLOW
        })
        en31 = TexMobject("v", "=", "v(", "t_i", ")", "=", "y_i")
        en31.set_color_by_tex_to_color_map(
            {"v": YELLOW, "t_i": TEAL, ")": YELLOW, "y_i": TEAL})
        en32 = TexMobject("v'", "=", "y'", "=", "f(", "t_{i+1}}",
                          ",", "y_{i+1}", ")").shift(0.8*DOWN+0.8*RIGHT)
        en32.set_color_by_tex_to_color_map(
            {"v'": YELLOW, "y'": YELLOW, "f(": RED, "t_{i+1}": GREEN, "y_{i+1}": YELLOW, ")": RED})
        en3 = VGroup(en31, en32)

        en41 = TexMobject("y_{i+1}", "=", "y_i", "+",
                          "f(", "t_{i+1}}", ",", "y_{i+1}", ")", "h")
        en41.set_color_by_tex_to_color_map({
            "y_{i+1}": YELLOW,
            "y_i": TEAL,
            "f(": RED,
            "t_{i+1}}": GREEN,
            ")": RED,
            "h": BLUE
        })
        en421 = TexMobject("v_{i+1}")
        en421.set_color_by_tex_to_color_map({"v_{i+1}": YELLOW})
        en422 = TexMobject("=", "v_i")
        en422.set_color_by_tex_to_color_map({"v_i": TEAL})
        en423 = TexMobject(
            "+", "\\big(", "g-\\frac{c}{m}", "v_{i+1}}", "\\big)", "h")
        en423.set_color_by_tex_to_color_map({
            "v_{i+1}": YELLOW,
            "g-\\frac{c}{m}": RED,
            "\\big(": RED,
            "\\big)": RED,
            "h": BLUE})
        en42 = VGroup(en421, en422, en423).shift(
            0.3*LEFT).shift(1.9*DOWN+0.1*LEFT)
        en42.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF/2)
        en424 = TexMobject("0").shift(1.84*DOWN+2.1*LEFT)
        en425 = TexMobject("-").shift(1.9*DOWN+0.65*LEFT)
        en426 = TexMobject("u(", "v_{i+1}", ")", "=").shift(1.84*DOWN+3.4*LEFT)
        en426.set_color_by_tex_to_color_map(
            {"u(": MAROON, "v_{i+1}": YELLOW, ")": MAROON})
        en4 = VGroup(en41, en42).shift(1.9*DOWN+0.1*LEFT)
        en4x = VGroup(en421, en422, en423, en424, en425, en426)
        vrstica3 = TexMobject("\\text{Enačbo preoblikujemo v funkcijo }",
                              "u(", "v_{i+1}", ")", "\\text{ in iščemo njeno ničlo:}")
        vrstica3.set_color_by_tex_to_color_map(
            {"u(": MAROON, "v_{i+1}": YELLOW, ")": MAROON}).scale(0.8).shift(1*LEFT)
        en5 = en42.copy().scale(0.8)

        ## PRVA ITERACIJA ##
        # Zgornji tekst
        i1 = TexMobject(
            "i=0:", "\,v_0=v(t_0=0\\textrm{ s})=0\\textrm{ m/s}", "\\textrm{ (začetni pogoj)}")
        i1.set_color_by_tex_to_color_map(
            {"i=0:": BLUE, "\,v_0=v(t_0=0\\textrm{ s})=0\\textrm{ m/s}": TEAL})
        i1.shift(3.6*UP+2.6*LEFT).scale(0.8)
        izracun11 = TexMobject(
            "= \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, +",
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)",
            "\cdot", "0.5\\textrm{ s}"
        )
        izracun11.scale(0.8).set_color_by_tex_to_color_map({
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)": RED,
            "0.5\\textrm{ s}": BLUE
        })
        v11 = TextMobject(
            "0\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.65*LEFT)
        v12 = TextMobject(
            "\\textrm{ ? }").scale(0.8).set_color(YELLOW).shift(2.9*UP+4.8*RIGHT)
        v122 = TextMobject(
            "3.9\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.9*UP+4.8*RIGHT)
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        # osi
        x_os = TexMobject("t\\textrm{ [s]}").scale(
            0.8).shift(2.4*DOWN+3.3*RIGHT)
        y_os = TexMobject(
            "v(t)\\textrm{ [m/s]}").scale(0.8).rotate(PI/2).shift(6.3*LEFT)
        analit_graph = self.get_graph(self.analiticna_resitev)
        dashed_analit_graph = DashedVMobject(analit_graph).set_color(WHITE)
        analit_lab = self.get_graph_label(
            analit_graph, label=f"v_a(t)").set_color(WHITE)
        interpolacija_graf = self.get_graph(self.interpolacija)
        # Izris
        v1 = 3.924
        v0 = 0
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta1 = self.get_graph(
            lambda t: v0+(g-c*v1/m)*(t-0.5)+v1, x_min=0.78, x_max=0).set_color(RED)
        #
        x0 = 0.01
        x1 = 0.5
        y0 = 0
        #
        tocka1L = self.get_point_to_graph(x0, interpolacija_graf, color=TEAL)
        linija1Lv = self.get_v_dashed_line_to_graph(
            x0, interpolacija_graf, color=TEAL)
        linija1Lh = self.get_h_dashed_line_to_graph(
            x0, self.interpolacija(x0), interpolacija_graf, color=TEAL)
        tocka1D = self.get_point_to_graph(x1, tangenta1, color=YELLOW)
        linija1Dv = self.get_v_dashed_line_to_graph(x1, tangenta1, color=BLUE)
        linija1Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta1, color=YELLOW)
        #
        input_triangle_p1 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p1 = RegularPolygon(n=3, start_angle=0).set_color(TEAL)
        input_triangle_p2 = input_triangle_p1.copy().set_color(TEAL)
        output_triangle_p2 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p1, output_triangle_p1, input_triangle_p2, output_triangle_p2:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p2.set_fill(YELLOW, 1)
        x_label_p1 = TexMobject("t_0").scale(0.8).set_color(TEAL)
        output_label_p1 = TexMobject("v_0").scale(0.8).set_color(TEAL)
        x_label_p2 = TexMobject("t_1").scale(0.8).set_color(TEAL)
        output_label_p2 = TexMobject(
            "v_1=3.9 \\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p1.next_to(linija1Lv, DOWN)
        x_label_p2.next_to(linija1Dv, RIGHT)
        output_label_p1.next_to(linija1Lh, LEFT)
        output_label_p2.next_to(linija1Dh, UP)
        input_triangle_p1.next_to(linija1Lv, DOWN, buff=0)
        input_triangle_p2.next_to(linija1Dv, DOWN, buff=0)
        output_triangle_p1.next_to(linija1Lh, LEFT, buff=0)
        output_triangle_p2.next_to(linija1Dh, LEFT, buff=0)
        #
        h_oklepaj = Brace(VGroup(input_triangle_p1, input_triangle_p2), DOWN).shift(
            0.3*DOWN).set_color(BLUE)
        h_napis = h_oklepaj.get_text("$h$").scale(
            0.8).shift(0.2*UP).set_color(BLUE)
        #
        koncna_crta1 = self.get_graph(
            lambda t: v0+(g-c*v1/m)*(t-0.5)+v1, x_min=0, x_max=0.5).set_color(YELLOW)

        ## DRUGA ITERACIJA ##
        # Zgornji tekst
        i2 = TexMobject("i=1:")
        i2.set_color_by_tex_to_color_map(
            {"i=1:": BLUE})
        i2.shift(3.63*UP+6.25*LEFT).scale(0.8)
        izracun21 = TexMobject(
            "= \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, +",
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)",
            "\cdot", "0.5\\textrm{ s}"
        )
        izracun21.scale(0.8).set_color_by_tex_to_color_map({
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)": RED,
            "0.5\\textrm{ s}": BLUE
        }).shift(2.9*UP+2.5*RIGHT)
        v211 = TextMobject(
            "3.9\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.76*LEFT)
        v221 = TextMobject(
            "7.1\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.9*UP+4.83*RIGHT)
        # izris
        v1 = 7.063
        v0 = 3.924
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta2 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.0), x_min=0.78+0.5, x_max=0.5).set_color(RED)
        #
        x0 = 0.5
        x1 = 1.0
        y0 = 3.924
        tocka2L = tocka1D.copy().set_color(TEAL)
        linija2Lv = linija1Dv.copy().set_color(TEAL)
        linija2Lh = linija1Dh.copy().set_color(TEAL)
        tocka2D = self.get_point_to_graph(x1, tangenta2, color=YELLOW)
        linija2Dv = self.get_v_dashed_line_to_graph(x1, tangenta2, color=BLUE)
        linija2Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta2, color=YELLOW)
        #
        input_triangle_p12 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p12 = RegularPolygon(
            n=3, start_angle=0).set_color(TEAL)
        input_triangle_p22 = input_triangle_p12.copy().set_color(TEAL)
        output_triangle_p22 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p12, output_triangle_p12, input_triangle_p22, output_triangle_p22:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p22.set_fill(YELLOW, 1)
        x_label_p12 = TexMobject("t_1").scale(0.8).set_color(TEAL)
        output_label_p12 = TexMobject("v_1").scale(0.8).set_color(TEAL)
        x_label_p22 = TexMobject("t_2").scale(0.8).set_color(TEAL)
        output_label_p22 = TexMobject(
            "v_2=7.1\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p12.next_to(linija2Lv, RIGHT)
        x_label_p22.next_to(linija2Dv, RIGHT)
        output_label_p12.next_to(linija2Lh, UP)
        output_label_p22.next_to(linija2Dh, UP)
        input_triangle_p12.next_to(linija2Lv, DOWN, buff=0)
        input_triangle_p22.next_to(linija2Dv, DOWN, buff=0)
        output_triangle_p12.next_to(linija2Lh, LEFT, buff=0)
        output_triangle_p22.next_to(linija2Dh, LEFT, buff=0)
        #
        koncna_crta2 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.0), x_min=0.5, x_max=1.0).set_color(YELLOW)

        ## TRETJA ITERACIJA ##
        # Zgornji tekst
        i3 = TexMobject("i=2:")
        i3.set_color_by_tex_to_color_map(
            {"i=2:": BLUE})
        i3.shift(3.63*UP+6.25*LEFT).scale(0.8)
        v311 = TextMobject(
            "7.1\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.76*LEFT)
        v321 = TextMobject(
            "9.6\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.9*UP+4.83*RIGHT)
        # izris
        v1 = 9.575
        v0 = 7.063
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta3 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.5), x_min=1.0, x_max=1.5).set_color(RED)
        #
        x0 = 1.0
        x1 = 1.5
        y0 = 7.063
        tocka3L = tocka1D.copy().set_color(TEAL)
        linija3Lv = linija2Dv.copy().set_color(TEAL)
        linija3Lh = linija2Dh.copy().set_color(TEAL)
        tocka3D = self.get_point_to_graph(x1, tangenta3, color=YELLOW)
        linija3Dv = self.get_v_dashed_line_to_graph(x1, tangenta3, color=BLUE)
        linija3Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta3, color=YELLOW)
        #
        input_triangle_p13 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p13 = RegularPolygon(
            n=3, start_angle=0).set_color(TEAL)
        input_triangle_p23 = input_triangle_p13.copy().set_color(TEAL)
        output_triangle_p23 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p13, output_triangle_p13, input_triangle_p23, output_triangle_p23:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p23.set_fill(YELLOW, 1)
        x_label_p13 = TexMobject("t_2").scale(0.8).set_color(TEAL)
        output_label_p13 = TexMobject("v_2").scale(0.8).set_color(TEAL)
        x_label_p23 = TexMobject("t_3").scale(0.8).set_color(TEAL)
        output_label_p23 = TexMobject(
            "v_3=9.6\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p13.next_to(linija3Lv, RIGHT)
        x_label_p23.next_to(linija3Dv, RIGHT)
        output_label_p13.next_to(linija3Lh, UP)
        output_label_p23.next_to(linija3Dh, UP)
        input_triangle_p13.next_to(linija3Lv, DOWN, buff=0)
        input_triangle_p23.next_to(linija3Dv, DOWN, buff=0)
        output_triangle_p13.next_to(linija3Lh, LEFT, buff=0)
        output_triangle_p23.next_to(linija3Dh, LEFT, buff=0)
        #
        koncna_crta3 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.5), x_min=1.0, x_max=1.5).set_color(YELLOW)

        ## ČETRTA ITERACIJA ##
        # Zgornji tekst
        i4 = TexMobject("i=3:")
        i4.set_color_by_tex_to_color_map(
            {"i=3:": BLUE})
        i4.shift(3.63*UP+6.25*LEFT).scale(0.8)
        v411 = TextMobject(
            "9.6\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.76*LEFT)
        v421 = TextMobject(
            "11.6\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.9*UP+4.83*RIGHT)
        # izris
        v1 = 11.584
        v0 = 9.575
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta4 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-2.0), x_min=1.5, x_max=2.0).set_color(RED)
        #
        x0 = 1.5
        x1 = 2.0
        y0 = 9.575
        tocka4L = tocka1D.copy().set_color(TEAL)
        linija4Lv = linija3Dv.copy().set_color(TEAL)
        linija4Lh = linija3Dh.copy().set_color(TEAL)
        tocka4D = self.get_point_to_graph(x1, tangenta4, color=YELLOW)
        linija4Dv = self.get_v_dashed_line_to_graph(x1, tangenta4, color=BLUE)
        linija4Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta4, color=YELLOW)
        #
        input_triangle_p14 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p14 = RegularPolygon(
            n=3, start_angle=0).set_color(TEAL)
        input_triangle_p24 = input_triangle_p14.copy().set_color(TEAL)
        output_triangle_p24 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p14, output_triangle_p14, input_triangle_p24, output_triangle_p24:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p24.set_fill(YELLOW, 1)
        x_label_p14 = TexMobject("t_3").scale(0.8).set_color(TEAL)
        output_label_p14 = TexMobject("v_3").scale(0.8).set_color(TEAL)
        x_label_p24 = TexMobject("t_4").scale(0.8).set_color(TEAL)
        output_label_p24 = TexMobject(
            "v_4=11.6\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p14.next_to(linija4Lv, RIGHT)
        x_label_p24.next_to(linija4Dv, RIGHT)
        output_label_p14.next_to(linija4Lh, UP)
        output_label_p24.next_to(linija4Dh, UP)
        input_triangle_p14.next_to(linija4Lv, DOWN, buff=0)
        input_triangle_p24.next_to(linija4Dv, DOWN, buff=0)
        output_triangle_p14.next_to(linija4Lh, LEFT, buff=0)
        output_triangle_p24.next_to(linija4Dh, LEFT, buff=0)
        #
        koncna_crta4 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-2.0), x_min=1.5, x_max=2.0).set_color(YELLOW)
        #
        v_implicitna = TexMobject("v_i(t)").set_color(
            YELLOW).shift(0.7*UP+3.2*RIGHT)

        ###########################
        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py IzrisImplicitna -pl
        # uvod
        self.play(Write(vrstica1.shift(3.2*UP+0.8*LEFT)))
        self.play(Write(en1.shift(2.2*UP+LEFT)))
        self.wait(2)
        self.play(Transform(en1, en2.shift(2.2*UP)))
        self.wait(2)
        self.play(Write(vrstica2.shift(1.0*UP+2.8*LEFT)))
        self.play(Write(en3.shift(UP+3*RIGHT)))
        self.wait(2)
        self.play(Write(en41))
        self.wait(2)
        self.play(ReplacementTransform(en41, en42))
        self.wait(2)
        self.play(FadeOut(en1), FadeOut(vrstica1),
                  FadeOut(vrstica2), FadeOut(en3))
        self.play(Write(vrstica3))
        self.wait(1)
        self.play(
            ApplyMethod(en421.shift, 2.52*RIGHT),
            ApplyMethod(en423.shift, 1.3*RIGHT),
            Write(en424),
            Write(en425))
        self.play(Write(en426))
        self.wait(3)
        self.play(FadeOut(vrstica3), FadeOut(en4x))
        #
        self.play(Write(i1), Write(en5.shift(4.8*UP+3.8*LEFT)))
        self.wait(2)
        self.play(Write(izracun11.shift(2.9*UP+2.6*RIGHT)),
                  Write(v11), Write(v12))
        self.wait(3)
        # izris
        self.setup_axes(animate=True, hideaxes=False)
        self.play(Write(x_os), Write(y_os))
        self.play(ShowCreation(dashed_analit_graph),
                  ShowCreation(analit_lab))
        # PRVA ITERACIJA
        self.play(
            DrawBorderThenFill(input_triangle_p1),
            DrawBorderThenFill(output_triangle_p1),
            Write(x_label_p1),
            Write(output_label_p1),
            ShowCreation(tocka1L)
        )
        self.play(ShowCreation(h_oklepaj), Write(h_napis))
        self.wait(2)
        self.play(
            DrawBorderThenFill(input_triangle_p2),
            Write(x_label_p2),
            ShowCreation(linija1Dv),
            DrawBorderThenFill(output_triangle_p2),
            Write(output_label_p2),
            ShowCreation(linija1Dh),
            ShowCreation(tocka1D),
            Transform(v12, v122)
        )
        self.wait(3)
        self.play(ShowCreation(koncna_crta1))

        # DRUGA ITERACIJA
        # zgornji tekst
        self.play(
            Transform(i1, i2),
            Transform(izracun11, izracun21),
            Transform(v11, v211),
            ApplyMethod(en5.shift, 0.3*LEFT)
        )
        self.wait(1)
        # izris
        self.play(
            FadeOut(input_triangle_p1),
            FadeOut(x_label_p1),
            FadeOut(output_triangle_p1),
            FadeOut(output_label_p1),
            Transform(input_triangle_p2, input_triangle_p12),
            Transform(x_label_p2, x_label_p12),
            Transform(linija1Dh, linija2Lh),
            Transform(linija1Dv, linija2Lv),
            Transform(output_triangle_p2, output_triangle_p12),
            Transform(output_label_p2, output_label_p12)
        )
        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT)
        )
        self.wait(2)
        self.play(
            Write(x_label_p22),
            ShowCreation(linija2Dv),
            DrawBorderThenFill(input_triangle_p22),
            DrawBorderThenFill(output_triangle_p22),
            Write(output_label_p22),
            ShowCreation(linija2Dh),
            ShowCreation(tocka2D),
            Transform(v12, v221)
        )
        self.play(ShowCreation(koncna_crta2))

        # TRETJA ITERACIJA
        # zgorjni tekst
        self.play(
            Transform(i1, i3),
            Transform(v11, v311),
        )
        self.wait(1)
        # izris
        self.play(
            FadeOut(input_triangle_p12),
            FadeOut(x_label_p12),
            FadeOut(output_triangle_p12),
            FadeOut(output_label_p12),
            Transform(input_triangle_p22, input_triangle_p13),
            Transform(x_label_p22, x_label_p13),
            Transform(linija2Dh, linija3Lh),
            Transform(linija2Dv, linija3Lv),
            Transform(output_triangle_p22, output_triangle_p13),
            Transform(output_label_p22, output_label_p13)
        )
        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT),
            FadeOut(linija1Dh),
            FadeOut(linija1Dv),
            FadeOut(input_triangle_p2),
            FadeOut(x_label_p2),
            FadeOut(output_triangle_p2),
            FadeOut(output_label_p2)
        )
        self.wait(2)
        self.play(
            Write(x_label_p23),
            ShowCreation(linija3Dv),
            DrawBorderThenFill(input_triangle_p23),
            DrawBorderThenFill(output_triangle_p23),
            Write(output_label_p23),
            ShowCreation(linija3Dh),
            ShowCreation(tocka3D),
            Transform(v12, v321)
        )
        self.play(ShowCreation(koncna_crta3))

        # ČETRTA ITERACIJA
        # zgorjni tekst
        self.play(
            Transform(i1, i4),
            Transform(v11, v411)
        )
        self.wait(1)
        # izris
        self.play(
            Transform(input_triangle_p23, input_triangle_p14),
            Transform(x_label_p23, x_label_p14),
            Transform(linija3Dh, linija4Lh),
            Transform(linija3Dv, linija4Lv),
            Transform(output_triangle_p23, output_triangle_p14),
            Transform(output_label_p23, output_label_p14)
        )
        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT),
            FadeOut(linija2Dh),
            FadeOut(linija2Dv),
            FadeOut(input_triangle_p22),
            FadeOut(x_label_p22),
            FadeOut(output_triangle_p22),
            FadeOut(output_label_p22)
        )
        self.wait(1)
        self.play(
            Write(x_label_p24),
            ShowCreation(linija4Dv),
            DrawBorderThenFill(input_triangle_p24),
            DrawBorderThenFill(output_triangle_p24),
            Write(output_label_p24),
            ShowCreation(linija4Dh),
            ShowCreation(tocka4D),
            Transform(v12, v421)
        )
        self.play(ShowCreation(koncna_crta4))

        # zaključek
        self.wait(1)
        self.play(
            FadeOut(input_triangle_p23),
            FadeOut(input_triangle_p24),
            FadeOut(output_triangle_p23),
            FadeOut(output_triangle_p24),
            FadeOut(x_label_p23),
            FadeOut(x_label_p24),
            FadeOut(linija4Dh),
            FadeOut(linija4Dv),
            FadeOut(linija3Dh),
            FadeOut(linija3Dv),
            FadeOut(h_oklepaj),
            FadeOut(h_napis),
            FadeOut(i1),
            FadeOut(en5),
            FadeOut(v421),
            FadeOut(v11),
            FadeOut(v12),
            FadeOut(izracun11),
            FadeOut(output_label_p14),
            FadeOut(output_label_p24),
            FadeOut(output_label_p23)
        )
        self.play(Write(v_implicitna))
        self.wait(5)


class SekantnaMetoda(GraphScene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py SekantnaMetoda -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 12,
        "x_axis_width": 11,
        "x_tick_frequency": 1,
        "x_axis_label": "",
        "y_min": 0,
        "y_max": 7,
        "y_tick_frequency": 1,
        "y_axis_height": 5.5,
        "graph_origin": 5.8*LEFT+2.7*DOWN,
        "axes_color": WHITE,
        "y_axis_label": "",
        "x_labeled_nums": list(np.arange(0, 12.1, 1)),
        "y_labeled_nums": range(0, 8, 1),
        "exclude_zero_label": False,
        "default_graph_colors": [ORANGE, PINK, GREEN],
        "x_label_decimals": 0,
    }

    def get_point_to_graph(
        self,
        x, graph,
        line_class=Dot,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_dashed_line_to_graph(
        self,
        x, graph,
        line_class=DashedLine,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.coords_to_point(x, 0),
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_area(self, graph, t_min, t_max):
        numerator = max(t_max - t_min, 0.0001)
        dx = float(numerator) / self.num_rects
        return self.get_riemann_rectangles(
            graph,
            x_min=t_min,
            x_max=t_max,
            dx=dx/8,
            stroke_width=0,
        ).set_fill(opacity=self.area_opacity)

    def get_line_to_graph(
        self,
        x1, x2, graph,
        line_class=Line,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x1, graph),
            self.input_to_graph_point(x2, graph),
            **line_kwargs
        )

    def polinom_primer1(self, x):
        v0 = 0
        g = 9.81
        c = 0.5
        m = 1
        h = 0.5
        return v0-x+(g-c/m*x)*h

    def polinom_primer2(self, x):
        v0 = 3.924
        g = 9.81
        c = 0.5
        m = 1
        h = 0.5
        return v0-x+(g-c/m*x)*h

    def polinom_primer3(self, x):
        v0 = 7.063
        g = 9.81
        c = 0.5
        m = 1
        h = 0.5
        return v0-x+(g-c/m*x)*h

    def polinom_primer4(self, x):
        v0 = 9.575
        g = 9.81
        c = 0.5
        m = 1
        h = 0.5
        return v0-x+(g-c/m*x)*h

    # KONSTRUKCIJA VSEH OBJEKTOV ##

    def construct(self):
        ## GRAF ##
        self.setup_axes(animate=False, hideaxes=True)
        x_os = TexMobject("v_{i+1}").set_color(YELLOW)
        x_os = TexMobject(
            "v_{i+1}").set_color(YELLOW).shift(2.7*DOWN+6.0*RIGHT)
        y_os = TexMobject("u(", "v_{i+1}", ")").shift(3.4*UP+5.8*LEFT)
        y_os.set_color_by_tex_to_color_map(
            {"u(": MAROON, "v_{i+1}": YELLOW, ")": MAROON})
        # funkcija
        fun_u1 = TexMobject("u(", "v_{i+1}", ")")
        fun_u1.set_color_by_tex_to_color_map({
            "u(": MAROON,
            "v_{i+1}": YELLOW,
            ")": MAROON}).shift(4*LEFT)
        fun_u2 = TexMobject(
            "=", "v_i", "-", "v_{i+1}", "+",
            "\\big(", "g-\\frac{c}{m}", "v_{i+1}}", "\\big)", "h")
        fun_u2.set_color_by_tex_to_color_map({
            "v_{i+1}": YELLOW,
            "v_i": TEAL,
            "g-\\frac{c}{m}": RED,
            "\\big(": RED,
            "\\big)": RED,
            "h": BLUE})
        fun_u = VGroup(fun_u1, fun_u2).scale(0.8).shift(3.3*UP+0.5*RIGHT)
        # 1. ITERACIJA
        x_min0 = 0.0
        x_max0 = 1.0
        x_mid0 = x_min0 - self.polinom_primer1(x_min0)*(x_max0-x_min0)/(
            self.polinom_primer1(x_max0)-self.polinom_primer1(x_min0))
        polinom_graph1 = self.get_graph(
            self.polinom_primer1, x_min=-1, x_max=4.5)
        dashed_polinom_graph1 = DashedVMobject(
            polinom_graph1).set_color(MAROON)
        # linije in točke
        tocka1L = self.get_point_to_graph(x_min0, polinom_graph1, color=YELLOW)
        tocka1L_pot = self.get_graph(
            self.polinom_primer1, x_min=x_min0, x_max=x_max0)
        tocka1D = self.get_point_to_graph(x_max0, polinom_graph1, color=YELLOW)
        tocka1D_pot = self.get_graph(
            self.polinom_primer1, x_min=x_max0, x_max=x_mid0)
        tocka1S = self.get_point_to_graph(x_mid0, polinom_graph1, color=YELLOW)
        linija1L = self.get_vertical_line_to_graph(
            x_min0, polinom_graph1, color=YELLOW)
        linija1D = self.get_vertical_line_to_graph(
            x_max0, polinom_graph1, color=YELLOW)
        linija1S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph1, color=YELLOW)
        linear1 = self.get_graph(self.polinom_primer1,
                                 x_min=-0.5, x_max=4.2).set_color(PINK)
        # tekst
        levo1 = TexMobject("v_{1_0}").set_color(YELLOW)
        levo_f1 = TexMobject("u(", "v_{1_0}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{1_0}": YELLOW, ")": MAROON
        })
        label_coord11 = self.input_to_graph_point(x_min0, polinom_graph1)
        levo1.next_to(label_coord11, 18*DOWN+0.2*LEFT).scale(0.8)
        levo_f1.next_to(label_coord11, 0.2*UP+0.2*RIGHT).scale(0.8)
        desno1 = TexMobject("v_{1_1}}").set_color(YELLOW)
        desno_f1 = TexMobject("u(", "v_{1_1}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{1_1}": YELLOW, ")": MAROON
        })
        label_coord12 = self.input_to_graph_point(x_max0, polinom_graph1)
        desno1.next_to(label_coord12, 14*DOWN+0.2*RIGHT).scale(0.8)
        desno_f1.next_to(label_coord12, 0.2*UP+0.2*RIGHT).scale(0.8)
        srednje1 = TexMobject("v_{1_2}").set_color(YELLOW)
        srednje_f1 = TexMobject("u(", "v_{1_2}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{1_2}": YELLOW, ")": MAROON
        })
        label_coord13 = self.input_to_graph_point(x_mid0, polinom_graph1)
        srednje1.next_to(label_coord13, 2.5*DOWN).scale(0.8)
        srednje_f1.next_to(label_coord13, 1.2*UP+0.1*RIGHT).scale(0.8)
        # rezultat
        rez11 = TexMobject(
            "v_{i+1_2}", "=", "v_{i+1_1}", " - "
            "u(", "v_{i+1_1}", ")",
            "{v_{i+1_1}", "-", "v_{i+1_0}", "\\over", "u(", "v_{i+1_1}", ") -", "u(", "v_{i+1_0}", ")}", "="
        )
        rez11.set_color_by_tex_to_color_map({
            "=": WHITE,  "+": WHITE, "v_{i+1_1}": YELLOW, "u(": MAROON, ")": MAROON
        })
        rez11.set_color_by_tex_to_color_map({
            "v_{i+1_2}": YELLOW, "v_{i+1_0}": YELLOW
        })
        rez12 = TexMobject(
            "=", "1\\textrm{ m/s}", " - "
            "3.7\\textrm{ m/s}", "\\cdot",
            "{1\\textrm{ m/s}", "-", "0\\textrm{ m/s}", "\\over", "3.7\\textrm{ m/s}", "-", "4.9\\textrm{ m/s}}", "="
        ).shift(1.5*DOWN+0.7*RIGHT)
        rez12.set_color_by_tex_to_color_map({
            "0": YELLOW, "1": YELLOW, "3.7": MAROON, "4.9": MAROON
        })
        convert_string_x = np.array2string(np.around(x_mid0, 2))
        string_print_x = f"{convert_string_x}"
        rez13 = TextMobject(
            string_print_x, " m/s").set_color(YELLOW).shift(6.4*RIGHT+1.5*DOWN)
        rez1 = VGroup(rez11, rez12, rez13).scale(0.8).shift(2.1*UP+0.5*RIGHT)

        # 2. ITERACIJA
        x_min0 = 3.924
        x_max0 = 4.924
        x_mid0 = x_min0 - self.polinom_primer2(x_min0)*(x_max0-x_min0)/(
            self.polinom_primer2(x_max0)-self.polinom_primer2(x_min0))
        polinom_graph2 = self.get_graph(self.polinom_primer2, x_min=1, x_max=8)
        dashed_polinom_graph2 = DashedVMobject(
            polinom_graph2).set_color(MAROON)
        # linije in točke
        tocka2L = self.get_point_to_graph(x_min0, polinom_graph2, color=YELLOW)
        tocka2L_pot = self.get_graph(
            self.polinom_primer2, x_min=x_min0, x_max=x_max0)
        tocka2D = self.get_point_to_graph(x_max0, polinom_graph2, color=YELLOW)
        tocka2D_pot = self.get_graph(
            self.polinom_primer2, x_min=x_max0, x_max=x_mid0)
        tocka2S = self.get_point_to_graph(x_mid0, polinom_graph2, color=YELLOW)
        linija2L = self.get_vertical_line_to_graph(
            x_min0, polinom_graph2, color=YELLOW)
        linija2D = self.get_vertical_line_to_graph(
            x_max0, polinom_graph2, color=YELLOW)
        linija2S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph2, color=YELLOW)
        linear2 = self.get_graph(self.polinom_primer2,
                                 x_min=2.5, x_max=7.5).set_color(PINK)
        # tekst
        levo2 = TexMobject("v_{2_0}").set_color(YELLOW)
        levo_f2 = TexMobject("u(", "v_{2_0}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{2_0}": YELLOW, ")": MAROON
        })
        label_coord21 = self.input_to_graph_point(x_min0, polinom_graph2)
        levo2.next_to(label_coord21, 14.6*DOWN+0.2*LEFT).scale(0.8)
        levo_f2.next_to(label_coord21, 0.1*UP+0.5*RIGHT).scale(0.8)
        desno2 = TexMobject("v_{2_1}}").set_color(YELLOW)
        desno_f2 = TexMobject("u(", "v_{2_1}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{2_1}": YELLOW, ")": MAROON
        })
        label_coord22 = self.input_to_graph_point(x_max0, polinom_graph2)
        desno2.next_to(label_coord22, 11.0*DOWN+0.2*RIGHT).scale(0.8)
        desno_f2.next_to(label_coord22, 0.2*UP+0.4*RIGHT).scale(0.8)
        srednje2 = TexMobject("v_{2_2}").set_color(YELLOW)
        srednje_f2 = TexMobject("u(", "v_{2_2}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{2_2}": YELLOW, ")": MAROON
        })
        label_coord23 = self.input_to_graph_point(x_mid0, polinom_graph2)
        srednje2.next_to(label_coord23, 2.5*DOWN).scale(0.8)
        srednje_f2.next_to(label_coord23, 1.2*UP+0.5*RIGHT).scale(0.8)
        # rezultat
        rez21 = TexMobject(
            "v_{i+1_2}", "=", "v_{i+1_1}", " - "
            "u(", "v_{i+1_1}", ")",
            "{v_{i+1_1}", "-", "v_{i+1_0}", "\\over", "u(", "v_{i+1_1}", ") -", "u(", "v_{i+1_0}", ")}", "="
        )
        rez21.set_color_by_tex_to_color_map({
            "=": WHITE,  "+": WHITE, "v_{i+1_1}": YELLOW, "u(": MAROON, ")": MAROON
        })
        rez21.set_color_by_tex_to_color_map({
            "v_{i+1_2}": YELLOW, "v_{i+1_0}": YELLOW
        })
        rez22 = TexMobject(
            "=", "4.9\\textrm{ m/s}", " - "
            "2.7\\textrm{ m/s}", "\\cdot",
            "{4.9\\textrm{ m/s}", "-", "3.9\\textrm{ m/s}", "\\over", "2.7\\textrm{ m/s}", "-", "3.92\\textrm{ m/s}}", "="
        ).shift(1.5*DOWN+1.1*RIGHT)
        rez22.set_color_by_tex_to_color_map({
            "3.9": YELLOW, "4.9": YELLOW, "2.7": MAROON, "3.92": MAROON
        })
        convert_string_x = np.array2string(np.around(x_mid0, 2))
        string_print_x = f"{convert_string_x}"
        rez23 = TextMobject("= ", string_print_x,
                            " m/s").set_color(YELLOW).shift(4.3*RIGHT+2.9*DOWN)
        rez2 = VGroup(rez21, rez22, rez23).scale(0.8).shift(2.4*UP+2.0*RIGHT)

        # 3. ITERACIJA
        x_min0 = 7.0632
        x_max0 = 8.0632
        x_mid0 = x_min0 - self.polinom_primer3(x_min0)*(x_max0-x_min0)/(
            self.polinom_primer3(x_max0)-self.polinom_primer3(x_min0))
        polinom_graph3 = self.get_graph(
            self.polinom_primer3, x_min=3, x_max=11)
        dashed_polinom_graph3 = DashedVMobject(
            polinom_graph3).set_color(MAROON)
        # linije in točke
        tocka3L = self.get_point_to_graph(x_min0, polinom_graph3, color=YELLOW)
        tocka3L_pot = self.get_graph(
            self.polinom_primer3, x_min=x_min0, x_max=x_max0)
        tocka3D = self.get_point_to_graph(x_max0, polinom_graph3, color=YELLOW)
        tocka3D_pot = self.get_graph(
            self.polinom_primer3, x_min=x_max0, x_max=x_mid0)
        tocka3S = self.get_point_to_graph(x_mid0, polinom_graph3, color=YELLOW)
        linija3L = self.get_vertical_line_to_graph(
            x_min0, polinom_graph3, color=YELLOW)
        linija3D = self.get_vertical_line_to_graph(
            x_max0, polinom_graph3, color=YELLOW)
        linija3S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph3, color=YELLOW)
        linear3 = self.get_graph(self.polinom_primer3,
                                 x_min=5.5, x_max=10.5).set_color(PINK)
        # tekst
        levo3 = TexMobject("v_{3_0}").set_color(YELLOW)
        levo_f3 = TexMobject("u(", "v_{3_0}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{3_0}": YELLOW, ")": MAROON
        })
        label_coord31 = self.input_to_graph_point(x_min0, polinom_graph3)
        levo3.next_to(label_coord31, 12.3*DOWN+0.2*LEFT).scale(0.8)
        levo_f3.next_to(label_coord31, 0.1*UP+0.5*RIGHT).scale(0.8)
        desno3 = TexMobject("v_{3_1}}").set_color(YELLOW)
        desno_f3 = TexMobject("u(", "v_{3_1}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{3_1}": YELLOW, ")": MAROON
        })
        label_coord32 = self.input_to_graph_point(x_max0, polinom_graph3)
        desno3.next_to(label_coord32, 8.7*DOWN+0.2*RIGHT).scale(0.8)
        desno_f3.next_to(label_coord32, 0.2*UP+0.4*RIGHT).scale(0.8)
        srednje3 = TexMobject("v_{3_2}").set_color(YELLOW)
        srednje_f3 = TexMobject("u(", "v_{3_2}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{3_2}": YELLOW, ")": MAROON
        })
        label_coord33 = self.input_to_graph_point(x_mid0, polinom_graph3)
        srednje3.next_to(label_coord33, 2.5*DOWN).scale(0.8)
        srednje_f3.next_to(label_coord33, 1.2*UP+0.5*RIGHT).scale(0.8)
        # rezultat
        rez31 = TexMobject(
            "v_{i+1_2}", "=", "v_{i+1_1}", " - "
            "u(", "v_{i+1_1}", ")",
            "{v_{i+1_1}", "-", "v_{i+1_0}", "\\over", "u(", "v_{i+1_1}", ") -", "u(", "v_{i+1_0}", ")}", "="
        )
        rez31.set_color_by_tex_to_color_map({
            "=": WHITE,  "+": WHITE, "v_{i+1_1}": YELLOW, "u(": MAROON, ")": MAROON
        })
        rez31.set_color_by_tex_to_color_map({
            "v_{i+1_2}": YELLOW, "v_{i+1_0}": YELLOW
        })
        rez32 = TexMobject(
            "=", "8.1\\textrm{ m/s}", " - "
            "1.9\\textrm{ m/s}", "\\cdot",
            "{8.1\\textrm{ m/s}", "-", "7.1\\textrm{ m/s}", "\\over", "1.9\\textrm{ m/s}", "-", "3.1\\textrm{ m/s}}", "="
        ).shift(1.5*DOWN+1.0*RIGHT)
        rez32.set_color_by_tex_to_color_map({
            "7.1": YELLOW, "8.1": YELLOW, "3.1": MAROON, "1.9": MAROON
        })
        convert_string_x = np.array2string(np.around(x_mid0, 2))
        string_print_x = f"{convert_string_x}"
        rez33 = TextMobject("= ", string_print_x,
                            " m/s").set_color(YELLOW).shift(4.3*RIGHT+2.9*DOWN)
        rez3 = VGroup(rez31, rez32, rez33).scale(0.8).shift(3.4*UP+2.0*RIGHT)

        # 4. ITERACIJA
        x_min0 = 9.575
        x_max0 = 10.575
        x_mid0 = x_min0 - self.polinom_primer4(x_min0)*(x_max0-x_min0)/(self.polinom_primer4(x_max0)-self.polinom_primer4(x_min0))
        polinom_graph4 = self.get_graph(self.polinom_primer4, x_min=5, x_max=12.5)
        dashed_polinom_graph4 = DashedVMobject(polinom_graph4).set_color(MAROON)
        # linije in točke
        tocka4L = self.get_point_to_graph(x_min0, polinom_graph4, color=YELLOW)
        tocka4L_pot = self.get_graph(self.polinom_primer4, x_min=x_min0, x_max=x_max0)
        tocka4D = self.get_point_to_graph(x_max0, polinom_graph4, color=YELLOW)
        tocka4D_pot = self.get_graph(self.polinom_primer4, x_min=x_max0, x_max=x_mid0)
        tocka4S = self.get_point_to_graph(x_mid0, polinom_graph4, color=YELLOW)
        linija4L = self.get_vertical_line_to_graph(x_min0, polinom_graph4, color=YELLOW)
        linija4D = self.get_vertical_line_to_graph(x_max0, polinom_graph4, color=YELLOW)
        linija4S = self.get_dashed_line_to_graph(x_mid0, polinom_graph4, color=YELLOW)
        linear4 = self.get_graph(self.polinom_primer4, x_min=6.5, x_max=12).set_color(PINK)
        # tekst
        levo4 = TexMobject("v_{4_0}").set_color(YELLOW)
        levo_f4 = TexMobject("u(", "v_{4_0}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{4_0}": YELLOW, ")": MAROON
        })
        label_coord41 = self.input_to_graph_point(x_min0, polinom_graph4)
        levo4.next_to(label_coord41, 10.3*DOWN+0.2*LEFT).scale(0.8)
        levo_f4.next_to(label_coord41, 0.1*UP+0.5*RIGHT).scale(0.8)
        desno4 = TexMobject("v_{4_1}}").set_color(YELLOW)
        desno_f4 = TexMobject("u(", "v_{4_1}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{4_1}": YELLOW, ")": MAROON
        })
        label_coord42 = self.input_to_graph_point(x_max0, polinom_graph4)
        desno4.next_to(label_coord42, 6.5*DOWN).scale(0.8)
        desno_f4.next_to(label_coord42, 0.2*UP+0.4*RIGHT).scale(0.8) 
        srednje4 = TexMobject("v_{4_2}").set_color(YELLOW)
        srednje_f4 = TexMobject("u(", "v_{4_2}", ")").set_color_by_tex_to_color_map({
            "u(": MAROON, "v_{4_2}": YELLOW, ")": MAROON
        })
        label_coord43 = self.input_to_graph_point(x_mid0, polinom_graph4)
        srednje4.next_to(label_coord43, 2.5*DOWN).scale(0.8)
        srednje_f4.next_to(label_coord43, 1.2*UP+0.5*RIGHT).scale(0.8)
        # rezultat
        rez41 = TexMobject(
            "v_{i+1_2}", "=", "v_{i+1_1}", " - "
            "u(", "v_{i+1_1}", ")",
            "{v_{i+1_1}", "-", "v_{i+1_0}", "\\over", "u(", "v_{i+1_1}", ") -", "u(", "v_{i+1_0}", ")}", "="
        )
        rez41.set_color_by_tex_to_color_map({
            "=": WHITE,  "+": WHITE, "v_{i+1_1}": YELLOW, "u(": MAROON, ")": MAROON
        })
        rez41.set_color_by_tex_to_color_map({
            "v_{i+1_2}": YELLOW, "v_{i+1_0}": YELLOW
        })
        rez42 = TexMobject(
            "=", "10.6\\textrm{ m/s}", " - "
            "1.3\\textrm{ m/s}", "\\cdot",
            "{10.6\\textrm{ m/s}", "-", "9.6\\textrm{ m/s}", "\\over", "1.3\\textrm{ m/s}", "-", "2.5\\textrm{ m/s}}", "="
        ).shift(1.5*DOWN+1.0*RIGHT)
        rez42.set_color_by_tex_to_color_map({
            "9.6": YELLOW, "10.6": YELLOW, "2.5": MAROON, "1.3": MAROON
        })
        convert_string_x = np.array2string(np.around(x_mid0, 2))
        string_print_x = f"{convert_string_x}"
        rez43 = TextMobject("= ", string_print_x,
                            " m/s").set_color(YELLOW).shift(4.3*RIGHT+2.9*DOWN)
        rez4 = VGroup(rez41, rez42, rez43).scale(0.75).shift(0.4*UP+2.0*LEFT)


        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py SekantnaMetoda -pl 
        self.setup_axes(animate=True, hideaxes=False)
        self.play(Write(x_os), Write(y_os))
        self.play(Write(fun_u))
        # prva iteracija
        self.play(ShowCreation(dashed_polinom_graph1))
        self.play(
            ShowCreation(tocka1L), ShowCreation(linija1L),
            ShowCreation(tocka1D), ShowCreation(linija1D)
        )
        self.play(
            ShowCreation(levo1), ShowCreation(levo_f1),
            ShowCreation(desno1), ShowCreation(desno_f1))
        self.play(ShowCreation(linear1))
        self.play(Write(rez11))
        self.wait(1)
        self.play(Write(rez12))
        self.play(Write(rez13))
        self.play(ShowCreation(tocka1S), ShowCreation(linija1S))
        self.play(ShowCreation(srednje1), ShowCreation(srednje_f1))
        self.wait(5)
        self.play(
            FadeOut(tocka1L), FadeOut(linija1L),
            FadeOut(tocka1D), FadeOut(linija1D),
            FadeOut(tocka1S), FadeOut(linija1S)
        )
        self.play(
            FadeOut(levo1), FadeOut(levo_f1),
            FadeOut(desno1), FadeOut(desno_f1),
            FadeOut(srednje1), FadeOut(srednje_f1)
        )
        self.play(FadeOut(rez1), FadeOut(
            dashed_polinom_graph1), FadeOut(linear1))
        self.wait(5)

        # druga iteracija
        self.play(ShowCreation(dashed_polinom_graph2))
        self.play(
            ShowCreation(tocka2L), ShowCreation(linija2L),
            ShowCreation(tocka2D), ShowCreation(linija2D)
        )
        self.play(
            ShowCreation(levo2), ShowCreation(levo_f2),
            ShowCreation(desno2), ShowCreation(desno_f2))
        self.play(ShowCreation(linear2))
        self.play(Write(rez21))
        self.wait(1)
        self.play(Write(rez22))
        self.play(Write(rez23))
        self.play(ShowCreation(tocka2S), ShowCreation(linija2S))
        self.play(ShowCreation(srednje2), ShowCreation(srednje_f2))
        self.wait(5)
        self.play(
            FadeOut(tocka2L), FadeOut(linija2L),
            FadeOut(tocka2D), FadeOut(linija2D),
            FadeOut(tocka2S), FadeOut(linija2S)
        )
        self.play(
            FadeOut(levo2), FadeOut(levo_f2),
            FadeOut(desno2), FadeOut(desno_f2),
            FadeOut(srednje2), FadeOut(srednje_f2) 
        )
        self.play(FadeOut(rez2), FadeOut(
            dashed_polinom_graph2), FadeOut(linear2))
        self.wait(5)

        # tretja iteracija
        self.play(ShowCreation(dashed_polinom_graph3))
        self.play(
            ShowCreation(tocka3L), ShowCreation(linija3L),
            ShowCreation(tocka3D), ShowCreation(linija3D)
        )
        self.play(
            ShowCreation(levo3), ShowCreation(levo_f3),
            ShowCreation(desno3), ShowCreation(desno_f3))
        self.play(ShowCreation(linear3))
        self.play(FadeOut(fun_u))
        self.play(Write(rez31))
        self.wait(1)
        self.play(Write(rez32))
        self.play(Write(rez33))
        self.play(ShowCreation(tocka3S), ShowCreation(linija3S))
        self.play(ShowCreation(srednje3), ShowCreation(srednje_f3))
        self.wait(5)
        self.play(
            FadeOut(tocka3L), FadeOut(linija3L),
            FadeOut(tocka3D), FadeOut(linija3D),
            FadeOut(tocka3S), FadeOut(linija3S)
        )
        self.play(
            FadeOut(levo3), FadeOut(levo_f3),
            FadeOut(desno3), FadeOut(desno_f3),
            FadeOut(srednje3), FadeOut(srednje_f3)
        )
        self.play(FadeOut(rez3), FadeOut(
            dashed_polinom_graph3), FadeOut(linear3))
        self.wait(5)

        # četrta iteracija
        self.play(ShowCreation(dashed_polinom_graph4))
        self.play(
            ShowCreation(tocka4L), ShowCreation(linija4L),
            ShowCreation(tocka4D), ShowCreation(linija4D)
        )
        self.play(
            ShowCreation(levo4), ShowCreation(levo_f4),
            ShowCreation(desno4), ShowCreation(desno_f4))
        self.play(ShowCreation(linear4))
        self.play(Write(rez41))
        self.wait(1)
        self.play(Write(rez42))
        self.play(Write(rez43))
        self.play(ShowCreation(tocka4S), ShowCreation(linija4S))
        self.play(ShowCreation(srednje4), ShowCreation(srednje_f4))
        self.wait(5)
        self.play(
            FadeOut(tocka4L), FadeOut(linija4L),
            FadeOut(tocka4D), FadeOut(linija4D),
            FadeOut(tocka4S), FadeOut(linija4S)
        )
        self.play(
            FadeOut(levo4), FadeOut(levo_f4),
            FadeOut(desno4), FadeOut(desno_f4),
            FadeOut(srednje4), FadeOut(srednje_f4)
        )
        self.play(FadeOut(rez4), FadeOut(
            dashed_polinom_graph4), FadeOut(linear4))
        self.wait(5)

class Credits(Scene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py Credits -pl

    def construct(self):  # KONSTRUKCIJA VSEH OBJEKTOV ##
        # 1 NASLOV
        naslov = TextMobject(
            "Numerično reševanje diferencialnih enačb").set_color(YELLOW).scale(1.1).shift(3*UP+1.8*LEFT)

        # 2 GLASBA
        glasba = TextMobject(
            "Glasba: https://www.bensound.com/").scale(0.8).set_color(RED)

        # 2 MAnim
        Manim1 = TextMobject("Narejeno z MAnim").scale(0.8).set_color(TEAL)
        Manim2 = TextMobject(
            "https://github.com/3b1b/manim").scale(0.8).set_color(TEAL)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(naslov))
        self.play(
            Write(Manim1.shift(5.05*LEFT+3*DOWN)),
            Write(Manim2.shift(3.8*LEFT+3.5*DOWN))
        )
        # self.play(Write(glasba.shift(3.4*LEFT+3.5*DOWN)))
        self.wait(5)


###############################
###############################
###############################
###############################

class IzrisImplicitnaOld(GraphScene):
    # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py IzrisImplicitnaOld -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 2,
        "x_axis_width": 8,
        "x_tick_frequency": 0.25,
        "x_axis_label": "",
        "y_min": 0,
        "y_max": 15,
        "y_tick_frequency": 1,
        "y_axis_height": 4.5,
        "graph_origin": 5.4*LEFT+2.4*DOWN,
        "y_axis_label": "",
        "x_labeled_nums": list(np.arange(0, 2.1, 0.5)),
        "y_labeled_nums": range(0, 16, 5),
        "exclude_zero_label": True,
        "default_graph_colors": [YELLOW],
        "x_label_decimals": 1,
    }

    def get_point_to_graph(
        self,
        x, graph,
        line_class=SmallDot,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_line_to_graph(
        self,
        x1, x2, graph,
        line_class=Line,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x1, graph),
            self.input_to_graph_point(x2, graph),
            **line_kwargs
        )

    def get_v_dashed_line_to_graph(
        self,
        x, graph,
        line_class=DashedLine,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.coords_to_point(x, 0),
            self.input_to_graph_point(x, graph),
            **line_kwargs
        )

    def get_h_dashed_line_to_graph(
        self,
        x, y, graph,
        line_class=DashedLine,
        **line_kwargs
    ):
        if "color" not in line_kwargs:
            line_kwargs["color"] = graph.get_color()
        return line_class(
            self.input_to_graph_point(x, graph),
            self.coords_to_point(0, y),
            **line_kwargs
        )

    def analiticna_resitev(self, t):
        m = 1
        c = 0.5
        g = 9.81
        return m*g/c*(1-np.e**(-c/m*t))

    def interpolacija(self, t):
        return -0.0510937*t**4 + 0.562031*t**3 - 3.20613*t**2 + 11.2789*t

    def f_zračni_upor(t, y, g=9.81, m=1., c=0.5):
        return g-c*y/m

    def euler(f, t, y0, *args, **kwargs):
        y = np.zeros_like(t)
        y[0] = y0
        h = t[1]-t[0]
        for i in range(len(t)-1):
            y[i+1] = y[i] + f(t[i], y[i], *args, **kwargs) * h
        return y

    t = np.linspace(0, 2, 5)
    v_rez = euler(f_zračni_upor, t, y0=0)

    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        # pretvorba primera v shemo
        vrstica1 = TextMobject(
            "Diferencialno enačbo padajočega telesa pretvorimo v ustrezno obliko:")
        vrstica1.scale(0.8)
        vrstica2 = TextMobject(
            "in jo uporabimo v Eulerjevi implicitni metodi:")
        vrstica2.scale(0.8)
        en1 = TexMobject("m \, g", "-", "c \,", "v", "=", "m \,", "v'")
        en1.set_color_by_tex_to_color_map({
            "m \, g": RED, "c \,": RED, "v": YELLOW, "m \,": RED, "v'": YELLOW
        })
        en2 = TexMobject("v'", "=", "g", "-", "\\frac{c}{m}", "v")
        en2.set_color_by_tex_to_color_map({
            "g": RED, "frac{c}{m}": RED, "v": YELLOW, "m": RED, "v'": YELLOW
        })
        en31 = TexMobject("v", "=", "v(", "t_i", ")", "=", "y_i")
        en31.set_color_by_tex_to_color_map(
            {"v": YELLOW, "t_i": TEAL, ")": YELLOW, "y_i": TEAL})
        en32 = TexMobject("v'", "=", "y'", "=", "f(", "t_{i+1}}",
                          ",", "y_{i+1}", ")").shift(0.8*DOWN+0.8*RIGHT)
        en32.set_color_by_tex_to_color_map(
            {"v'": YELLOW, "y'": YELLOW, "f(": RED, "t_{i+1}": GREEN, "y_{i+1}": YELLOW, ")": RED})
        en3 = VGroup(en31, en32)

        en41 = TexMobject("y_{i+1}", "=", "y_i", "+",
                          "f(", "t_{i+1}}", ",", "y_{i+1}", ")", "h")
        en41.set_color_by_tex_to_color_map({
            "y_{i+1}": YELLOW,
            "y_i": TEAL,
            "f(": RED,
            "t_{i+1}}": GREEN,
            ")": RED,
            "h": BLUE
        })
        en42 = TexMobject("v_{i+1}", "=", "v_i", "+",
                          "\\big(", "g-\\frac{c}{m}", "v_{i+1}}", "\\big)", "h")
        en42.set_color_by_tex_to_color_map({
            "v_{i+1}": YELLOW,
            "v_i": TEAL,
            "g-\\frac{c}{m}": RED,
            "\\big(": RED,
            "\\big)": RED,
            "h": BLUE
        }).shift(0.9*DOWN+0.35*RIGHT)
        en4 = VGroup(en41, en42).shift(DOWN)

        ## PRVA ITERACIJA ##
        # Zgornji tekst
        i1 = TexMobject(
            "i=0:", "\,v_0=v(t_0=0\\textrm{ s})=0\\textrm{ m/s}", "\\textrm{ (Začetni pogoj)}")
        i1.set_color_by_tex_to_color_map(
            {"i=0:": BLUE, "\,v_0=v(t_0=0\\textrm{ s})=0\\textrm{ m/s}": TEAL})
        i1.shift(3.6*UP+2.6*LEFT).scale(0.8)
        izracun11 = TexMobject(
            "= \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, +",
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)",
            "\cdot", "0.5\\textrm{ s}"
        )
        izracun11.scale(0.8).set_color_by_tex_to_color_map({
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)": RED,
            "0.5\\textrm{ s}": BLUE
        })
        v11 = TextMobject(
            "0\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.65*LEFT)
        v12 = TextMobject(
            "0\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.7*RIGHT)
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        # osi
        x_os = TexMobject("t\\textrm{ [s]}").scale(
            0.8).shift(2.4*DOWN+3.3*RIGHT)
        y_os = TexMobject(
            "v(t)\\textrm{ [m/s]}").scale(0.8).rotate(PI/2).shift(6.3*LEFT)
        analit_graph = self.get_graph(self.analiticna_resitev)
        dashed_analit_graph = DashedVMobject(analit_graph).set_color(WHITE)
        analit_lab = self.get_graph_label(
            analit_graph, label=f"v_a(t)").set_color(WHITE)
        interpolacija_graf = self.get_graph(self.interpolacija)
        ## Prvi korak ##
        # Newtonova metoda
        v1 = 0.01
        v0 = 0
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta11 = self.get_graph(
            lambda t: v0+(g-c*v1/m)*(t-0.5)+v1, x_min=0.78, x_max=0).set_color(RED)
        #
        x0 = 0.01
        x1 = 0.5
        y0 = 0
        tocka1L = self.get_point_to_graph(x0, interpolacija_graf, color=TEAL)
        linija1Lv = self.get_v_dashed_line_to_graph(
            x0, interpolacija_graf, color=TEAL)
        linija1Lh = self.get_h_dashed_line_to_graph(
            x0, self.interpolacija(x0), interpolacija_graf, color=TEAL)
        tocka1D = self.get_point_to_graph(x1, tangenta11, color=YELLOW)
        linija1Dv = self.get_v_dashed_line_to_graph(x1, tangenta11, color=BLUE)
        linija1Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta11, color=YELLOW)
        presecisce1 = self.input_to_graph_point(x1, tangenta11)
        ravna_linija1 = Line(
            presecisce1, (presecisce1[0]+1.22, presecisce1[1], 0)).set_color(RED)
        kot1 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle1 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot1
        )
        angle1.add_tip().scale(0.6).shift(7.65*LEFT+2.65*DOWN).set_color(RED)
        angle_label1 = TexMobject("v_1'").set_color(RED)
        angle_label1.scale(0.8).next_to(angle1, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka1L, tocka1D).set_color(RED)
        #
        input_triangle_p1 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p1 = RegularPolygon(n=3, start_angle=0).set_color(TEAL)
        input_triangle_p2 = input_triangle_p1.copy().set_color(TEAL)
        output_triangle_p2 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p1, output_triangle_p1, input_triangle_p2, output_triangle_p2:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p2.set_fill(YELLOW, 1)
        x_label_p1 = TexMobject("t_0").scale(0.8).set_color(TEAL)
        output_label_p1 = TexMobject("v_0").scale(0.8).set_color(TEAL)
        x_label_p2 = TexMobject("t_1").scale(0.8).set_color(TEAL)
        output_label_p2 = TexMobject("v_1=v_0").scale(0.6).set_color(YELLOW)
        output_label_p22 = TexMobject(
            "v_1=4.9\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p1.next_to(linija1Lv, DOWN)
        x_label_p2.next_to(linija1Dv, RIGHT)
        output_label_p1.next_to(linija1Lh, LEFT)
        output_label_p2.next_to(linija1Dh, UP)
        output_label_p22.next_to(linija1Dh, UP)
        input_triangle_p1.next_to(linija1Lv, DOWN, buff=0)
        input_triangle_p2.next_to(linija1Dv, DOWN, buff=0)
        output_triangle_p1.next_to(linija1Lh, LEFT, buff=0)
        output_triangle_p2.next_to(linija1Dh, LEFT, buff=0)
        h_oklepaj = Brace(VGroup(input_triangle_p1, input_triangle_p2), DOWN).shift(
            0.3*DOWN).set_color(BLUE)
        h_napis = h_oklepaj.get_text("$h$").scale(
            0.8).shift(0.2*UP).set_color(BLUE)
        rezultat11 = TexMobject(
            "= 4.9\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.3*UP+0.65*LEFT)

        ## Drugi korak ##
        # Newtonova metoda
        v1 = 4.905
        v0 = 0
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta12 = self.get_graph(
            lambda t: v0+(g-c*v1/m)*(t-0.5)+v1, x_min=0.78, x_max=0).set_color(RED)
        #
        tocka12L = self.get_point_to_graph(x0, interpolacija_graf, color=TEAL)
        linija12Lv = self.get_v_dashed_line_to_graph(
            x0, interpolacija_graf, color=TEAL)
        linija12Lh = self.get_h_dashed_line_to_graph(
            x0, self.interpolacija(x0), interpolacija_graf, color=TEAL)
        tocka12D = self.get_point_to_graph(x1, tangenta12, color=YELLOW)
        linija12Dv = self.get_v_dashed_line_to_graph(
            x1, tangenta12, color=BLUE)
        linija12Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta12, color=YELLOW)
        presecisce12 = self.input_to_graph_point(x1, tangenta12)
        ravna_linija12 = Line(
            presecisce12, (presecisce12[0]+1.22, presecisce12[1], 0)).set_color(RED)
        kot12 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle12 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot12
        )
        angle12.add_tip().scale(0.5).shift(7.65*LEFT+1.25*DOWN).set_color(RED)
        angle_label12 = TexMobject("v_1'").set_color(RED)
        angle_label12.scale(0.8).next_to(angle12, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka12L, tocka12D).set_color(RED)
        #
        output_triangle_p22 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in output_triangle_p22:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p22.set_fill(YELLOW, 1)
        x_label_p22 = TexMobject("t_1").scale(0.8).set_color(TEAL)
        output_label_p22 = TexMobject("v_1=4.9").scale(0.6).set_color(YELLOW)
        x_label_p22.next_to(linija12Dv, RIGHT)
        output_label_p22.next_to(linija12Dh, UP)
        output_label_p22.next_to(linija12Dh, UP)
        output_triangle_p22.next_to(linija12Dh, LEFT, buff=0)
        #
        izracun112 = TexMobject(
            "= \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, +",
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)",
            "\cdot", "0.5\\textrm{ s}"
        )
        izracun112.scale(0.8).set_color_by_tex_to_color_map({
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)": RED,
            "0.5\\textrm{ s}": BLUE
        }).shift(2.9*UP+2.63*RIGHT)
        v122 = TextMobject(
            "4.9\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.8*RIGHT)
        rezultat12 = TexMobject(
            "= 3.7\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.3*UP+0.65*LEFT)

        ## Tretji korak ##
        # Newtonova metoda
        v1 = 3.924
        v0 = 0
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta13 = self.get_graph(
            lambda t: v0+(g-c*v1/m)*(t-0.5)+v1, x_min=0.78, x_max=0).set_color(RED)
        #
        tocka13L = self.get_point_to_graph(x0, interpolacija_graf, color=TEAL)
        linija13Lv = self.get_v_dashed_line_to_graph(
            x0, interpolacija_graf, color=TEAL)
        linija13Lh = self.get_h_dashed_line_to_graph(
            x0, self.interpolacija(x0), interpolacija_graf, color=TEAL)
        tocka13D = self.get_point_to_graph(x1, tangenta13, color=YELLOW)
        linija13Dv = self.get_v_dashed_line_to_graph(
            x1, tangenta13, color=BLUE)
        linija13Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta13, color=YELLOW)
        presecisce13 = self.input_to_graph_point(x1, tangenta13)
        ravna_linija13 = Line(
            presecisce13, (presecisce13[0]+1.22, presecisce13[1], 0)).set_color(RED)
        kot13 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle13 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot13
        )
        angle13.add_tip().scale(0.51).shift(7.65*LEFT+1.51*DOWN).set_color(RED)
        angle_label13 = TexMobject("v_1'").set_color(RED)
        angle_label13.scale(0.8).next_to(angle13, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka13L, tocka13D).set_color(RED)
        #
        output_triangle_p23 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in output_triangle_p23:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p23.set_fill(YELLOW, 1)
        x_label_p23 = TexMobject("t_1").scale(0.8).set_color(TEAL)
        output_label_p23 = TexMobject("v_1=3.7").scale(0.6).set_color(YELLOW)
        x_label_p23.next_to(linija13Dv, RIGHT)
        output_label_p23.next_to(linija13Dh, UP)
        output_triangle_p23.next_to(linija13Dh, LEFT, buff=0)
        #
        v123 = TextMobject(
            "3.7\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.8*RIGHT)
        rezultat13 = TexMobject(
            "= 3.9\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.3*UP+0.65*LEFT)
        # zaklucek iteracije
        koncna_crta1 = self.get_graph(
            lambda t: v0+(g-c*v1/m)*(t-0.5)+v1, x_min=0.5, x_max=0).set_color(YELLOW)
        koncna_hitrost1 = TexMobject("v_1=3.9\\textrm{ m/s}").scale(
            0.6).set_color(YELLOW).next_to(linija13Dh, UP)

        ## DRUGA ITERACIJA ##
        # Zgornji tekst
        i2 = TexMobject("i=1:")
        i2.set_color_by_tex_to_color_map(
            {"i=1:": BLUE})
        i2.shift(3.63*UP+6.25*LEFT).scale(0.8)
        izracun21 = TexMobject(
            "= \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, +",
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)",
            "\cdot", "0.5\\textrm{ s}"
        )
        izracun21.scale(0.8).set_color_by_tex_to_color_map({
            "(9.81\\textrm{ m/s}^2-\\frac{0.5\\textrm{ kg/s}}{1.0\\textrm{ kg}}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,)": RED,
            "0.5\\textrm{ s}": BLUE
        }).shift(2.9*UP+2.5*RIGHT)
        v211 = TextMobject(
            "3.9\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.76*LEFT)
        v221 = TextMobject(
            "3.9\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.83*RIGHT)
        ## Prvi korak ##
        # Newtonova metoda
        v1 = 3.924
        v0 = 3.924
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta21 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.0), x_min=0.78+0.5, x_max=0.5).set_color(RED)
        #
        x0 = 0.5
        x1 = 1.0
        y0 = 3.924
        tocka21L = tocka13D.copy().set_color(TEAL)
        linija21Lv = linija13Dv.copy().set_color(TEAL)
        linija21Lh = linija13Dh.copy().set_color(TEAL)
        tocka21D = self.get_point_to_graph(x1, tangenta21, color=YELLOW)
        linija21Dv = self.get_v_dashed_line_to_graph(
            x1, tangenta21, color=BLUE)
        linija21Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta21, color=YELLOW)
        presecisce21 = self.input_to_graph_point(x1, tangenta21)
        ravna_linija21 = Line(
            presecisce21, (presecisce21[0]+1.22, presecisce21[1], 0)).set_color(RED)
        kot21 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle21 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot21
        )
        angle21.add_tip().scale(0.54).shift(5.65*LEFT+1.5*DOWN).set_color(RED)
        angle_label21 = TexMobject("v_2'").set_color(RED)
        angle_label21.scale(0.8).next_to(angle21, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka21L, tocka21D).set_color(RED)
        #
        input_triangle_p121 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p121 = RegularPolygon(
            n=3, start_angle=0).set_color(TEAL)
        input_triangle_p221 = input_triangle_p121.copy().set_color(TEAL)
        output_triangle_p221 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p121, output_triangle_p121, input_triangle_p221, output_triangle_p221:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p221.set_fill(YELLOW, 1)
        x_label_p121 = TexMobject("t_1").scale(0.8).set_color(TEAL)
        output_label_p121 = TexMobject("v_1").scale(0.8).set_color(TEAL)
        x_label_p221 = TexMobject("t_2").scale(0.8).set_color(TEAL)
        output_label_p221 = TexMobject("v_2=v_1").scale(0.6).set_color(YELLOW)
        output_label_p2212 = TexMobject(
            "v_2=7,8\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p121.next_to(linija21Lv, RIGHT)
        x_label_p221.next_to(linija21Dv, RIGHT)
        output_label_p121.next_to(linija21Lh, UP)
        output_label_p221.next_to(linija21Dh, UP)
        output_label_p2212.next_to(linija21Dh, UP)
        input_triangle_p121.next_to(linija21Lv, DOWN, buff=0)
        input_triangle_p221.next_to(linija21Dv, DOWN, buff=0)
        output_triangle_p121.next_to(linija21Lh, LEFT, buff=0)
        output_triangle_p221.next_to(linija21Dh, LEFT, buff=0)
        rezultat21 = TexMobject(
            "= 7.8\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.3*UP+0.9*LEFT)

        ## Drugi korak ##
        # Newtonova metoda
        v1 = 7.848
        v0 = 3.924
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta22 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.0), x_min=0.78+0.5, x_max=0.5).set_color(RED)
        #
        x0 = 0.5
        x1 = 1.0
        y0 = 3.924
        tocka22D = self.get_point_to_graph(x1, tangenta22, color=YELLOW)
        linija22Dv = self.get_v_dashed_line_to_graph(
            x1, tangenta22, color=BLUE)
        linija22Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta22, color=YELLOW)
        presecisce22 = self.input_to_graph_point(x1, tangenta22)
        ravna_linija22 = Line(
            presecisce22, (presecisce22[0]+1.22, presecisce22[1], 0)).set_color(RED)
        kot22 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle22 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot22
        )
        angle22.add_tip().scale(0.45).shift(5.65*LEFT+0.42*DOWN).set_color(RED)
        angle_label22 = TexMobject("v_2'").set_color(RED)
        angle_label22.scale(0.8).next_to(angle22, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka21L, tocka22D).set_color(RED)
        #
        input_triangle_p222 = input_triangle_p121.copy().set_color(TEAL)
        output_triangle_p222 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p222, output_triangle_p222:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p222.set_fill(YELLOW, 1)
        x_label_p222 = TexMobject("t_2").scale(0.8).set_color(TEAL)
        output_label_p222 = TexMobject("v_2=7.8").scale(0.6).set_color(YELLOW)
        output_label_p2222 = TexMobject(
            "v_1=7.8\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p222.next_to(linija22Dv, RIGHT)
        output_label_p222.next_to(linija22Dh, UP)
        output_label_p2222.next_to(linija22Dh, UP)
        input_triangle_p222.next_to(linija22Dv, DOWN, buff=0)
        output_triangle_p222.next_to(linija22Dh, LEFT, buff=0)
        #
        v222 = TextMobject(
            "7.8\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.83*RIGHT)
        rezultat22 = TexMobject(
            "= 6.9\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.3*UP+0.9*LEFT)

        ## Tretji korak ##
        # Newtonova metoda
        v1 = 7.0632
        v0 = 3.924
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta23 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.0), x_min=0.78+0.5, x_max=0.5).set_color(RED)
        #
        x0 = 0.5
        x1 = 1.0
        y0 = 3.924
        tocka23D = self.get_point_to_graph(x1, tangenta23, color=YELLOW)
        linija23Dv = self.get_v_dashed_line_to_graph(
            x1, tangenta23, color=BLUE)
        linija23Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta23, color=YELLOW)
        presecisce23 = self.input_to_graph_point(x1, tangenta23)
        ravna_linija23 = Line(
            presecisce23, (presecisce23[0]+1.22, presecisce23[1], 0)).set_color(RED)
        kot23 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle23 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot23
        )
        angle23.add_tip().scale(0.45).shift(5.65*LEFT+0.62*DOWN).set_color(RED)
        angle_label23 = TexMobject("v_2'").set_color(RED)
        angle_label23.scale(0.8).next_to(angle23, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka21L, tocka23D).set_color(RED)
        #
        input_triangle_p223 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        output_triangle_p223 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p223, output_triangle_p223:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p223.set_fill(YELLOW, 1)
        x_label_p223 = TexMobject("t_2").scale(0.8).set_color(TEAL)
        output_label_p223 = TexMobject("v_2=6.9").scale(0.6).set_color(YELLOW)
        output_label_p2232 = TexMobject(
            "v_2=6.9\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p223.next_to(linija22Dv, RIGHT)
        output_label_p223.next_to(linija23Dh, UP)
        output_label_p2232.next_to(linija23Dh, UP)
        input_triangle_p223.next_to(linija23Dv, DOWN, buff=0)
        output_triangle_p223.next_to(linija23Dh, LEFT, buff=0)
        #
        v232 = TextMobject(
            "6.9\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.83*RIGHT)
        rezultat23 = TexMobject(
            "= 7.1\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.3*UP+0.9*LEFT)
        # zaklucek iteracije
        koncna_crta2 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.0), x_min=1.0, x_max=0.5).set_color(YELLOW)
        koncna_hitrost2 = TexMobject("v_2=7.1\\textrm{ m/s}").scale(
            0.6).set_color(YELLOW).next_to(linija23Dh, UP)

        ## TRETJA ITERACIJA ##
        # Zgornji tekst
        i3 = TexMobject(
            "i=2:")
        i3.set_color_by_tex_to_color_map(
            {"i=2:": BLUE, "\,v_0=v(t_0=1.0\\textrm{ s})=7.1\\textrm{ m/s}": TEAL})
        i3.shift(3.63*UP+6.25*LEFT).scale(0.8)
        v311 = TextMobject(
            "7.1\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.76*LEFT)
        v321 = TextMobject(
            "9.6\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.83*RIGHT)
        ## Prvi korak ##
        # Newtonova metoda
        v1 = 9.57456
        v0 = 7.0632
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta31 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.5), x_min=0.78+1.0, x_max=1.0).set_color(RED)
        #
        x0 = 1.0
        x1 = 1.5
        y0 = 7.0632
        tocka31L = tocka23D.copy().set_color(TEAL)
        linija31Lv = linija23Dv.copy().set_color(TEAL)
        linija31Lh = linija23Dh.copy().set_color(TEAL)
        tocka31D = self.get_point_to_graph(x1, tangenta31, color=YELLOW)
        linija31Dv = self.get_v_dashed_line_to_graph(
            x1, tangenta31, color=BLUE)
        linija31Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta31, color=YELLOW)
        presecisce31 = self.input_to_graph_point(x1, tangenta31)
        ravna_linija31 = Line(
            presecisce31, (presecisce31[0]+1.22, presecisce31[1], 0)).set_color(RED)
        kot31 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle31 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot31
        )
        angle31.add_tip().scale(0.4).shift(3.65*LEFT+0.1*UP).set_color(RED)
        angle_label31 = TexMobject("v_3'").set_color(RED)
        angle_label31.scale(0.8).next_to(angle31, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka31L, tocka31D).set_color(RED)

        #
        input_triangle_p131 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p131 = RegularPolygon(
            n=3, start_angle=0).set_color(TEAL)
        input_triangle_p231 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p231 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p131, output_triangle_p131, input_triangle_p231, output_triangle_p231:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p231.set_fill(YELLOW, 1)
        x_label_p131 = TexMobject("t_2").scale(0.8).set_color(TEAL)
        output_label_p131 = TexMobject("v_2").scale(0.8).set_color(TEAL)
        x_label_p231 = TexMobject("t_3").scale(0.8).set_color(TEAL)
        output_label_p231 = TexMobject("v_3=v_2").scale(0.6).set_color(YELLOW)
        output_label_p2312 = TexMobject(
            "v_3=9.6\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p131.next_to(linija31Lv, RIGHT)
        x_label_p231.next_to(linija31Dv, RIGHT)
        output_label_p131.next_to(linija31Lh, UP)
        output_label_p231.next_to(linija31Dh, UP)
        output_label_p2312.next_to(linija31Dh, UP)
        input_triangle_p131.next_to(linija31Lv, DOWN, buff=0)
        input_triangle_p231.next_to(linija31Dv, DOWN, buff=0)
        output_triangle_p131.next_to(linija31Lh, LEFT, buff=0)
        output_triangle_p231.next_to(linija31Dh, LEFT, buff=0)
        rezultat31 = TexMobject(
            "= 9.6\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.3*UP+0.9*LEFT)

        # zaklucek iteracije
        koncna_crta3 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-1.5), x_min=1.5, x_max=1.0).set_color(YELLOW)
        koncna_hitrost3 = TexMobject("v_3=9.6\\textrm{ m/s}").scale(
            0.6).set_color(YELLOW).next_to(linija31Dh, UP)

        ## ČETRTA ITERACIJA ##
        # Zgornji tekst
        i4 = TexMobject(
            "i=3:")
        i4.set_color_by_tex_to_color_map(
            {"i=3:": BLUE, "\,v_0=v(t_0=1.0\\textrm{ s})=7.1\\textrm{ m/s}": TEAL})
        i4.shift(3.63*UP+6.25*LEFT).scale(0.8)
        v411 = TextMobject(
            "9.6\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+0.76*LEFT)
        v421 = TextMobject(
            "12\\textrm{ m/s}").scale(0.8).set_color(TEAL).shift(2.9*UP+4.83*RIGHT)
        ## Prvi korak ##
        # Newtonova metoda
        v1 = 11.584
        v0 = 9.57456
        g = 9.81
        m = 1.
        c = 0.5
        h = 0.5
        tangenta41 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-2), x_min=0.78+1.5, x_max=1.5).set_color(RED)
        #
        x0 = 1.5
        x1 = 2.0
        y0 = 9.57456
        tocka41L = tocka31D.copy().set_color(TEAL)
        linija41Lv = linija31Dv.copy().set_color(TEAL)
        linija41Lh = linija31Dh.copy().set_color(TEAL)
        tocka41D = self.get_point_to_graph(x1, tangenta41, color=YELLOW)
        linija41Dv = self.get_v_dashed_line_to_graph(
            x1, tangenta41, color=BLUE)
        linija41Dh = self.get_h_dashed_line_to_graph(
            x1, v1, tangenta41, color=YELLOW)
        presecisce41 = self.input_to_graph_point(x1, tangenta41)
        ravna_linija41 = Line(
            presecisce41, (presecisce41[0]+1.22, presecisce41[1], 0)).set_color(RED)
        kot41 = np.arctan(9.81-0.5/1*y0)/(2*np.pi)
        angle41 = Arc(
            radius=5.5,
            start_angle=0,
            angle=kot41
        )
        angle41.add_tip().scale(0.3).shift(1.65*LEFT+0.68*UP).set_color(RED)
        angle_label41 = TexMobject("v_4'").set_color(RED)
        angle_label41.scale(0.8).next_to(angle41, RIGHT).shift(0.2*LEFT)
        linija_odvod = Line(tocka41L, tocka41D).set_color(RED)

        #
        input_triangle_p141 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p141 = RegularPolygon(
            n=3, start_angle=0).set_color(TEAL)
        input_triangle_p241 = RegularPolygon(
            n=3, start_angle=TAU / 4).set_color(TEAL)
        output_triangle_p241 = RegularPolygon(
            n=3, start_angle=TAU).set_color(YELLOW)
        for triangle in input_triangle_p141, output_triangle_p141, input_triangle_p241, output_triangle_p241:
            triangle.set_fill(TEAL, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        output_triangle_p241.set_fill(YELLOW, 1)
        x_label_p141 = TexMobject("t_3").scale(0.8).set_color(TEAL)
        output_label_p141 = TexMobject("v_3").scale(0.8).set_color(TEAL)
        x_label_p241 = TexMobject("t_4").scale(0.8).set_color(TEAL)
        output_label_p241 = TexMobject("v_4=v_3").scale(0.6).set_color(YELLOW)
        output_label_p2412 = TexMobject(
            "v_4=12\\textrm{ m/s}").scale(0.6).set_color(YELLOW)
        x_label_p141.next_to(linija41Lv, RIGHT)
        x_label_p241.next_to(linija41Dv, RIGHT)
        output_label_p141.next_to(linija41Lh, UP)
        output_label_p241.next_to(linija41Dh, UP)
        output_label_p2412.next_to(linija41Dh, UP)
        input_triangle_p141.next_to(linija41Lv, DOWN, buff=0)
        input_triangle_p241.next_to(linija41Dv, DOWN, buff=0)
        output_triangle_p141.next_to(linija41Lh, LEFT, buff=0)
        output_triangle_p241.next_to(linija41Dh, LEFT, buff=0)
        rezultat41 = TexMobject(
            "= 12\\textrm{ m/s}").scale(0.8).set_color(YELLOW).shift(2.3*UP+0.9*LEFT)

        # zaklucek iteracije
        koncna_crta4 = self.get_graph(
            lambda t: v1+(g-c*v1/m)*(t-2), x_min=2, x_max=1.5).set_color(YELLOW)
        koncna_hitrost4 = TexMobject("v_4=12\\textrm{ m/s}").scale(
            0.6).set_color(YELLOW).next_to(linija41Dh, UP)

        v_implicitna = TexMobject("v_i(t)").set_color(
            YELLOW).shift(0.7*UP+3.2*RIGHT)

        ###########################
        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_diff_enacbe\manim_eulerjeva_metoda.py IzrisImplicitnaOld -pl
        self.play(Write(vrstica1.shift(3.2*UP+0.8*LEFT)))
        self.play(Write(en1.shift(2.2*UP+LEFT)))
        self.wait(2)
        self.play(Transform(en1, en2.shift(2.2*UP)))
        self.wait(2)
        self.play(Write(vrstica2.shift(1.0*UP+2.8*LEFT)))
        self.play(Write(en3.shift(UP+3*RIGHT)))
        self.wait(2)
        self.play(Write(en41))
        self.wait(2)
        self.play(Transform(en41, en42.shift(0.3*LEFT)))
        self.wait(2)
        self.play(FadeOut(en1), FadeOut(vrstica1), FadeOut(
            vrstica2), FadeOut(en3))
        # PRVA ITERACIJA
        self.play(Write(i1), ApplyMethod(en41.scale, 0.8))
        self.play(ApplyMethod(en41.shift, 4.8*UP+3.9*LEFT))
        self.play(Write(izracun11.shift(2.9*UP+2.5*RIGHT)),
                  Write(v11), Write(v12))
        self.wait(3)
        self.setup_axes(animate=True, hideaxes=False)
        self.play(Write(x_os), Write(y_os))
        self.play(ShowCreation(dashed_analit_graph),
                  ShowCreation(analit_lab))
        # prvi korak
        self.play(
            DrawBorderThenFill(input_triangle_p1),
            DrawBorderThenFill(output_triangle_p1),
            Write(x_label_p1),
            Write(output_label_p1),
            ShowCreation(tocka1L)
        )
        self.play(ShowCreation(h_oklepaj), Write(h_napis))
        self.play(
            DrawBorderThenFill(input_triangle_p2),
            Write(x_label_p2),
            ShowCreation(linija1Dv),
            DrawBorderThenFill(output_triangle_p2),
            Write(output_label_p2),
            ShowCreation(linija1Dh),
            ShowCreation(tocka1D)
        )
        self.play(Write(rezultat11))
        self.play(ShowCreation(ravna_linija1))
        self.play(
            ShowCreation(angle1),
            ShowCreation(angle_label1)
        )
        self.play(ShowCreation(tangenta11))
        # drugi korak
        self.wait(3)
        self.play(
            Uncreate(tangenta11),
            Uncreate(angle1),
            Uncreate(angle_label1),
            Uncreate(ravna_linija1),
            FadeOut(x_label_p2),
            FadeOut(linija1Dv),
            FadeOut(output_triangle_p2),
            FadeOut(output_label_p2),
            FadeOut(linija1Dh),
            FadeOut(tocka1D)
        )
        self.play(
            Transform(izracun11, izracun112),
            Transform(v12, v122),
            Transform(rezultat11, v122)
        )
        self.play(
            Write(x_label_p22),
            ShowCreation(linija12Dv),
            DrawBorderThenFill(output_triangle_p22),
            Write(output_label_p22),
            ShowCreation(linija12Dh),
            ShowCreation(tocka12D)
        )
        self.play(Write(rezultat12))
        self.play(ShowCreation(ravna_linija12))
        self.play(
            ShowCreation(angle12),
            ShowCreation(angle_label12)
        )
        self.play(ShowCreation(tangenta12))

        # tretji korak
        self.wait(3)
        self.play(
            Uncreate(tangenta12),
            Uncreate(angle12),
            Uncreate(angle_label12),
            Uncreate(ravna_linija12),
            FadeOut(x_label_p22),
            FadeOut(linija12Dv),
            FadeOut(output_triangle_p22),
            FadeOut(output_label_p22),
            FadeOut(linija12Dh),
            FadeOut(tocka12D)
        )
        self.play(
            Transform(v12, v123),
            Transform(rezultat12, v123),
            Transform(rezultat11, v123)
        )
        self.play(
            Write(x_label_p23),
            ShowCreation(linija13Dv),
            DrawBorderThenFill(output_triangle_p23),
            Write(output_label_p23),
            ShowCreation(linija13Dh),
            ShowCreation(tocka13D)
        )
        self.play(Write(rezultat13))
        self.play(ShowCreation(ravna_linija13))
        self.play(
            ShowCreation(angle13),
            ShowCreation(angle_label13)
        )
        self.play(ShowCreation(tangenta13))
        # zaklucek iteracije
        self.wait(3)
        self.play(
            Uncreate(angle13),
            Uncreate(angle_label13),
            Uncreate(ravna_linija13)
        )
        self.play(
            Transform(tangenta13, koncna_crta1),
            Transform(output_label_p23, koncna_hitrost1)
        )
        # DRUGA ITERACIJA
        # prvi korak
        self.play(
            FadeOut(rezultat13),
            Transform(i1, i2),
            Transform(izracun11, izracun21),
            Transform(v11, v211),
            Transform(v12, v221),
            FadeOut(rezultat11),
            FadeOut(rezultat12),
            ApplyMethod(en41.shift, 0.3*LEFT)
        )
        self.wait(1)
        self.play(
            FadeOut(input_triangle_p1),
            FadeOut(x_label_p1),
            FadeOut(output_triangle_p1),
            FadeOut(output_label_p1),
            Transform(input_triangle_p2, input_triangle_p121),
            Transform(x_label_p23, x_label_p121),
            Transform(linija13Dh, linija21Lh),
            Transform(linija13Dv, linija21Lv),
            Transform(output_triangle_p23, output_triangle_p121),
            Transform(output_label_p23, output_label_p121)
        )
        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT)
        )
        self.wait(1)
        self.play(
            Write(x_label_p221),
            ShowCreation(linija21Dv),
            DrawBorderThenFill(input_triangle_p221),
            DrawBorderThenFill(output_triangle_p221),
            Write(output_label_p221),
            ShowCreation(linija21Dh),
            ShowCreation(tocka21D)
        )
        self.play(Write(rezultat21))
        self.play(ShowCreation(ravna_linija21))
        self.play(
            ShowCreation(angle21),
            ShowCreation(angle_label21),
        )
        self.play(ShowCreation(tangenta21))
        self.wait(2)
        # drugi korak
        self.play(
            Uncreate(tangenta21),
            Uncreate(angle21),
            Uncreate(angle_label21),
            Uncreate(ravna_linija21),
            FadeOut(x_label_p221),
            FadeOut(linija21Dv),
            FadeOut(output_triangle_p221),
            FadeOut(output_label_p221),
            FadeOut(linija21Dh),
            FadeOut(tocka21D)
        )
        self.wait(1)
        self.play(
            Transform(rezultat21, v222),
            FadeOut(v12)
        )
        self.play(
            Write(x_label_p222),
            ShowCreation(linija22Dv),
            DrawBorderThenFill(output_triangle_p222),
            Write(output_label_p222),
            ShowCreation(linija22Dh),
            ShowCreation(tocka22D)
        )
        self.play(Write(rezultat22))
        self.play(ShowCreation(ravna_linija22))
        self.play(
            ShowCreation(angle22),
            ShowCreation(angle_label22),
        )
        self.play(ShowCreation(tangenta22))
        self.wait(2)
        # tretji korak
        self.play(
            Uncreate(tangenta22),
            Uncreate(angle22),
            Uncreate(angle_label22),
            Uncreate(ravna_linija22),
            FadeOut(x_label_p222),
            FadeOut(linija22Dv),
            FadeOut(output_triangle_p222),
            FadeOut(output_label_p222),
            FadeOut(linija22Dh),
            FadeOut(tocka22D)
        )
        self.wait(1)
        self.play(
            Transform(rezultat21, v232),
            Transform(rezultat22, v232)
        )
        self.play(
            Write(x_label_p223),
            ShowCreation(linija23Dv),
            DrawBorderThenFill(output_triangle_p223),
            Write(output_label_p223),
            ShowCreation(linija23Dh),
            ShowCreation(tocka23D)
        )
        self.play(Write(rezultat23))
        self.play(ShowCreation(ravna_linija23))
        self.play(
            ShowCreation(angle23),
            ShowCreation(angle_label23),
        )
        self.play(ShowCreation(tangenta23))
        self.wait(2)
        # zaklucek iteracije
        self.wait(3)
        self.play(
            Uncreate(angle23),
            Uncreate(angle_label23),
            Uncreate(ravna_linija23)
        )
        self.play(
            Transform(tangenta23, koncna_crta2),
            Transform(output_label_p223, koncna_hitrost2)
        )
        # TRETJA ITERACIJA
        self.play(
            FadeOut(rezultat23),
            Transform(i1, i3),
            Transform(v11, v311),
            Write(v321),
            FadeOut(rezultat21),
            FadeOut(rezultat22)
        )
        self.wait(1)
        self.play(
            FadeOut(input_triangle_p2),
            FadeOut(x_label_p23),
            FadeOut(output_triangle_p23),
            FadeOut(output_label_p23),
            FadeOut(linija13Dh),
            FadeOut(linija13Dv),
            Transform(input_triangle_p223, input_triangle_p131),
            Transform(x_label_p223, x_label_p131),
            Transform(linija23Dh, linija31Lh),
            Transform(linija23Dv, linija31Lv),
            Transform(output_triangle_p223, output_triangle_p131),
            Transform(output_label_p223, output_label_p131)
        )
        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT)
        )
        self.wait(1)
        self.play(
            Write(x_label_p231),
            ShowCreation(linija31Dv),
            DrawBorderThenFill(input_triangle_p231),
            DrawBorderThenFill(output_triangle_p231),
            Write(output_label_p2312),
            ShowCreation(linija31Dh),
            ShowCreation(tocka31D),

        )
        self.play(Write(rezultat31))
        self.play(ShowCreation(ravna_linija31))
        self.play(
            ShowCreation(angle31),
            ShowCreation(angle_label31),
        )
        self.play(ShowCreation(tangenta31))
        self.wait(2)
        # zaklucek iteracije
        self.wait(3)
        self.play(
            Uncreate(angle31),
            Uncreate(angle_label31),
            Uncreate(ravna_linija31)
        )
        self.play(
            Transform(tangenta31, koncna_crta3),
            Transform(output_label_p2312, koncna_hitrost3)
        )
        # ČETRTA ITERACIJA
        self.play(
            FadeOut(rezultat31),
            Transform(i1, i4),
            Transform(v11, v411),
            FadeOut(v321),
            Write(v421)
        )
        self.wait(1)
        self.play(
            FadeOut(input_triangle_p221),
            FadeOut(input_triangle_p223),
            FadeOut(x_label_p223),
            FadeOut(output_triangle_p223),
            FadeOut(output_label_p223),
            FadeOut(linija23Dh),
            FadeOut(linija23Dv),
            Transform(linija31Dh, linija41Lh),
            Transform(linija31Dv, linija41Lv),
            Transform(output_triangle_p231, output_triangle_p141),
            Transform(output_label_p2312, output_label_p141)
        )
        self.play(
            ApplyMethod(h_oklepaj.shift, 2*RIGHT),
            ApplyMethod(h_napis.shift, 2*RIGHT)
        )
        self.wait(1)
        self.play(
            Write(x_label_p241),
            ShowCreation(linija41Dv),
            DrawBorderThenFill(input_triangle_p241),
            DrawBorderThenFill(output_triangle_p241),
            Write(output_label_p2412),
            ShowCreation(linija41Dh),
            ShowCreation(tocka41D),

        )
        self.play(Write(rezultat41))
        self.play(ShowCreation(ravna_linija41))
        self.play(
            ShowCreation(angle41),
            ShowCreation(angle_label41),
        )
        self.play(ShowCreation(tangenta41))
        self.wait(2)
        # zaklucek iteracije
        self.wait(3)
        self.play(
            Uncreate(angle41),
            Uncreate(angle_label41),
            Uncreate(ravna_linija41)
        )
        self.play(
            Transform(tangenta41, koncna_crta4),
            Transform(output_label_p2412, koncna_hitrost4)
        )
        # zaključek
        self.wait(1)
        self.play(
            FadeOut(input_triangle_p231),
            FadeOut(input_triangle_p241),
            FadeOut(output_triangle_p231),
            FadeOut(output_triangle_p241),
            FadeOut(x_label_p231),
            FadeOut(output_label_p2412),
            FadeOut(x_label_p241),
            FadeOut(output_label_p2312),
            FadeOut(linija41Dh),
            FadeOut(linija41Dv),
            FadeOut(linija31Dh),
            FadeOut(linija31Dv),
            FadeOut(h_oklepaj),
            FadeOut(h_napis),
            FadeOut(i1),
            FadeOut(en41),
            FadeOut(v421),
            FadeOut(rezultat41),
            FadeOut(v11),
            FadeOut(izracun11)
        )
        self.play(Write(v_implicitna))

        self.wait(5)


#########################
#########################
#########################
#########################
#########################