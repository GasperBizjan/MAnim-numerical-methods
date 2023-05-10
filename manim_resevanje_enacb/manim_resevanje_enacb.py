from manimlib.imports import *
import os
import pyclbr

# v cmd vpišemo: "cd C:\Program Files (x86)\MAnim\manim-master" brez " " (pomik v ustrezno mapo)
# v cmd vpišemo inicializacijski ukaz (npr. "python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl") za začetek scene
# iz # python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl lahko odstranimo l za HD render
# Vsaka scena je definirana z svojim Class-om


class Title(Scene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py Title -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        # 1 NASLOV
        naslov = TextMobject("Numerično reševanje enačb").set_color(
            YELLOW).scale(1.5).shift(2.8*UP)

        # 2 AVTORJI
        avtor1 = TextMobject("prof. dr. Janko Slavič")
        avtor2 = TextMobject("Gašper Bizjan")
        p1 = VGroup(avtor1, avtor2)
        p1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF).scale(0.7)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(naslov))
        self.play(
            Write(avtor1.shift(3.1*DOWN+5.0*LEFT)),
            Write(avtor2.next_to(avtor1, DOWN).shift(0.6*LEFT)),
        )
        self.wait(2)
        self.play(FadeOut(p1))
        self.play(FadeOut(naslov))


class Uvod(GraphScene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py Uvod -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 5,
        "x_axis_width": 10,
        "x_tick_frequency": 0.5,
        "x_leftmost_tick": None,  # Change if different from x_min
        "y_min": -2,
        "y_max": 5,
        "y_tick_frequency": 2,
        "y_axis_height": 4,
        "graph_origin": 6*LEFT+1*DOWN,
        "axes_color": WHITE,
        "y_axis_label": "$y=f(x)$",
        "exclude_zero_label": True,
        "default_graph_colors": [ORANGE, PINK, GREEN],
    }
    ### KONSTRUKCIJA VSEH OBJEKTOV ###

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

    def prva_st(self, x):
        return -4.5*np.cos(1/2.2*x+0.3)+0.5

    def druga_st(self, x):
        return 1/2*(x-2.5)**2

    def tretja_st(self, x):
        return 1/2*(x-2.5)**3

    def construct(self):
        # 1 Prva stran
        vrstica1 = TextMobject("Obravnavamo od spremenljivke ",
                               r"$x$", " odvisno enačbo").set_color_by_tex("x", TEAL)
        en1 = TexMobject("f(", "x", ")=0", " .").set_color_by_tex_to_color_map(
            {"x": TEAL, "f(": RED, ")=0": RED})
        vrstica2 = TextMobject("Torej iščemo ", "ničle ",
                               "enačbe").set_color_by_tex("ničle", RED)
        en2 = TexMobject("y = f(", "x", ")").set_color_by_tex_to_color_map(
            {"x": TEAL, "y = f(": RED, ")": RED})
        pika1 = TextMobject(".")
        # 2. stran
        vrstica31 = TextMobject("Funkcija").set_color(RED)
        vrstica32 = TextMobject("ima lahko ničle:")
        vrstica41 = TextMobject("- prve stopnje").set_color(ORANGE)
        vrstica42 = TextMobject("- sode stopnje").set_color(PINK)
        vrstica43 = TextMobject("- lihe stopnje").set_color(GREEN)

        x_min0 = 0
        x_max0 = 5

        from scipy.optimize import fsolve

        # 1. polinom
        self.setup_axes(animate=False, hideaxes=True)
        polinom1_graph = self.get_graph(self.prva_st).set_color(ORANGE)
        polinom1_lab = self.get_graph_label(polinom1_graph, label=f"p_1(x)")
        tocka1 = self.get_point_to_graph(x_min0, polinom1_graph, color=TEAL)
        tocka1_pot = self.get_graph(
            lambda x: self.prva_st(x), x_min=x_min0, x_max=x_max0)
        linija11 = self.get_vertical_line_to_graph(
            x_min0, polinom1_graph, color=YELLOW)
        linija12 = self.get_vertical_line_to_graph(
            x_max0, polinom1_graph, color=YELLOW)
        tocka_nic1 = self.get_point_to_graph(
            fsolve(self.prva_st, 5), polinom1_graph, color=TEAL)
        y_je_0 = TexMobject("y=", "0").set_color_by_tex_to_color_map(
            {"y=": RED, "0": TEAL})

        # 2. polinom
        polinom2_graph = self.get_graph(self.druga_st).set_color(PINK)
        polinom2_lab = self.get_graph_label(polinom2_graph, label=f"p_2(x)")
        tocka2 = self.get_point_to_graph(x_min0, polinom2_graph, color=TEAL)
        tocka21_pot = self.get_graph(lambda x: self.druga_st(
            x), x_min=x_min0, x_max=(x_min0+x_max0)/2)
        tocka22_pot = self.get_graph(lambda x: self.druga_st(
            x), x_min=(x_min0+x_max0)/2, x_max=x_max0)
        linija21 = self.get_vertical_line_to_graph(
            x_min0, polinom2_graph, color=YELLOW)
        linija22 = self.get_vertical_line_to_graph(
            (x_min0+x_max0)/2, polinom2_graph, color=YELLOW)
        linija23 = self.get_vertical_line_to_graph(
            x_max0, polinom2_graph, color=YELLOW)
        # 3. polinom
        polinom3_graph = self.get_graph(self.tretja_st).set_color(GREEN)
        polinom3_lab = self.get_graph_label(polinom3_graph, label=f"p_3(x)")
        tocka3 = self.get_point_to_graph(x_min0, polinom3_graph, color=TEAL)
        tocka31_pot = self.get_graph(lambda x: self.tretja_st(
            x), x_min=x_min0, x_max=(x_min0+x_max0)/2)
        tocka32_pot = self.get_graph(lambda x: self.tretja_st(
            x), x_min=(x_min0+x_max0)/2, x_max=x_max0)
        linija31 = self.get_vertical_line_to_graph(
            x_min0, polinom3_graph, color=YELLOW)
        linija32 = self.get_vertical_line_to_graph(
            (x_min0+x_max0)/2, polinom2_graph, color=YELLOW)
        linija33 = self.get_vertical_line_to_graph(
            x_max0, polinom3_graph, color=YELLOW)

        # 3. stran
        vrstica51 = TextMobject("Obravnavane funkcije so na",
                                " intervalu ").set_color_by_tex("intervalu", YELLOW)
        vrstica52 = TexMobject("[", "x", ",", "y", "]").set_color(TEAL)
        vrstica52.set_color_by_tex_to_color_map(
            {"[": YELLOW, "x_0": TEAL, ",": YELLOW, "x_1": TEAL, "]": YELLOW})
        vrstica53 = TextMobject("zvezne...")
        vrstica5 = VGroup(vrstica51, vrstica52, vrstica53)
        vrstica5.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF/2)
        vrstica6 = TextMobject("...in omejimo se na", " ničle prve stopnje",
                               ".").set_color_by_tex("ničle prve stopnje", RED)

        # 1. polinom - zveznost
        x_min0 = 0.5
        x_max0 = 4.5
        self.setup_axes(animate=False, hideaxes=True)
        polinom1z_graph = self.get_graph(self.prva_st).set_color(ORANGE)
        polinom1z_lab = self.get_graph_label(polinom1z_graph, label=f"p_1(x)")
        tocka1z = self.get_point_to_graph(x_min0, polinom1z_graph, color=TEAL)
        tocka1z_pot = self.get_graph(
            lambda x: self.prva_st(x), x_min=x_min0, x_max=x_max0)
        tocka2z = self.get_point_to_graph(x_max0, polinom1z_graph, color=TEAL)
        tocka2z_pot = self.get_graph(lambda x: self.prva_st(
            x), x_min=x_max0, x_max=fsolve(self.prva_st, 5))
        linija11z = self.get_vertical_line_to_graph(
            x_min0, polinom1z_graph, color=YELLOW)
        linija12z = self.get_vertical_line_to_graph(
            x_max0, polinom1z_graph, color=YELLOW)
        linija13z = self.get_vertical_line_to_graph(
            (x_min0+x_max0)/2, polinom1z_graph, color=YELLOW)
        levo = TexMobject("x_0").set_color(TEAL)
        levo_f = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map({
            "f(": RED, "x_0": TEAL, ")": RED})
        label_coord1 = self.input_to_graph_point(x_min0, polinom1z_graph)
        levo.next_to(label_coord1, 8.8*UP)
        levo_f.next_to(label_coord1, 1*DOWN)
        desno = TexMobject("x_1").set_color(TEAL)
        desno_f = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map({
            "f(": RED, "x_1": TEAL, ")": RED})
        label_coord2 = self.input_to_graph_point(x_max0, polinom1z_graph)
        desno.next_to(label_coord2, 9.8*DOWN)
        desno_f.next_to(label_coord2, 1.2*UP)

    ### ANIMIRANJE OBJEKTOV ###
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py Uvod -pl
        self.play(Write(vrstica1.shift(2*UP)))
        self.play(Write(en1.shift(1*UP)))
        self.play(Write(vrstica2.shift(2.6*LEFT+0*DOWN)))
        self.play(Write(en2.shift(1*DOWN)),
                  Write(pika1.next_to(en2, RIGHT).shift(0.1*LEFT+0.1*DOWN)))
        self.wait(2)
        self.play(
            FadeOut(vrstica1), FadeOut(en1), FadeOut(vrstica2), FadeOut(pika1),
            ApplyMethod(en2.shift, 3*LEFT+4.5*UP)
        )
        self.play(Write(vrstica31.move_to(en2, LEFT).shift(2.2*LEFT)))
        self.play(Write(vrstica32.move_to(en2, RIGHT).shift(3.7*RIGHT+0.02*UP)))
        self.play(Write(vrstica41.move_to(
            vrstica31, DOWN).shift(0.5*DOWN+0.8*RIGHT)))
        self.setup_axes(animate=True, hideaxes=False)

        # prvi polinom
        self.play(ShowCreation(polinom1_graph), ShowCreation(polinom1_lab))
        #self.play(ShowCreation(linija11), ShowCreation(tocka1))
        #self.play(MoveAlongPath(tocka1, tocka1_pot), Transform(linija11, linija12))
        self.play(
            ShowCreation(tocka_nic1),
            Write(y_je_0.shift(1.8*DOWN)))
        self.wait(2)

        # drugi polinom
        self.play(Transform(vrstica41, vrstica42.move_to(vrstica41)))
        self.play(
            Transform(polinom1_graph, polinom2_graph),
            Transform(polinom1_lab, polinom2_lab))
        #    FadeOut(tocka1), FadeOut(linija11))
        #self.play(ShowCreation(linija21), ShowCreation(tocka2))
        #self.play(MoveAlongPath(tocka2, tocka21_pot), Transform(linija21, linija22))
        #self.play(MoveAlongPath(tocka2, tocka22_pot), Transform(linija21, linija23))
        self.wait(2)

        # tretji polinom
        self.play(Transform(vrstica41, vrstica43.move_to(vrstica41)))
        self.play(
            Transform(polinom1_graph, polinom3_graph),
            Transform(polinom1_lab, polinom3_lab))
        #   FadeOut(tocka2), FadeOut(linija21))
        #self.play(ShowCreation(linija31), ShowCreation(tocka3))
        #self.play(MoveAlongPath(tocka3, tocka31_pot), Transform(linija31, linija32))
        #self.play(MoveAlongPath(tocka3, tocka32_pot), Transform(linija31, linija33))
        self.wait(3)

        self.play(
            FadeOut(vrstica31),
            FadeOut(vrstica32),
            FadeOut(vrstica41),
            FadeOut(en2),
            FadeOut(polinom1_graph),
            Uncreate(polinom1_lab),
            FadeOut(y_je_0),
            FadeOut(tocka_nic1))
        self.play(Write(vrstica5.shift(3.2*UP+0.5*LEFT)))
        self.wait(3)

        # prvi polinom - zveznost
        self.play(ShowCreation(polinom1z_graph), ShowCreation(polinom1z_lab))
        self.play(
            ShowCreation(levo),
            ShowCreation(levo_f))
        self.play(ShowCreation(linija11z), ShowCreation(tocka1z))
        self.wait(1)
        self.play(
            MoveAlongPath(tocka1z, tocka1z_pot),
            Transform(linija11z, linija12z),
            ShowCreation(desno),
            ShowCreation(desno_f)
        )
        self.play(ShowCreation(tocka2z), FadeOut(tocka1z))
        self.play(
            MoveAlongPath(tocka2z, tocka2z_pot),
            Transform(linija11z, linija13z))
        self.play(FadeIn(y_je_0.shift(0.3*UP)))
        self.play(Write(vrstica6.shift(2.5*DOWN+2*RIGHT)))
        self.wait(5)


class KonkretnaFunkcija(GraphScene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py KonkretnaFunkcija -pl
    CONFIG = {
        "x_min": -10,
        "x_max": 40,
        "x_axis_width": 12,
        "x_tick_frequency": 10,
        "y_min": -250,
        "y_max": 100,
        "y_tick_frequency": 50,
        "y_axis_height": 6,
        "graph_origin": 3*LEFT,
        "axes_color": WHITE,
        "y_axis_label": "$y=f(x)$",
        "x_labeled_nums": range(-10, 40, 10),
        "y_labeled_nums": None,
        "exclude_zero_label": True,
        "default_graph_colors": [ORANGE, PINK, GREEN],
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

    def polinom_primer(self, x):
        return x**3 - 10*x**2 + 5

    # KONSTRUKCIJA VSEH OBJEKTOV ##

    def construct(self):
        # 1 Prva stran
        vrstica11 = TextMobject("Za konkreten polinom s koreni prve stopnje")
        en12 = TexMobject(
            "p(", "x", ")=", "1", "x", "^3 ", "-10", "x", "^2", "+5"
        )
        en12.set_color_by_tex_to_color_map({
            "x": TEAL, "p(": RED, ")=": RED, "^3": RED, "^2": RED, "1": YELLOW,  "-10": YELLOW,  "+5": YELLOW
        })
        vrstica13 = TextMobject("numerično poiščemo ničle.")
        vrstica1 = VGroup(vrstica11, en12, vrstica13).scale(0.8)
        vrstica1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF/2)
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        polinom_graph = self.get_graph(self.polinom_primer)
        polinom_lab = self.get_graph_label(polinom_graph, label=f"p(x)")
        vrstica2 = TextMobject("Če si pogledamo od bližje...")

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py KonkretnaFunkcija -pl
        self.play(Write(vrstica1))
        self.wait(2)
        self.play(FadeOut(vrstica11), FadeOut(vrstica13),
                  ApplyMethod(en12.shift, 3*UP+3*LEFT))
        self.setup_axes(animate=True, hideaxes=False)
        self.play(ShowCreation(polinom_graph), ShowCreation(polinom_lab))
        self.wait(1)
        self.play(Write(vrstica2.shift(2*DOWN+3*RIGHT)))

        self.wait(3)


class KonkretnaFunkcijaBlizje(GraphScene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py KonkretnaFunkcijaBlizje -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 1.3,
        "x_axis_width": 11,
        "x_tick_frequency": 10,
        "y_min": -6,
        "y_max": 6,
        "y_tick_frequency": 2,
        "y_axis_height": 6,
        "graph_origin": 6*LEFT+0.5*DOWN,
        "axes_color": WHITE,
        "y_axis_label": "$y$",
        "x_labeled_nums": list(np.arange(0.25, 1.3, 0.25)),
        "y_labeled_nums": range(-6, 7, 2),
        "exclude_zero_label": False,
        "default_graph_colors": [ORANGE, PINK, GREEN],
        "x_label_decimals": 2,
    }

    def polinom_primer(self, x):
        return x**3 - 10*x**2 + 5

    # KONSTRUKCIJA VSEH OBJEKTOV ##

    def construct(self):
        # 1 Prva stran
        en12 = TexMobject(
            "p(", "x", ")=", "1", "x", "^3 ", "-10", "x", "^2", "+5"
        )
        en12.set_color_by_tex_to_color_map({
            "x": TEAL, "p(": RED, ")=": RED, "^3": RED, "^2": RED, "1": YELLOW,  "-10": YELLOW,  "+5": YELLOW
        }).scale(0.8)
        # Graf
        self.setup_axes(animate=False, hideaxes=True)
        polinom_graph = self.get_graph(self.polinom_primer)
        polinom_lab = self.get_graph_label(polinom_graph, label=f"p(x)")
        vrstica1 = TextMobject("... vidimo, da je ničla v okolici ",
                               r"$ x = 0.75 $", ".").set_color_by_tex(r"$ x = 0.75 $", TEAL)
        vrstica21 = TextMobject("( Natančna vrednost ničle:")
        vrstica22 = TexMobject("x = 0.73460351").set_color(TEAL)
        vrstica23 = TextMobject(")")
        vrstica2 = VGroup(vrstica21, vrstica22, vrstica23)
        vrstica2.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF/2)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py KonkretnaFunkcijaBlizje -pl
        self.add(en12.shift(3*UP+3*LEFT))
        self.wait(1)
        self.setup_axes(animate=True, hideaxes=False)
        self.play(ShowCreation(polinom_graph),
                  ShowCreation(polinom_lab.shift(UP+2*LEFT)))
        self.play(Write(vrstica1.scale(0.8).shift(2.5*DOWN+2*LEFT)))
        self.play(Write(vrstica2.scale(0.8).shift(3.2*DOWN+1.2*LEFT)))

        self.wait(5)


class PrehodMedMetodami1(Scene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py PrehodMedMetodami1 -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        vrstica1 = TextMobject(
            "Prikažemo numerično iskanje korena z:").shift(2.8*UP+2*LEFT)
        vrstica21 = TextMobject("1. Bisekcijsko metodo,").set_color(YELLOW)
        vrstica22 = TextMobject("2. Sekantno metodo,").set_color(YELLOW)
        vrstica23 = TextMobject("3. Newtonovo metodo").set_color(YELLOW)
        vrstica2 = VGroup(vrstica21, vrstica22, vrstica23)
        vrstica2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF/1.5)
        vrstica3 = TextMobject("reševanja enačb.").shift(2.8*DOWN+3*RIGHT)

        vrstica4 = TextMobject("1. Bisekcijska metoda").scale(
            1.3).set_color(YELLOW)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(vrstica1))
        self.play(Write(vrstica2))
        self.play(Write(vrstica3))
        self.wait(1)
        self.play(
            FadeOut(vrstica1),
            FadeOut(vrstica22), FadeOut(vrstica23),
            FadeOut(vrstica3),
            Transform(vrstica21, vrstica4))
        self.wait(2)


class BisekcijskaMetoda(GraphScene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py BisekcijskaMetoda -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 1.3,
        "x_axis_width": 11,
        "x_tick_frequency": 10,
        "y_min": -6,
        "y_max": 6,
        "y_tick_frequency": 2,
        "y_axis_height": 6,
        "graph_origin": 6*LEFT+0.5*DOWN,
        "axes_color": WHITE,
        "y_axis_label": "$y$",
        "x_labeled_nums": list(np.arange(0.25, 1.3, 0.25)),
        "y_labeled_nums": range(-6, 7, 2),
        "exclude_zero_label": False,
        "default_graph_colors": [ORANGE, PINK, GREEN],
        "x_label_decimals": 2,
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

    def polinom_primer(self, x):
        return x**3 - 10*x**2 + 5

    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        vrstica1 = TextMobject("1. Bisekcijska metoda").scale(
            1.3).set_color(YELLOW)

        ## GRAF ##
        # 1. ITERACIJA
        self.setup_axes(animate=False, hideaxes=True)
        x_min0 = 0.05
        x_max0 = 1.15
        x_mid0 = (x_min0+x_max0)/2
        polinom_graph1 = self.get_graph(self.polinom_primer).set_color(ORANGE)
        polinom_graph2 = self.get_graph(
            self.polinom_primer, x_min=x_min0, x_m=x_max0).set_color(ORANGE)
        # linije in točke
        tocka1L = self.get_point_to_graph(x_min0, polinom_graph1, color=TEAL)
        tocka1D = self.get_point_to_graph(x_max0, polinom_graph1, color=TEAL)
        tocka1S = self.get_point_to_graph(x_mid0, polinom_graph1, color=TEAL)
        linija1L = self.get_vertical_line_to_graph(
            x_min0, polinom_graph1, color=YELLOW)
        linija1D = self.get_vertical_line_to_graph(
            x_max0, polinom_graph1, color=YELLOW)
        linija1S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph1, color=YELLOW)
        tocka1L_pot = self.get_graph(
            self.polinom_primer, x_min=x_min0, x_max=x_mid0)
        obarvano1 = self.get_area(polinom_graph1, t_min=x_mid0, t_max=x_max0)
        # tekst
        levo1 = TexMobject("x_0").set_color(TEAL)
        levo_f1 = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_0": TEAL, ")": RED})
        label_coord11 = self.input_to_graph_point(x_min0, polinom_graph1)
        levo1.next_to(label_coord11, 10.7*DOWN)
        levo_f1.next_to(label_coord11, 1.2*UP+2*RIGHT)
        desno1 = TexMobject("x_1").set_color(TEAL)
        desno_f1 = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_1": TEAL, ")": RED})
        label_coord12 = self.input_to_graph_point(x_max0, polinom_graph1)
        desno1.next_to(label_coord12, 13.8*UP)
        desno_f1.next_to(label_coord12, 1*UP+2*RIGHT)
        srednje1 = TexMobject("x_2", "=", "{x_0", "+", "x_1", "\\over 2}")
        srednje1.set_color_by_tex_to_color_map(
            {"x_2": TEAL, "=": WHITE, "{x_0": TEAL, "+": WHITE, "x_1": TEAL, "\\over 2}": WHITE})
        srednje_f1 = TexMobject("f(", "x_2", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_2": TEAL, ")": RED})
        label_coord13 = self.input_to_graph_point(x_mid0, polinom_graph1)
        srednje1.next_to(label_coord13, 6*DOWN)
        srednje_f1.next_to(label_coord13, 1*UP+2*RIGHT)
        # rezultat
        rez11 = TextMobject("$x_2=$")
        convert_string_x = np.array2string(np.around(x_mid0, 3))
        string_print_x = f"{convert_string_x}"
        rez12 = TextMobject(string_print_x)
        rez1 = VGroup(rez11, rez12).set_color(TEAL)
        rez1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2.5*DOWN+1.4*LEFT)
        # napaka
        e11 = TexMobject("\\epsilon_1=")
        e = np.abs(0.73460351-x_mid0)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e12 = TextMobject(string_print_e)
        e1 = VGroup(e11, e12).set_color(GREEN)
        e1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.1*LEFT).scale(0.8)

        # 2. ITERACIJA
        x_min0 = (x_min0+x_max0)/2
        x_max0 = 1.15
        x_mid0 = (x_min0+x_max0)/2
        # linije in točke
        linija2L = self.get_vertical_line_to_graph(
            x_min0, polinom_graph1, color=YELLOW)
        tocka2S = self.get_point_to_graph(x_mid0, polinom_graph1, color=TEAL)
        linija2S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph1, color=YELLOW)
        obarvano2 = self.get_area(polinom_graph1, t_min=x_min0, t_max=x_mid0)
        tocka1D_pot = self.get_graph(
            self.polinom_primer, x_min=x_max0, x_max=x_mid0)
        # tekst
        levo2 = TexMobject("x_0").set_color(TEAL)
        levo_f2 = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_0": TEAL, ")": RED})
        label_coord21 = self.input_to_graph_point(x_min0, polinom_graph1)
        levo2.next_to(label_coord21, 4.7*DOWN)
        levo_f2.next_to(label_coord21, 2*LEFT)
        srednje2 = TexMobject("x_2", "=", "{x_0", "+", "x_1", "\\over 2}")
        srednje2.set_color_by_tex_to_color_map(
            {"x_2": TEAL, "=": WHITE, "{x_0": TEAL, "+": WHITE, "x_1": TEAL, "\\over 2}": WHITE})
        srednje_f2 = TexMobject("f(", "x_2", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_2": TEAL, ")": RED})
        label_coord23 = self.input_to_graph_point(x_mid0, polinom_graph1)
        srednje2.next_to(label_coord23, 6*UP)
        srednje_f2.next_to(label_coord23, 1*DOWN+1*LEFT)
        # rezultat
        rez21 = TextMobject("$=$")
        convert_string_x = np.array2string(np.around(x_mid0, 3))
        string_print_x = f"{convert_string_x}"
        rez22 = TextMobject(string_print_x)
        rez2 = VGroup(rez21, rez22).set_color(TEAL)
        rez2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(0.5*UP+4.0*RIGHT)
        # napaka
        e21 = TexMobject("\\epsilon_2=")
        e = np.abs(0.73460351-x_mid0)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e22 = TextMobject(string_print_e)
        e2 = VGroup(e21, e22).set_color(GREEN)
        e2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.1*LEFT).scale(0.8)

        # 3. ITERACIJA
        x_max0 = (x_min0+x_max0)/2
        x_mid0 = (x_min0+x_max0)/2
        tocka3S = self.get_point_to_graph(x_mid0, polinom_graph1, color=TEAL)
        linija3S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph1, color=YELLOW)
        linija2D = self.get_vertical_line_to_graph(
            x_max0, polinom_graph1, color=YELLOW)
        # tekst
        desno2 = TexMobject("x_1").set_color(TEAL)
        desno_f2 = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_1": TEAL, ")": RED})
        label_coord31 = self.input_to_graph_point(x_max0, polinom_graph1)
        desno2.next_to(label_coord31, 5*UP)
        desno_f2.next_to(label_coord21, 10.5*RIGHT+6*DOWN)
        srednje3 = TexMobject("x_2", "=", "{x_0", "+", "x_1", "\\over 2}")
        srednje3.set_color_by_tex_to_color_map(
            {"x_2": TEAL, "=": WHITE, "{x_0": TEAL, "+": WHITE, "x_1": TEAL, "\\over 2}": WHITE})
        srednje_f3 = TexMobject("f(", "x_2", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_2": TEAL, ")": RED})
        label_coord33 = self.input_to_graph_point(x_mid0, polinom_graph1)
        srednje3.next_to(label_coord33, 3.5*DOWN+0.5*LEFT)
        srednje_f3.next_to(label_coord23, 2*LEFT+6*UP)
        # rezultat
        rez31 = TextMobject("$=$")
        convert_string_x = np.array2string(np.around(x_mid0, 3))
        string_print_x = f"{convert_string_x}"
        rez32 = TextMobject(string_print_x)
        rez3 = VGroup(rez31, rez32).set_color(TEAL)
        rez3.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2.9*DOWN+1.2*LEFT)
        # napaka
        e31 = TexMobject("\\epsilon_3=")
        e = np.abs(0.73460351-x_mid0)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e32 = TextMobject(string_print_e)
        e3 = VGroup(e31, e32).set_color(GREEN)
        e3.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.1*LEFT).scale(0.8)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py BisekcijskaMetoda -pl
        self.add(vrstica1)
        self.play(ApplyMethod(vrstica1.shift, 4*LEFT+3.5*UP))
        self.play(ApplyMethod(vrstica1.scale, 0.8))
        self.setup_axes(animate=True, hideaxes=False)
        self.play(ShowCreation(polinom_graph1))
        # prva iteracija
        self.play(
            ShowCreation(tocka1L), ShowCreation(linija1L),
            ShowCreation(tocka1D), ShowCreation(linija1D),
            Transform(polinom_graph1, polinom_graph2)
        )
        self.play(
            ShowCreation(levo1), ShowCreation(levo_f1),
            ShowCreation(desno1), ShowCreation(desno_f1))
        self.play(ShowCreation(tocka1S), ShowCreation(linija1S))
        self.play(ShowCreation(srednje1), ShowCreation(srednje_f1))
        self.play(Write(rez1), Write(e1))
        self.play(ShowCreation(obarvano1))
        self.wait(2)

        # druga iteracija
        self.play(
            FadeOut(levo1), FadeOut(levo_f1),
            MoveAlongPath(tocka1L, tocka1L_pot),
            Transform(linija1L, linija2L),
            Transform(srednje1, levo2), Transform(srednje_f1, levo_f2),
            Transform(rez1, levo2),
            FadeOut(e1)
        )
        self.play(FadeOut(obarvano1), FadeOut(linija1S))
        self.play(ShowCreation(tocka2S), ShowCreation(linija2S))
        self.play(ShowCreation(srednje2), ShowCreation(srednje_f2))
        self.play(Write(rez2), Write(e2))
        self.play(ShowCreation(obarvano2))
        self.wait(2)

        # tretja iteracija

        self.play(
            FadeOut(desno1), FadeOut(desno_f1),
            MoveAlongPath(tocka1D, tocka1D_pot),
            Transform(linija1D, linija2D),
            Transform(srednje2, desno2), Transform(srednje_f2, desno_f2),
            Transform(rez2, desno2),
            FadeOut(e2)
        )
        self.play(FadeOut(obarvano2), FadeOut(linija2S))
        self.play(ShowCreation(tocka3S), ShowCreation(linija3S))
        self.play(ShowCreation(srednje3), ShowCreation(srednje_f3))
        self.play(Write(rez3), Write(e3))
        self.wait(2)

        self.wait(5)


class PrehodMedMetodami2(Scene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py PrehodMedMetodami2 -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        vrstica1 = TextMobject(
            "Prikažemo numerično iskanje korena z:").shift(2.8*UP+2*LEFT)
        vrstica21 = TextMobject("1. Bisekcijsko metodo,").set_color(YELLOW)
        vrstica22 = TextMobject("2. Sekantno metodo,").set_color(YELLOW)
        vrstica23 = TextMobject("3. Newtonovo metodo").set_color(YELLOW)
        vrstica2 = VGroup(vrstica21, vrstica22, vrstica23)
        vrstica2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF/1.5)
        vrstica3 = TextMobject("reševanja enačb.").shift(2.8*DOWN+3*RIGHT)

        vrstica4 = TextMobject("2. Sekantna metoda").scale(
            1.3).set_color(YELLOW)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(vrstica1), Write(vrstica2), Write(vrstica3))
        self.wait(1)
        self.play(
            FadeOut(vrstica1),
            FadeOut(vrstica21), FadeOut(vrstica23),
            FadeOut(vrstica3),
            Transform(vrstica22, vrstica4))
        self.wait(2)


class SekantnaMetoda(GraphScene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py SekantnaMetoda -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 1.3,
        "x_axis_width": 11,
        "x_tick_frequency": 10,
        "y_min": -6,
        "y_max": 6,
        "y_tick_frequency": 2,
        "y_axis_height": 6,
        "graph_origin": 6*LEFT+0.5*DOWN,
        "axes_color": WHITE,
        "y_axis_label": "$y$",
        "x_labeled_nums": list(np.arange(0.25, 1.3, 0.25)),
        "y_labeled_nums": range(-6, 7, 2),
        "exclude_zero_label": False,
        "default_graph_colors": [ORANGE, PINK, GREEN],
        "x_label_decimals": 2,
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

    def polinom_primer(self, x):
        return x**3 - 10*x**2 + 5

    def linija_tocke1(self, x):
        x1 = 0.05
        x2 = 0.5
        y1 = x1**3 - 10*x1**2 + 5
        y2 = x2**3 - 10*x2**2 + 5
        m = (y2-y1)/(x2-x1)
        y = y1 + m*(x-x1)
        return y

    def linija_tocke2(self, x):
        x1 = 0.5
        x2 = 1.003
        y1 = x1**3 - 10*x1**2 + 5
        y2 = x2**3 - 10*x2**2 + 5
        m = (y2-y1)/(x2-x1)
        y = y1 + m*(x-x1)
        return y

    def linija_tocke3(self, x):
        x1 = 1.003
        x2 = 0.698
        y1 = x1**3 - 10*x1**2 + 5
        y2 = x2**3 - 10*x2**2 + 5
        m = (y2-y1)/(x2-x1)
        y = y1 + m*(x-x1)
        return y

    # KONSTRUKCIJA VSEH OBJEKTOV ##

    def construct(self):
        vrstica1 = TextMobject("2. Sekantna metoda").scale(
            1.3).set_color(YELLOW)

        ## GRAF ##
        # 1. ITERACIJA
        self.setup_axes(animate=False, hideaxes=True)
        x_min0 = 0.05
        x_max0 = 0.5
        x_mid0 = x_min0 - self.polinom_primer(x_min0)*(x_max0-x_min0)/(
            self.polinom_primer(x_max0)-self.polinom_primer(x_min0))
        polinom_graph1 = self.get_graph(self.polinom_primer).set_color(ORANGE)
        # linije in točke
        tocka1L = self.get_point_to_graph(x_min0, polinom_graph1, color=TEAL)
        tocka1L_pot = self.get_graph(
            self.polinom_primer, x_min=x_min0, x_max=x_max0)
        tocka1D = self.get_point_to_graph(x_max0, polinom_graph1, color=TEAL)
        tocka1D_pot = self.get_graph(
            self.polinom_primer, x_min=x_max0, x_max=x_mid0)
        tocka1S = self.get_point_to_graph(x_mid0, polinom_graph1, color=TEAL)
        linija1L = self.get_vertical_line_to_graph(
            x_min0, polinom_graph1, color=YELLOW)
        linija1D = self.get_vertical_line_to_graph(
            x_max0, polinom_graph1, color=YELLOW)
        linija1S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph1, color=YELLOW)
        linear1 = self.get_graph(self.linija_tocke1).set_color(PINK)
        # tekst
        levo1 = TexMobject("x_0").set_color(TEAL)
        levo_f1 = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_0": TEAL, ")": RED})
        label_coord11 = self.input_to_graph_point(x_min0, polinom_graph1)
        levo1.next_to(label_coord11, 11.7*DOWN)
        levo_f1.next_to(label_coord11, 1.2*UP+2*RIGHT)
        desno1 = TexMobject("x_1").set_color(TEAL)
        desno_f1 = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_1": TEAL, ")": RED})
        label_coord12 = self.input_to_graph_point(x_max0, polinom_graph1)
        desno1.next_to(label_coord12, 8*DOWN)
        desno_f1.next_to(label_coord12, 1*UP+2*RIGHT)
        srednje1 = TexMobject("x_2").set_color(TEAL)
        srednje_f1 = TexMobject("f(", "x_2", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_2": TEAL, ")": RED})
        label_coord13 = self.input_to_graph_point(x_mid0, polinom_graph1)
        srednje1.next_to(label_coord13, 10*UP)
        srednje_f1.next_to(label_coord13, 1*UP+2*RIGHT)
        # rezultat
        rez11 = TexMobject(
            "x_2", "=", "x_1", " - "
            "f(", "x_1", ")",
            "{x_1", "-", "x_0", "\\over", "f(", "x_1", ") -", "f(", "x_0", ")}", "="
        )
        rez11.set_color_by_tex_to_color_map(
            {"x_2": TEAL, "=": WHITE, "x_0": TEAL, "+": WHITE, "x_1": TEAL, "f(": RED, ")": RED})
        convert_string_x = np.array2string(np.around(x_mid0, 3))
        string_print_x = f"{convert_string_x}"
        rez12 = TextMobject(string_print_x).set_color(TEAL)
        rez1 = VGroup(rez11, rez12)
        rez1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2.5*DOWN+2.1*LEFT).scale(0.8)
        # napaka
        e11 = TexMobject("\\epsilon_1=")
        e = np.abs(0.73460351-x_mid0)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e12 = TextMobject(string_print_e)
        e1 = VGroup(e11, e12).set_color(GREEN)
        e1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.1*LEFT).scale(0.8)

        # 2. ITERACIJA
        x_min0 = x_max0
        x_max0 = x_mid0
        x_mid0 = x_min0 - self.polinom_primer(x_min0)*(x_max0-x_min0)/(
            self.polinom_primer(x_max0)-self.polinom_primer(x_min0))
        # linije in točke
        tocka2L = self.get_point_to_graph(x_min0, polinom_graph1, color=TEAL)
        tocka2L_pot = self.get_graph(
            self.polinom_primer, x_min=x_min0, x_max=x_max0)
        tocka2D = self.get_point_to_graph(x_max0, polinom_graph1, color=TEAL)
        tocka2D_pot = self.get_graph(
            self.polinom_primer, x_min=x_max0, x_max=x_mid0)
        tocka2S = self.get_point_to_graph(x_mid0, polinom_graph1, color=TEAL)
        linija2L = self.get_vertical_line_to_graph(
            x_min0, polinom_graph1, color=YELLOW)
        linija2D = self.get_vertical_line_to_graph(
            x_max0, polinom_graph1, color=YELLOW)
        linija2S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph1, color=YELLOW)
        linear2 = self.get_graph(self.linija_tocke2).set_color(PINK)
        # tekst
        levo2 = TexMobject("x_0").set_color(TEAL)
        levo_f2 = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_0": TEAL, ")": RED})
        label_coord21 = self.input_to_graph_point(x_min0, polinom_graph1)
        levo2.next_to(label_coord21, 8.7*DOWN)
        levo_f2.next_to(label_coord21, 1.2*UP+2*RIGHT)
        desno2 = TexMobject("x_1").set_color(TEAL)
        desno_f2 = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_1": TEAL, ")": RED})
        label_coord22 = self.input_to_graph_point(x_max0, polinom_graph1)
        desno2.next_to(label_coord22, 10*UP)
        desno_f2.next_to(label_coord22, 1*UP+2*RIGHT)
        srednje2 = TexMobject("x_2").set_color(TEAL)
        srednje_f2 = TexMobject("f(", "x_2", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_2": TEAL, ")": RED})
        label_coord23 = self.input_to_graph_point(x_mid0, polinom_graph1)
        srednje2.next_to(label_coord23, 3*DOWN)
        srednje_f2.next_to(label_coord23, 1*UP+2*RIGHT)
        # rezultat
        rez21 = TexMobject(
            "x_2", "=", "x_1", " - "
            "f(", "x_1", ")",
            "{x_1", "-", "x_0", "\\over", "f(", "x_1", ") -", "f(", "x_0", ")}", "="
        )
        rez21.set_color_by_tex_to_color_map(
            {"x_2": TEAL, "=": WHITE, "x_0": TEAL, "+": WHITE, "x_1": TEAL, "f(": RED, ")": RED})
        convert_string_x = np.array2string(np.around(x_mid0, 3))
        string_print_x = f"{convert_string_x}"
        rez22 = TextMobject(string_print_x).set_color(TEAL)
        rez2 = VGroup(rez21, rez22)
        rez2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2.5*DOWN+2.1*LEFT).scale(0.8)
        # napaka
        e21 = TexMobject("\\epsilon_2=")
        e = np.abs(0.73460351-x_mid0)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e22 = TextMobject(string_print_e)
        e2 = VGroup(e21, e22).set_color(GREEN)
        e2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.1*LEFT).scale(0.8)

        # 3. ITERACIJA
        x_min0 = x_max0
        x_max0 = x_mid0
        x_mid0 = x_min0 - self.polinom_primer(x_min0)*(x_max0-x_min0)/(
            self.polinom_primer(x_max0)-self.polinom_primer(x_min0))
        # linije in točke
        tocka3L = self.get_point_to_graph(x_min0, polinom_graph1, color=TEAL)
        tocka3D = self.get_point_to_graph(x_max0, polinom_graph1, color=TEAL)
        tocka3S = self.get_point_to_graph(x_mid0, polinom_graph1, color=TEAL)
        linija3L = self.get_vertical_line_to_graph(
            x_min0, polinom_graph1, color=YELLOW)
        linija3D = self.get_vertical_line_to_graph(
            x_max0, polinom_graph1, color=YELLOW)
        linija3S = self.get_dashed_line_to_graph(
            x_mid0, polinom_graph1, color=YELLOW)
        linear3 = self.get_graph(self.linija_tocke3).set_color(PINK)
        # tekst
        levo3 = TexMobject("x_0").set_color(TEAL)
        levo_f3 = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_0": TEAL, ")": RED})
        label_coord31 = self.input_to_graph_point(x_min0, polinom_graph1)
        levo3.next_to(label_coord31, 8.7*DOWN)
        levo_f3.next_to(label_coord31, 1.2*UP+2*RIGHT)
        desno3 = TexMobject("x_1").set_color(TEAL)
        desno_f3 = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_1": TEAL, ")": RED})
        label_coord32 = self.input_to_graph_point(x_max0, polinom_graph1)
        desno3.next_to(label_coord32, 2.1*DOWN+1.1*LEFT)
        desno_f3.next_to(label_coord32, 2*LEFT+0.05*UP)
        srednje3 = TexMobject("x_2").set_color(TEAL)
        srednje_f3 = TexMobject("f(", "x_2", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_2": TEAL, ")": RED})
        label_coord33 = self.input_to_graph_point(x_mid0, polinom_graph1)
        srednje3.next_to(label_coord33, 3*DOWN)
        srednje_f3.next_to(label_coord33, 1*UP+2*RIGHT)
        # rezultat
        rez31 = TexMobject(
            "x_2", "=", "x_1", " - "
            "f(", "x_1", ")",
            "{x_1", "-", "x_0", "\\over", "f(", "x_1", ") -", "f(", "x_0", ")}", "="
        )
        rez31.set_color_by_tex_to_color_map(
            {"x_2": TEAL, "=": WHITE, "x_0": TEAL, "+": WHITE, "x_1": TEAL, "f(": RED, ")": RED})
        convert_string_x = np.array2string(np.around(x_mid0, 3))
        string_print_x = f"{convert_string_x}"
        rez32 = TextMobject(string_print_x).set_color(TEAL)
        rez3 = VGroup(rez31, rez32)
        rez3.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2.5*DOWN+2.1*LEFT).scale(0.8)
        # napaka
        e31 = TexMobject("\\epsilon_3=")
        e = np.abs(0.73460351-x_mid0)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e32 = TextMobject(string_print_e)
        e3 = VGroup(e31, e32).set_color(GREEN)
        e3.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.1*LEFT).scale(0.8)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py SekantnaMetoda -pl
        self.add(vrstica1)
        self.play(ApplyMethod(vrstica1.shift, 4*LEFT+3.5*UP))
        self.play(ApplyMethod(vrstica1.scale, 0.8))
        self.setup_axes(animate=True, hideaxes=False)
        self.play(ShowCreation(polinom_graph1))
        # prva iteracija
        self.play(
            ShowCreation(tocka1L), ShowCreation(linija1L),
            ShowCreation(tocka1D), ShowCreation(linija1D)
        )
        self.play(
            ShowCreation(levo1), ShowCreation(levo_f1),
            ShowCreation(desno1), ShowCreation(desno_f1))
        self.play(ShowCreation(linear1))
        self.play(ShowCreation(tocka1S), ShowCreation(linija1S))
        self.play(ShowCreation(srednje1), ShowCreation(srednje_f1))
        self.play(Write(rez1), Write(e1))
        self.wait(2)

        # druga iteracija
        self.play(FadeOut(linear1))
        self.play(
            Transform(levo1, levo2),
            Transform(desno1, desno2),
            Transform(levo_f1, levo_f2),
            Transform(desno_f1, desno_f2),
            MoveAlongPath(tocka1L, tocka1L_pot),
            MoveAlongPath(tocka1D, tocka1D_pot),
            Transform(linija1L, linija2L),
            Transform(linija1D, linija2D),
            FadeOut(srednje1), FadeOut(srednje_f1),
            FadeOut(e1), FadeOut(rez1)
        )
        self.play(FadeOut(linija1S), FadeOut(tocka1S))
        self.play(ShowCreation(linear2))
        self.play(ShowCreation(tocka2S), ShowCreation(linija2S))
        self.play(ShowCreation(srednje2), ShowCreation(srednje_f2))
        self.play(Write(rez2), Write(e2))
        self.wait(2)

        # tretja iteracija
        self.play(FadeOut(linear2))
        self.play(
            Transform(levo1, levo3),
            Transform(desno1, desno3),
            Transform(levo_f1, levo_f3),
            Transform(desno_f1, desno_f3),
            MoveAlongPath(tocka1L, tocka2L_pot),
            MoveAlongPath(tocka1D, tocka2D_pot),
            Transform(linija1L, linija3L),
            Transform(linija1D, linija3D),
            FadeOut(srednje2), FadeOut(srednje_f2),
            FadeOut(e2), FadeOut(rez2),
        )
        self.play(ShowCreation(linear3))
        self.play(ShowCreation(tocka3S), ShowCreation(linija3S))
        self.play(ShowCreation(srednje3), ShowCreation(srednje_f3))
        self.play(Write(rez3), Write(e3))

        self.wait(5)


class PrehodMedMetodami3(Scene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py PrehodMedMetodami3 -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        vrstica1 = TextMobject(
            "Prikažemo numerično iskanje korena z:").shift(2.8*UP+2*LEFT)
        vrstica21 = TextMobject("1. Bisekcijsko metodo,").set_color(YELLOW)
        vrstica22 = TextMobject("2. Sekantno metodo,").set_color(YELLOW)
        vrstica23 = TextMobject("3. Newtonovo metodo").set_color(YELLOW)
        vrstica2 = VGroup(vrstica21, vrstica22, vrstica23)
        vrstica2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF/1.5)
        vrstica3 = TextMobject("reševanja enačb.").shift(2.8*DOWN+3*RIGHT)

        vrstica4 = TextMobject("3. Newtonova metoda").scale(
            1.3).set_color(YELLOW)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(vrstica1), Write(vrstica2), Write(vrstica3))
        self.wait(1)
        self.play(
            FadeOut(vrstica1),
            FadeOut(vrstica21), FadeOut(vrstica22),
            FadeOut(vrstica3),
            Transform(vrstica23, vrstica4))
        self.wait(2)


class NewtonovaMetodaIzpeljava(Scene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py NewtonovaMetodaIzpeljava -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        vrstica1 = TextMobject("3. Newtonova metoda").scale(
            1.3).set_color(YELLOW)
        vrstica2 = TextMobject("Izpeljava z uporabo ", "Taylorjeve vrste",
                               ":").set_color_by_tex("Taylorjeve vrste", RED)
        en1 = TexMobject(
            "f(", "x_{i+1}", ")", "=",
            "f(", "x_i", ")", "+",
            "f'(", "x_i", ")", "\\big(", "x_{i+1}", "-", "x_i", "\\big)", "+", "O^2", "[", "x_{i+1}", "-", "x_i", "]")
        en1.set_color_by_tex_to_color_map({
            "f(": RED, ")": RED, "(": RED,
            "\\big(": WHITE, "\\big)": WHITE,
            "[": GREEN, "]": GREEN,
            "+": WHITE, "-": WHITE, "=": WHITE,
            "x_i": TEAL, "x_{i+1}": TEAL,
            "O^2": GREEN
        })

        en21 = TexMobject("f(", "x_{i+1}", ")")
        en21.set_color_by_tex_to_color_map(
            {"f(": RED, ")": RED, "(": RED, "x_{i+1}": TEAL})
        en22 = TexMobject(
            "=", "f(", "x_i", ")", "+",
            "f'(", "x_i", ")", "\\big(", "x_{i+1}", "-", "x_i", "\\big)")
        en22.set_color_by_tex_to_color_map({
            "f(": RED, ")": RED, "(": RED,
            "\\big(": WHITE, "\\big)": WHITE,
            "[": GREEN, "]": GREEN,
            "+": WHITE, "-": WHITE, "=": WHITE,
            "x_i": TEAL, "x_{i+1}": TEAL,
            "O^2": GREEN
        })
        en23 = TexMobject(
            "+", "O^2", "[", "x_{i+1}", "-", "x_i", "]")
        en23.set_color_by_tex_to_color_map({
            "[": GREEN, "]": GREEN,
            "+": WHITE, "-": WHITE, "=": WHITE,
            "x_i": TEAL, "x_{i+1}": TEAL,
            "O^2": GREEN
        })
        en2 = VGroup(en21, en22, en23)
        en2.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF/2)

        vrstica3 = TextMobject("Naj bo pri ", r"$x_{i+1}$", " vrednost funkcije nič, potem velja:").set_color_by_tex(
            "Taylorjeve vrste", RED).set_color_by_tex(r"$x_{i+1}$", TEAL)

        en3 = TexMobject("0")

        en4 = TexMobject("\\cancel{+ O^2 [x_{i+1} - x_i ]}").set_color(GREEN)
        vrstica4 = TextMobject("Lahko izpeljemo:")
        en51 = TexMobject(
            "x_{i+1}", "=", "x_i", "-").set_color(TEAL)
        en51.set_color_by_tex_to_color_map({
            "f(": RED, ")": RED, "(": RED,
            "\\big(": WHITE, "\\big)": WHITE,
            "+": WHITE, "-": WHITE, "=": WHITE,
            "x_i": TEAL, "x_{i+1}": TEAL,
        })
        en52 = TexMobject(
            "f(", "x_i", ")", "\\over", "f'(", "x_i", ")")
        en52.set_color_by_tex_to_color_map({
            "f(": RED, ")": RED, "(": RED,
            "\\big(": WHITE, "\\big)": WHITE,
            "+": WHITE, "-": WHITE, "=": WHITE,
            "x_i": TEAL, "x_{i+1}": TEAL,
        })
        en5 = VGroup(en51, en52)
        en5.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF/2)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py NewtonovaMetodaIzpeljava -pl
        self.add(vrstica1)
        self.play(ApplyMethod(vrstica1.shift, 4.2*LEFT+3.5*UP))
        self.play(ApplyMethod(vrstica1.scale, 0.8))
        self.play(Write(vrstica2.scale(0.8).shift(2*UP+3.6*LEFT)))
        self.play(Write(en1.scale(0.8).shift(1.2*UP+1.6*LEFT)))
        self.wait(3)
        self.play(Write(vrstica3.scale(0.8).shift(2.4*LEFT)))
        self.play(Write(en2.scale(0.8).shift(0.8*DOWN+1.6*LEFT)))
        self.play(Transform(en21, en3.scale(0.8).shift(0.8*DOWN+4.9*LEFT)))
        self.wait(3)
        self.play(Transform(en23, en4.scale(0.8).shift(0.8*DOWN+1.85*RIGHT)))
        self.wait(0.8)
        self.play(FadeOut(en23))
        self.wait(3)
        self.play(Write(vrstica4.scale(0.8).shift(2*DOWN+5.35*LEFT)))
        self.play(Transform(en2, en5.shift(2.0*DOWN)))
        self.wait(5)


class NewtonovaMetoda(GraphScene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py NewtonovaMetoda -pl
    CONFIG = {
        "x_min": 0,
        "x_max": 1.3,
        "x_axis_width": 11,
        "x_tick_frequency": 10,
        "y_min": -6,
        "y_max": 6,
        "y_tick_frequency": 2,
        "y_axis_height": 6,
        "graph_origin": 6*LEFT+0.5*DOWN,
        "axes_color": WHITE,
        "y_axis_label": "$y$",
        "x_labeled_nums": list(np.arange(0.25, 1.3, 0.25)),
        "y_labeled_nums": range(-6, 7, 2),
        "exclude_zero_label": False,
        "default_graph_colors": [ORANGE, PINK, GREEN],
        "x_label_decimals": 2,
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

    def polinom_primer(self, x):
        return x**3 - 10*x**2 + 5

    def odvod_polinoma(self, x):
        return 3*x**2 - 20*x

    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        vrstica1 = TextMobject("3. Newtonova metoda").scale(
            1.3).set_color(YELLOW)

        ## GRAF ##
        # 1. ITERACIJA
        self.setup_axes(animate=False, hideaxes=True)
        x0 = 0.3
        xs = x0 - self.polinom_primer(x0)/self.odvod_polinoma(x0)
        polinom_graph1 = self.get_graph(self.polinom_primer).set_color(ORANGE)
        # linije in točke
        tocka1L = self.get_point_to_graph(x0, polinom_graph1, color=TEAL)
        tocka1L_pot = self.get_graph(self.polinom_primer, x_min=x0, x_max=xs)
        tocka1S = self.get_point_to_graph(xs, polinom_graph1, color=TEAL)
        linija1L = self.get_vertical_line_to_graph(
            x0, polinom_graph1, color=YELLOW)
        linija1S = self.get_dashed_line_to_graph(
            xs, polinom_graph1, color=YELLOW)
        kot1 = -np.arctan(self.odvod_polinoma(x0))/(2*np.pi)
        tangenta1 = TangentLine(
            polinom_graph1, alpha=kot1+0.01, length=25.0).set_color(PINK)
        presecisce = self.input_to_graph_point(x0, polinom_graph1)
        ravna_linija1 = DashedLine(
            presecisce, (presecisce[0]+3, presecisce[1], 0)).set_color(YELLOW)
        angle1 = Arc(
            radius=3.0,
            start_angle=(kot1-0.23),
            angle=-(kot1+0.11)
        ).set_color(YELLOW)
        angle1.add_tip()
        # tekst
        levo1 = TexMobject("x_0").set_color(TEAL)
        levo_f1 = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_0": TEAL, ")": RED})
        label_coord11 = self.input_to_graph_point(x0, polinom_graph1)
        levo1.next_to(label_coord11, 10*DOWN+0.2*RIGHT)
        levo_f1.next_to(label_coord11, 1.2*UP+1*RIGHT)
        angle_f1 = TexMobject("f'(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f'(": RED, "x_0": TEAL, ")": RED}
        )
        angle_f1.next_to(label_coord11, 14*RIGHT)
        srednje1 = TexMobject("x_1").set_color(TEAL)
        srednje_f1 = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_1": TEAL, ")": RED})
        label_coord13 = self.input_to_graph_point(xs, polinom_graph1)
        srednje1.next_to(label_coord13, 10.5*UP)
        srednje_f1.next_to(label_coord13, 0.5*UP+1.5*RIGHT)
        # rezultat
        rez11 = TexMobject(
            "x_1", "=", "x_0", " - ",
            "{f(", "x_0", ")", "\\over", "f'(", "x_0", ")}", "="
        )
        rez11.set_color_by_tex_to_color_map(
            {"x_1": TEAL, "=": WHITE, "x_0": TEAL, "+": WHITE, "x_1": TEAL, "f(": RED, ")": RED, "f'(": RED})
        convert_string_x = np.array2string(np.around(xs, 3))
        string_print_x = f"{convert_string_x}"
        rez12 = TextMobject(string_print_x).set_color(TEAL)
        rez1 = VGroup(rez11, rez12)
        rez1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2.5*DOWN+3.4*LEFT).scale(0.8)
        # napaka
        e11 = TexMobject("\\epsilon_1=")
        e = np.abs(0.73460351-xs)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e12 = TextMobject(string_print_e)
        e1 = VGroup(e11, e12).set_color(GREEN)
        e1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.1*LEFT).scale(0.8)

        # 2. ITERACIJA
        x0 = xs
        xs = x0 - self.polinom_primer(x0)/self.odvod_polinoma(x0)
        # linije in točke
        tocka2L = self.get_point_to_graph(x0, polinom_graph1, color=TEAL)
        tocka2L_pot = self.get_graph(self.polinom_primer, x_min=x0, x_max=xs)
        tocka2S = self.get_point_to_graph(xs, polinom_graph1, color=TEAL)
        linija2L = self.get_vertical_line_to_graph(
            x0, polinom_graph1, color=YELLOW)
        linija2S = self.get_dashed_line_to_graph(
            xs, polinom_graph1, color=YELLOW)
        kot2 = -np.arctan(self.odvod_polinoma(x0))/(2*np.pi)
        tangenta2 = TangentLine(
            polinom_graph1, alpha=kot2+0.55, length=25.0).set_color(PINK)
        presecisce2 = self.input_to_graph_point(x0, polinom_graph1)
        ravna_linija2 = DashedLine(
            presecisce2, (presecisce2[0]+0.7, presecisce2[1], 0)).set_color(YELLOW)
        angle2 = Arc(
            radius=2.0,
            start_angle=(kot2-0.27),
            angle=-(kot2+0.11)
        ).set_color(YELLOW)
        angle2.add_tip()
        # tekst
        levo2 = TexMobject("x_0").set_color(TEAL)
        levo_f2 = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_0": TEAL, ")": RED})
        label_coord21 = self.input_to_graph_point(x0, polinom_graph1)
        levo2.next_to(label_coord21, 10.5*UP)
        levo_f2.next_to(label_coord21, 0.5*UP+1.5*RIGHT)
        angle_f2 = TexMobject("f'(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f'(": RED, "x_0": TEAL, ")": RED}
        )
        angle_f2.next_to(label_coord21, 4*RIGHT+DOWN)
        srednje2 = TexMobject("x_1").set_color(TEAL)
        srednje_f2 = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_1": TEAL, ")": RED})
        label_coord23 = self.input_to_graph_point(xs, polinom_graph1)
        srednje2.next_to(label_coord23, 1.8*UP)
        srednje_f2.next_to(label_coord23, 0.7*DOWN+1.3*LEFT)
        # rezultat
        rez21 = TexMobject(
            "x_1", "=", "x_0", " - ",
            "{f(", "x_0", ")", "\\over", "f'(", "x_0", ")}", "="
        )
        rez21.set_color_by_tex_to_color_map(
            {"x_1": TEAL, "=": WHITE, "x_0": TEAL, "+": WHITE, "x_1": TEAL, "f(": RED, ")": RED, "f'(": RED})
        convert_string_x = np.array2string(np.around(xs, 3))
        string_print_x = f"{convert_string_x}"
        rez22 = TextMobject(string_print_x).set_color(TEAL)
        rez2 = VGroup(rez21, rez22)
        rez2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2.5*DOWN+3.2*LEFT).scale(0.8)
        # napaka
        e21 = TexMobject("\\epsilon_2=")
        e = np.abs(0.73460351-xs)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e22 = TextMobject(string_print_e)
        e2 = VGroup(e21, e22).set_color(GREEN)
        e2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.1*LEFT).scale(0.8)

        # 3. ITERACIJA
        x0 = xs
        xs = x0 - self.polinom_primer(x0)/self.odvod_polinoma(x0)
        # linije in točke
        tocka3L = self.get_point_to_graph(x0, polinom_graph1, color=TEAL)
        tocka3L_pot = self.get_graph(self.polinom_primer, x_min=x0, x_max=xs)
        tocka3S = self.get_point_to_graph(xs, polinom_graph1, color=TEAL)
        linija3L = self.get_vertical_line_to_graph(
            x0, polinom_graph1, color=YELLOW)
        linija3S = self.get_dashed_line_to_graph(
            xs, polinom_graph1, color=YELLOW)
        kot3 = -np.arctan(self.odvod_polinoma(x0))/(2*np.pi)
        tangenta3 = TangentLine(
            polinom_graph1, alpha=kot3+0.35, length=25.0).set_color(PINK)
        presecisce3 = self.input_to_graph_point(x0, polinom_graph1)
        ravna_linija3 = DashedLine(
            presecisce3, (presecisce3[0]+2.4, presecisce3[1], 0)).set_color(YELLOW)
        angle3 = Arc(
            radius=5.0,
            start_angle=(kot3-0.28),
            angle=-(kot3+0.11)
        ).set_color(YELLOW)
        angle3.add_tip()
        # tekst
        levo3 = TexMobject("x_0").set_color(TEAL)
        levo_f3 = TexMobject("f(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_0": TEAL, ")": RED})
        label_coord31 = self.input_to_graph_point(x0, polinom_graph1)
        levo3.next_to(label_coord31, 2.5*UP)
        levo_f3.next_to(label_coord31, 0.6*DOWN+1.6*LEFT)
        angle_f3 = TexMobject("f'(", "x_0", ")").set_color_by_tex_to_color_map(
            {"f'(": RED, "x_0": TEAL, ")": RED}
        )
        angle_f3.next_to(label_coord31, 11*RIGHT+2.5*DOWN)
        srednje3 = TexMobject("x_1").set_color(TEAL)
        srednje_f3 = TexMobject("f(", "x_1", ")").set_color_by_tex_to_color_map(
            {"f(": RED, "x_1": TEAL, ")": RED})
        label_coord33 = self.input_to_graph_point(xs, polinom_graph1)
        srednje3.next_to(label_coord23, 1.7*UP+1.3*RIGHT)
        srednje_f3.next_to(label_coord23, 2.4*DOWN)
        # rezultat
        rez31 = TexMobject(
            "x_1", "=", "x_0", " - ",
            "{f(", "x_0", ")", "\\over", "f'(", "x_0", ")}", "="
        )
        rez31.set_color_by_tex_to_color_map(
            {"x_1": TEAL, "=": WHITE, "x_0": TEAL, "+": WHITE, "x_1": TEAL, "f(": RED, ")": RED, "f'(": RED})
        convert_string_x = np.array2string(np.around(xs, 3))
        string_print_x = f"{convert_string_x}"
        rez32 = TextMobject(string_print_x).set_color(TEAL)
        rez3 = VGroup(rez31, rez32)
        rez3.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2.5*DOWN+3.2*LEFT).scale(0.8)
        # napaka
        e31 = TexMobject("\\epsilon_3=")
        e = np.abs(0.73460351-xs)
        convert_string_e = np.array2string(np.around(e, 7))
        string_print_e = f"{convert_string_e}"
        e32 = TextMobject(string_print_e)
        e3 = VGroup(e31, e32).set_color(GREEN)
        e3.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.5*DOWN+4.2*LEFT).scale(0.8)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py NewtonovaMetoda -pl
        self.add(vrstica1.shift(4.2*LEFT+3.5*UP).scale(0.8))
        self.setup_axes(animate=True, hideaxes=False)
        self.play(ShowCreation(polinom_graph1))
        # prva iteracija
        self.play(ShowCreation(tocka1L), ShowCreation(linija1L))
        self.play(ShowCreation(levo1), ShowCreation(levo_f1))
        self.play(ShowCreation(ravna_linija1))
        self.play(ShowCreation(angle1.shift(3.4*LEFT+1.6*UP)),
                  ShowCreation(angle_f1), ShowCreation(tangenta1))
        self.play(ShowCreation(tocka1S), ShowCreation(linija1S))
        self.play(ShowCreation(srednje1), ShowCreation(srednje_f1))
        self.play(Write(rez1), Write(e1))
        self.wait(2)

        # druga iteracija
        self.play(
            FadeOut(angle1), FadeOut(angle_f1),
            FadeOut(tangenta1), FadeOut(ravna_linija1)
        )
        self.play(
            Transform(levo1, levo2),
            Transform(levo_f1, levo_f2),
            MoveAlongPath(tocka1L, tocka1L_pot),
            FadeOut(srednje1), FadeOut(srednje_f1),
            Transform(linija1L, linija2L)
        )
        self.play(
            FadeOut(linija1S), FadeOut(tocka1S),
            FadeOut(rez1), FadeOut(e1))

        self.play(ShowCreation(ravna_linija2))
        self.play(ShowCreation(angle2.shift(1.4*RIGHT+2.6*DOWN)),
                  ShowCreation(angle_f2), ShowCreation(tangenta2))
        self.play(ShowCreation(tocka2S), ShowCreation(linija2S))
        self.play(ShowCreation(srednje2), ShowCreation(srednje_f2))
        self.play(Write(rez2), Write(e2))
        self.wait(2)

        # tretja iteracija
        self.play(
            FadeOut(angle2), FadeOut(angle_f2),
            FadeOut(tangenta2), FadeOut(ravna_linija2)
        )
        self.play(
            Transform(levo1, levo3),
            Transform(levo_f1, levo_f3),
            MoveAlongPath(tocka2L, tocka2L_pot),
            FadeOut(srednje2), FadeOut(srednje_f2),
            Transform(linija1L, linija3L),
            FadeOut(tocka1L)
        )
        self.play(
            FadeOut(linija2S), FadeOut(tocka2S),
            FadeOut(rez2), FadeOut(e2))

        self.play(ShowCreation(ravna_linija3))
        self.play(ShowCreation(angle3.shift(2.0*LEFT+0.5*DOWN)),
                  ShowCreation(angle_f3), ShowCreation(tangenta3))
        self.play(ShowCreation(tocka3S), ShowCreation(linija3S))
        self.play(ShowCreation(srednje3), ShowCreation(srednje_f3))
        self.play(Write(rez3), Write(e3))
        self.wait(5)


class Primerjava(Scene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py Primerjava -pl
    # KONSTRUKCIJA VSEH OBJEKTOV ##
    def construct(self):
        vrstica_tekst = TextMobject("Primerjava napak metod").set_color(
            YELLOW).shift(3.1*UP+3.9*LEFT)

        # tabela
        rectangle1 = Rectangle(height=0.8, width=12).shift(0.4*DOWN)
        rectangle2 = Rectangle(height=0.8, width=12).shift(0.4*UP)
        rectangle3 = Rectangle(height=0.8, width=12).shift(1.2*UP)
        rectangle4 = Rectangle(height=2.4, width=4).shift(0.1*LEFT+0.4*UP)
        tab = VGroup(rectangle1, rectangle2, rectangle3,
                     rectangle4).set_color(WHITE)

        zad11 = TextMobject(" Bisekcijska metoda ")
        zad12 = TextMobject(" Sekantna metoda ")
        zad13 = TextMobject(" Newtonova metoda ")
        zad1 = VGroup(zad11, zad12, zad13).set_color(WHITE)
        zad1.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF).shift(
            2*UP).scale(0.9).set_color(RED)

        zad20 = TexMobject(" \\epsilon ")
        zad21 = TextMobject(" 1 ")
        zad22 = TextMobject(" 2 ")
        zad23 = TextMobject(" 3 ")
        zad2 = VGroup(zad20, zad21, zad22, zad23).set_color(WHITE)
        zad2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF).shift(
            6.5*LEFT+0.75*UP).set_color(GREEN)

        # vrednosti
        vrstica11 = TexMobject(" 0.1346035 ")
        vrstica12 = TexMobject(" 0.2680293 ")
        vrstica13 = TexMobject(" 0.2856408 ")
        vrstica1 = VGroup(vrstica11, vrstica12, vrstica13)
        vrstica1.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF*4)

        vrstica21 = TexMobject(" 0.1403965 ")
        vrstica22 = TexMobject(" 0.0367856 ")
        vrstica23 = TexMobject(" 0.0341094 ")
        vrstica2 = VGroup(vrstica21, vrstica22, vrstica23)
        vrstica2.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF*4)

        vrstica31 = TexMobject(" 0.0028965 ")
        vrstica32 = TexMobject(" 0.0050353 ")
        vrstica33 = TexMobject(" 0.0006612 ")
        vrstica3 = VGroup(vrstica31, vrstica32, vrstica33)
        vrstica3.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF*4)

        vrstica = VGroup(vrstica1, vrstica2, vrstica3).set_color(TEAL)
        vrstica.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF).shift(0.4*UP)

        # tekst
        zad31 = TextMobject(" Najpočasneje konvergira")
        zad32 = TextMobject(" bisekcijska metoda, ").set_color(RED)
        zad33 = TextMobject(" najhitreje pa")
        zad34 = TextMobject(" Newtonova metoda.").set_color(RED)
        zad3 = VGroup(zad31, zad32, zad33, zad34)
        zad3.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2*DOWN).scale(0.8)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py Primerjava -pl
        self.play(Write(vrstica_tekst))
        self.play(ShowCreation(tab))
        self.play(Write(zad1), Write(zad2))
        self.play(Write(vrstica.shift(0.65*RIGHT)))
        self.play(Write(zad3))

        self.wait(5)


class Credits(Scene):
    # python -m manim manim_resevanje_enacb\manim_resevanje_enacb.py Credits -pl

    def construct(self):  # KONSTRUKCIJA VSEH OBJEKTOV ##
        # 1 NASLOV
        naslov = TextMobject(
            "Numerično reševanje enačb").set_color(YELLOW).scale(1.1).shift(3*UP+3*LEFT)

        # 2 GLAsBA
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
