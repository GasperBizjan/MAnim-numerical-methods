from manimlib.imports import *
import os
import pyclbr

# v cmd vpišemo: "cd C:\Program Files (x86)\MAnim\manim-master" brez " " (pomik v ustrezno mapo)
# v cmd vpišemo inicializacijski ukaz (npr. "python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl") za začetek scene
# iz # python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl lahko odstranimo l za HD render
# Vsaka scena je definirana z svojim Class-om

#############################################
#############################################
#### SETUP FUNKCIJE - NISO DEL ANIMACIJE ####
#############################################
#############################################


class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 8,
        "height": FRAME_Y_RADIUS * 3,
        "width": 14,
        "grid_stroke": 0.3,
        "grid_color": WHITE,
        "axis_color": GREEN,
        "axis_stroke": 2,
        "labels_scale": 0.1,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height,
                    rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(
            self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [
                          0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = TextMobject(f"{coord_point}").scale(
                        self.labels_scale)
                    label.next_to(ubication, directions_buff,
                                  buff=self.labels_buff)
                    labels.add(label)

        self.add(grid)  # , axes),  # labels)


def coord(x, y, z=0):
    return np.array([x, y, z])


def getX(mob):
    return mob.get_center()[0]


def getY(mob):
    return mob.get_center()[1]

# Abstract class:


class PathScene(GraphScene):
    # python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl
    CONFIG = {
        "x_coords": [],
        "y_coords": [],
        "x_min": -1.65,
        "x_max": 4.65,
        "x_axis_width": 11,
        "x_tick_frequency": 0.5,
        "x_leftmost_tick": -1,  # Change if different from x_min
        "y_min": -1,
        "y_max": 1,
        "y_tick_frequency": 0.5,
        "graph_origin": 3.5*LEFT,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-1, 5, 1),
        "y_labeled_nums": range(-2, 2, 1),
        "exclude_zero_label": True,
    }

    """
    The setup method it is executed before the construct method,
    so whatever they write in the setup method will be executed
    before the construct method
    """

    def showvid(self):
        self.wait(3)

    def setup(self):
        self.screen_grid = ScreenGrid()
        # tuples = [(0,3),(1,-2)...]
        self.tuples = list(zip(self.x_coords, self.y_coords))

        dots, labels, numbers = self.get_all_mobs()
        self.add(self.screen_grid, dots, labels, numbers)

    def get_dots(self, coords):
        # This is called list comprehension, learn to use it here:
        # https://www.youtube.com/watch?v=AhSvKGTh28Q
        dots = VGroup(*[Dot(coord(x, y)) for x, y in coords])
        return dots

    def get_dot_labels(self, dots, direction=RIGHT):
        labels = VGroup(*[
            # This is called f-strings, learn to use it here:
            # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
            TexMobject(f"({getX(dot)},{getY(dot)})", height=0.25)\
            .next_to(dot, direction, buff=SMALL_BUFF)
            # This is called Multi-line statement, learn how to use it here:
            # https://www.programiz.com/python-programming/statement-indentation-comments
            for dot in dots
        ])
        return labels

    def get_dot_numbers(self, dots):
        numbers = VGroup(*[
            TextMobject(f"{n}", height=0.2).next_to(dot, DOWN, buff=SMALL_BUFF)
            for n, dot in zip(range(1, len(dots)+1), dots)
        ])
        return numbers

    def get_all_mobs(self):
        dots = self.get_dots(self.tuples)
        labels = self.get_dot_labels(dots)
        numbers = self.get_dot_numbers(dots)
        return dots, labels, numbers

####################################################
####################################################
############### ZAČETEK ANIMIRANJA #################
####################################################
####################################################


class Title(PathScene):
    # python -m manim manim_lagrange\manim_lagrange.py Title -pl
    def koncni_polinom(self, x):
        def lagrange_interpolacija(x, x_int, y_int):
            y = 0.
            for i in range(len(x_int)):
                Lx = 1.0
                for j in range(len(x_int)):
                    if j != i:
                        Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
                y += y_int[i] * Lx
            return y
        n = 3
        x_vhod = np.linspace(1, 4, n)
        y_vhod = np.cos(x_vhod)
        f = lagrange_interpolacija(x, x_vhod, y_vhod)
        return f

    def construct(self):  # KONSTRUKCIJA VSEH OBJEKTOV ##
        # 1 PRIKAZ TOČK
        self.setup_axes(animate=False, hideaxes=True)
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(1.7*np.cos(x0), decimals=2)
        koordinate_za_interpolirat = [coord(x0[i], y0[i]) for i in range(n)]
        new_points = np.array(koordinate_za_interpolirat)
        new_points_labels = np.array(koordinate_za_interpolirat)
        new_dots = self.get_dots(new_points[:, :2])
        VGroup(new_dots).set_color(TEAL).shift(1.62*LEFT+0.2*DOWN).scale(1.75)

        # 2 KONČNI POLINOM
        koncni_polinom_graf = self.get_graph(
            self.koncni_polinom, self.function_color)
        koncni_polinom_lab = self.get_graph_label(
            koncni_polinom_graf, label=f"L(x)").shift(1*DOWN+0*LEFT)
        koncni_polinom_coord = self.input_to_graph_point(
            TAU, koncni_polinom_graf)

        # 3 NASLOV
        naslov = TextMobject(
            "Interpolacija z Lagrangevo metodo").set_color(YELLOW).scale(1.5).shift(UP)

        # 4 AVTORJI
        avtor1 = TextMobject("prof. dr. Janko Slavič")
        avtor2 = TextMobject("Gašper Bizjan")
        p1 = VGroup(avtor1, avtor2)
        p1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF).scale(0.8)


        ### ANIMIRANJE OBJEKTOV ###
        self.play(
            Write(new_dots),
            ShowCreation(koncni_polinom_graf),
            Write(koncni_polinom_lab))

        self.play(Write(naslov))
        self.play(
            Write(avtor1.shift(3.0*DOWN+4.5*LEFT)),
            Write(avtor2.next_to(avtor1, DOWN).shift(0.7*LEFT)),
            )
        self.wait(2)
        self.play(
            FadeOut(new_dots),
            FadeOut(koncni_polinom_graf),
            FadeOut(koncni_polinom_lab),
            FadeOut(p1))
        self.play(FadeOut(naslov))


class ShowPoints(PathScene):
    # python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl
    def construct(self):  # KONSTRUKCIJA VSEH OBJEKTOV ##
        # 1 IZRIS IN BLIŽANJE KOSINUSA (izpuščeno)
        # self.setup_axes(animate=False, hideaxes=True)
        # func_graph1 = self.get_graph(self.func_to_graph, self.function_color)
        # func_graph2 = self.get_graph(self.func_to_graph, self.function_color)
        # func_graph3 = self.get_graph(self.func_to_graph, self.function_color)
        # func_graph4 = self.get_graph(self.func_to_graph, self.function_color)
        # graph_lab = self.get_graph_label(func_graph1, label="\\cos(x)")
        # label_coord = self.input_to_graph_point(TAU, func_graph4)

        # 2 DISKRETIZACIJA KOSINUSA NA TOČKE (izpuščeno)
        # n = 3
        # x0 = np.linspace(1, 4, n)
        # y0 = np.around(1.7*np.cos(x0), decimals=2)
        # koordinate_za_interpolirat = [coord(x0[i], y0[i]) for i in range(n)]
        # new_points = np.array(koordinate_za_interpolirat)
        # new_points_labels = np.array(koordinate_za_interpolirat)
        # new_dots = self.get_dots(new_points[:, :2])
        # VGroup(new_dots).set_color(TEAL).shift(1.6*LEFT).scale(1.75)

        # 2 PRIKAZ TOČK
        self.setup_axes(animate=True)
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(1.7*np.cos(x0), decimals=2)
        koordinate_za_interpolirat = [coord(x0[i], y0[i]) for i in range(n)]
        new_points = np.array(koordinate_za_interpolirat)
        new_points_labels = np.array(koordinate_za_interpolirat)
        new_dots = self.get_dots(new_points[:, :2])
        VGroup(new_dots).set_color(TEAL).shift(1.6*LEFT).scale(1.75)
        dot0_label = TextMobject(r"$(x_0, y_0)$").set_color(TEAL)
        dot1_label = TextMobject(r"$(x_1, y_1)$").set_color(TEAL)
        dot2_label = TextMobject(r"$(x_2, y_2)$").set_color(TEAL)

        # 3 PRIKAZ IZRAČUNA TABELE VREDNOSTI
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(np.cos(x0), decimals=2)
        # izdelava številka
        string_print_x = " "
        string_print_y = " "
        for i in range(n):
            convert_string_x = np.array2string(np.around(x0[i], 2))
            convert_string_y = np.array2string(np.around(y0[i], 2))
            string_print_x += f"\quad{convert_string_x}\quad"
            string_print_y += f"{convert_string_y} \quad "
        tabx = TextMobject(string_print_x)
        taby = TexMobject(string_print_y)
        tab1 = VGroup(tabx, taby)
        tab1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        # tabela
        rectangle1 = Rectangle(height=0.8, width=5).shift(
            0.4*DOWN).set_color(WHITE)
        rectangle2 = Rectangle(height=0.8, width=5).shift(
            0.4*UP).set_color(WHITE)
        rectangle3 = Rectangle(height=1.6, width=1.6).shift(
            0.1*LEFT).set_color(WHITE)
        tab2 = VGroup(tab1, rectangle1, rectangle2, rectangle3)
        x0_label = TextMobject(f"$x_i$").shift(3*LEFT+0.4*UP).set_color(TEAL)
        y0_label = TextMobject(f"$y_i$").shift(3*LEFT+0.4*DOWN).set_color(TEAL)
        tab3 = VGroup(tab2, x0_label, y0_label)
        BlackCover = Rectangle(height=40, width=40,
                               fill_color=BLACK, fill_opacity=1)
        navodilo1 = TextMobject("Cilj metode je")
        navodilo2 = TextMobject("polinomska interpolacija").set_color(RED)
        navodilo3 = TextMobject("brez reševanja sistema enačb.")
        navodilo = VGroup(navodilo1, navodilo2, navodilo3)
        navodilo.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2*DOWN)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_lagrange\manim_lagrange.py ShowPoints -pl
        # 1
        # self.play(ShowCreation(func_graph1.scale(0.5).shift(5.485*LEFT)))
        # self.play(ShowCreation(func_graph2.scale(0.5)))
        # self.play(ShowCreation(func_graph3.scale(0.5).shift(5.485*RIGHT)))
        # self.play(Uncreate(func_graph1), Uncreate(func_graph3))
        # self.play(Transform(func_graph2, func_graph4))
        # self.setup_axes(animate=True, hideaxes=False)
        # self.play(ShowCreation(graph_lab))
        # self.wait(1)
        # self.play(Transform(func_graph2, new_dots), FadeOut(graph_lab))
        # self.wait(1)
        # 2
        self.play(
            Write(new_dots))
        self.play(
            Write(dot0_label.move_to(ORIGIN+2.25*UP+2.6*LEFT)),
            Write(dot1_label.move_to(ORIGIN+1.85*DOWN)),
            Write(dot2_label.move_to(ORIGIN+2.5*RIGHT+1.4*DOWN)),
        )
        self.wait(1)
        # 3
        self.play(Write(tab3.shift(UP*2.3+3*RIGHT)))
        self.add_foreground_mobjects(tab3)
        self.wait(1)
        self.play(FadeIn(BlackCover))
        self.play(ApplyMethod(tab3.move_to, ORIGIN+1*UP))
        self.play(ApplyMethod(tab3.scale, 1.6))
        self.play(Write(navodilo.scale(0.85)))
        self.wait(1)
        self.play(FadeOut(tab3))
        self.play(FadeOut(navodilo))
        self.wait(1)

    def func_to_graph(self, x):
        return np.cos(x)


class IzpeljavaLagranga(Scene):
    # python -m manim manim_lagrange\manim_lagrange.py IzpeljavaLagranga -pl

    def construct(self):  # IZDELAVA OBJEKTOV ###
        # 1 IZPELJAVA
        vrstica11 = TextMobject(
            "Lagrangev interpolacijski polinom").set_color(RED)
        vrstica12 = TextMobject("stopnje")
        vrstica13 = TextMobject(r"$n-1$").set_color(RED)
        vrstica14 = TextMobject("je definiran kot:")
        vrstica1 = VGroup(vrstica11, vrstica12, vrstica13, vrstica14)
        vrstica1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3*UP).scale(0.8)

        LagrangeIntPolinom = TextMobject(
            r"$L(x)= \sum_{i=0}^{n-1}$", r"$y_i$", r"$l_i(x)$", ",").shift(2*UP).scale(0.8)
        LagrangeIntPolinom.set_color_by_tex_to_color_map({
            "$L(x)= \sum_{i=0}^{n-1}$": RED,
            "$l_i(x)$": YELLOW,
            "$y_i$": TEAL
        })
        vrstica21 = TextMobject("kjer je")
        vrstica22 = TextMobject(r"$l_i$").set_color(YELLOW)
        vrstica23 = TextMobject("Lagrangeov polinom:").set_color(YELLOW)
        vrstica2 = VGroup(vrstica21, vrstica22, vrstica23)
        vrstica2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3.2*LEFT+1*UP).scale(0.8)
        LagrangePolinom1 = TextMobject(
            r"$ l_i(x) = \prod_{j=0, j \neq i}^{n-1} \frac{x-x_j}{x_i-x_j}$").shift(0*UP).scale(0.8).set_color(YELLOW)
        LagrangePolinom2 = TextMobject(
            r"$ l_i(x) = \frac{(x-x_0)}{(x_i-x_0)} \cdots \frac{(x-x_{i-1})}{(x_i-x_{i-1})} \frac{(x-x_{i+1})}{(x_i-x_{i+1})} \cdots \frac{(x-x_{n-1})}{(x_i-x_{n-1})}. $").scale(0.8).shift(1*DOWN).set_color(YELLOW)
        vrstica31 = TextMobject("Torej velja:").shift(2*DOWN+5*LEFT).scale(0.8)
        LagrangePolinom3 = TextMobject(
            r"$ l_i(x=x_i) = 1$").shift(3*DOWN+3*LEFT).scale(0.8).set_color(YELLOW)
        LagrangePolinom4 = TextMobject(
            r"$ l_i(x=x_k) = 0$", ", za ", r"$k \neq i$").shift(3*DOWN+2*RIGHT).scale(0.8)
        LagrangePolinom4.set_color_by_tex_to_color_map({
            "$ l_i(x=x_k) = 0$": YELLOW,
            ", za ": WHITE,
            "$k \neq i$": YELLOW
        })

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(vrstica1))
        self.play(Write(LagrangeIntPolinom))
        self.wait(1)
        self.play(Write(vrstica2))
        self.play(Write(LagrangePolinom1))
        self.wait(1)
        self.play(Write(LagrangePolinom2))
        self.wait(1)
        self.play(Write(vrstica31))
        self.play(Write(LagrangePolinom3))
        self.wait(1)
        self.play(Write(LagrangePolinom4))
        self.wait(4)


class IzracunPrimera(Scene):
    # python -m manim manim_lagrange\manim_lagrange.py IzracunPrimera -pl
    def construct(self):  # IZDELAVA OBJEKTOV ###
        # 1 TABELA VREDNOSTI
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(np.cos(x0), decimals=2)
        # izdelava številk
        string_print_x = []
        string_print_y = []
        for i in range(n):
            convert_string_x = np.array2string(np.around(x0[i], 2))
            convert_string_y = np.array2string(np.around(y0[i], 2))
            string_print_x.append(f"\quad{convert_string_x}\quad")
            string_print_y.append(f"{convert_string_y} \quad ")
        tabx = TextMobject(
            string_print_x[0],
            string_print_x[1],
            string_print_x[2]
        )
        tabx.set_color_by_tex_to_color_map({
            string_print_x[0]: ORANGE,
            string_print_x[1]: PINK,
            string_print_x[2]: GREEN
        })
        taby = TextMobject(
            string_print_y[0],
            string_print_y[1],
            string_print_y[2]
        )
        taby.set_color_by_tex_to_color_map({
            string_print_y[0]: ORANGE,
            string_print_y[1]: PINK,
            string_print_y[2]: GREEN
        })
        tab1 = VGroup(tabx, taby)
        tab1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        # tabela
        rectangle1 = Rectangle(height=0.8, width=5).shift(
            0.4*DOWN).set_color(WHITE)
        rectangle2 = Rectangle(height=0.8, width=5).shift(
            0.4*UP).set_color(WHITE)
        rectangle3 = Rectangle(height=1.6, width=1.6).shift(
            0.1*LEFT).set_color(WHITE)
        tab2 = VGroup(tab1, rectangle1, rectangle2, rectangle3)
        x0_label = TextMobject(f"$x_i$").shift(3*LEFT+0.4*UP).set_color(TEAL)
        y0_label = TextMobject(f"$y_i$").shift(3*LEFT+0.4*DOWN).set_color(TEAL)
        oznake = TextMobject(r"$i=0$", r"$\quad i=1$",
                             r"$\quad i=2$").shift(1.2*UP)
        oznake.set_color_by_tex_to_color_map({
            "$i=0$": ORANGE,
            "$\quad i=1$": PINK,
            "$\quad i=2$": GREEN
        })
        tab3 = VGroup(tab2, x0_label, y0_label, oznake)
        rectangle4 = Rectangle(height=1.23, width=1.3).shift(
            3.1*RIGHT+2.45*UP).set_color(YELLOW)

        # 2 IZRAČUN LAGRANGEVIH FUNKCIJ L0, L1 in L2
        vrstica11 = TextMobject("Za primer diskretnih točk")
        vrstica12 = TextMobject(r"$(x_i, y_i)$").set_color(TEAL)
        vrstica13 = TextMobject("zapišimo interpolacijski polinom")
        vrstica14 = TextMobject(r"$L(x).$").set_color(RED)
        vrstica1 = VGroup(vrstica11, vrstica12, vrstica13, vrstica14)
        vrstica1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(1*UP).scale(0.8)
        vrstica21 = TextMobject("V prvem koraku za poljuben")
        vrstica22 = TextMobject(r"$x$").set_color(TEAL)
        vrstica23 = TextMobject("izračunamo Lagrangeov polinom")
        vrstica24 = TextMobject(r"$l_i(x)$").set_color(YELLOW)
        vrstica25 = TextMobject(":")
        vrstica2 = VGroup(vrstica21, vrstica22,
                          vrstica23, vrstica24, vrstica25)
        vrstica2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(3*UP).scale(0.8)

        LagrangePolinom1 = TextMobject(
            r"$ = \prod_{j=0, j \neq i}^{n-1} \frac{x-x_j}{x_i-x_j}$").scale(0.8).shift(2.605*UP+4*LEFT).set_color(YELLOW)
        line = Line(np.array([0, 0, 0]), np.array(
            [4, 0, 0])).shift(2.1*UP+6.5*LEFT)
        ### Lagrangevi polinomi ###
        # prvi polinom #python -m manim manim_lagrange\manim_lagrange.py IzracunPrimera -pl
        eq_lg0 = TextMobject(r"$l$", r"$_0$", r"$(x)=$")
        eq_lg0.set_color_by_tex_to_color_map({"$_0$": ORANGE})
        eq01 = TexMobject("{\\prod^{2}", "_{j=0,", "j \\neq 0}", "{x-",
                          "x_j", "\\over", "x_0", "-", "x_j}").scale(0.7).shift(0.7*LEFT)
        eq01.set_color_by_tex_to_color_map(
            {"_{j=0,": TEAL, "j \\neq 0}": ORANGE, "x_j": TEAL, "x_j}": TEAL, "x_0": ORANGE})
        enacaj01 = TextMobject(r"$=$")
        eq02 = TexMobject(
            "\\Big( {x-", "x_0", "\\over", "x_0", "-", "x_0}", "\\Big)").scale(0.7)
        eq02.set_color_by_tex_to_color_map({"x_0": ORANGE, "x_0}": ORANGE})
        eq02_cancel = TextMobject(
            r"$\Big( \xcancel{\frac{x-x_0}{x_0-x_0}} \Big) $").set_color(RED)
        eq03 = TexMobject(
            "\\Big( {x-", "x_1", "\\over", "x_0", "-", "x_1}", "\\Big)").scale(0.7)
        eq03.set_color_by_tex_to_color_map({"x_0": ORANGE, "x_1": PINK})
        eq04 = TexMobject(
            "\\Big( {x-", "x_2", "\\over", "x_0", "-", "x_2}", "\\Big)").scale(0.7)
        eq04.set_color_by_tex_to_color_map({"x_0": ORANGE, "x_2": GREEN})
        enacaj02 = TextMobject(r"$=$")
        eq05 = TexMobject("\\Big( {x-", "2.5", "\\over", "1.", "-", "2.5}", "\\Big)",
                          "\\Big( {x-", "4.", "\\over", "1.", "-", "4.}", "\\Big) =").scale(0.7)
        eq05.set_color_by_tex_to_color_map(
            {"1.": ORANGE, "2.5": PINK, "4.": GREEN})
        eq06 = TextMobject(r"$\frac{2}{9} (x-4) (x-2.5) $")
        opomin0 = TexMobject("i", "=", "j").scale(0.7)
        opomin0.set_color_by_tex_to_color_map({"i": ORANGE, "j": ORANGE})

        # drugi polinom
        eq_lg1 = TextMobject(r"$l$", r"$_1$", r"$(x)=$")
        eq_lg1.set_color_by_tex_to_color_map({"$_1$": PINK})
        eq11 = TexMobject("{\\prod^{2}", "_{j=0,", "j \\neq 1}", "{x-",
                          "x_j", "\\over", "x_1", "-", "x_j}").scale(0.7).shift(0.7*LEFT)
        eq11.set_color_by_tex_to_color_map(
            {"_{j=0,": TEAL, "j \\neq 1}": PINK, "x_j": TEAL, "x_j}": TEAL, "x_1": PINK})
        enacaj11 = TextMobject(r"$=$")
        eq12 = TexMobject(
            "\\Big({x-", "x_0", "\\over", "x_1", "-", "x_0}", "\\Big)").scale(0.7)
        eq12.set_color_by_tex_to_color_map(
            {"x_1": PINK, "x_0": ORANGE, "x_0}": ORANGE})
        eq13 = TexMobject(
            "\\Big({x-", "x_1", "\\over", "x_1", "-", "x_1}", "\\Big)").scale(0.7)
        eq13.set_color_by_tex_to_color_map({"x_1": PINK, "x_1}": PINK})
        eq13_cancel = TextMobject(
            r"$\Big(\xcancel{\frac{x-x_1}{x_1-x_1}}\Big)$").set_color(RED)
        eq14 = TexMobject(
            "\\Big({x-", "x_2", "\\over", "x_1", "-", "x_2}", "\\Big)").scale(0.7)
        eq14.set_color_by_tex_to_color_map(
            {"x_2": GREEN, "x_1": PINK, "x_2}": GREEN})
        enacaj12 = TextMobject(r"$=$")
        eq15 = TexMobject("\\Big({x-", "1.", "\\over", "2.5", "-", "1.}", "\\Big)",
                          "\\Big({x-", "4.", "\\over", "2.5.", "-", "4.}", "\\Big)=").scale(0.7)
        eq15.set_color_by_tex_to_color_map(
            {"1.": ORANGE, "2.5": PINK, "4.": GREEN})
        eq16 = TextMobject(r"$-\frac{4}{9} (x-4) (x-1) $")
        opomin1 = TexMobject("i", "=", "j").scale(0.7)
        opomin1.set_color_by_tex_to_color_map({"i": PINK, "j": PINK})

        # tretji polinom
        eq_lg2 = TextMobject(r"$l$", r"$_2$", r"$(x)=$")
        eq_lg2.set_color_by_tex_to_color_map({"$_2$": GREEN})
        eq21 = TexMobject("{\\prod^{2}", "_{j=0,", "j \\neq 2}", "{x-",
                          "x_j", "\\over", "x_2", "-", "x_j}").scale(0.7).shift(0.7*LEFT)
        eq21.set_color_by_tex_to_color_map(
            {"_{j=0,": TEAL, "j \\neq 2}": GREEN, "x_j": TEAL, "x_j}": TEAL, "x_2": GREEN})
        enacaj21 = TextMobject(r"$=$")
        eq22 = TexMobject(
            "\\Big({x-", "x_0", "\\over", "x_2", "-", "x_0}", "\\Big)").scale(0.7)
        eq22.set_color_by_tex_to_color_map(
            {"x_2": GREEN, "x_0": ORANGE, "x_0}": ORANGE})
        eq23 = TexMobject(
            "\\Big({x-", "x_1", "\\over", "x_2", "-", "x_1}", "\\Big)").scale(0.7)
        eq23.set_color_by_tex_to_color_map(
            {"x_2": GREEN, "x_1": PINK, "x_1}": PINK})
        eq24 = TexMobject(
            "\\Big({x-", "x_2", "\\over", "x_2", "-", "x_2}", "\\Big)").scale(0.7)
        eq24.set_color_by_tex_to_color_map({"x_2": GREEN, "x_2}": GREEN})
        eq24_cancel = TextMobject(
            r"$\Big(\xcancel{\frac{x-x_2}{x_2-x_2}}\Big)$").set_color(RED)
        enacaj23 = TextMobject(r"$=$")
        enacaj22 = TextMobject(r"$=$")
        eq25 = TextMobject(r"$(\frac{x-1}{4-1})(\frac{x-2.5}{4-2.5})=$")
        eq26 = TextMobject(r"$\frac{2}{9} (x-1) (x-2.5) $")

        eq25 = TexMobject("\\Big({x-", "1.", "\\over", "4.", "-", "1.}", "\\Big)",
                          "\\Big({x-", "2.5", "\\over", "4.", "-", "2.5}", "\\Big)=").scale(0.7)
        eq25.set_color_by_tex_to_color_map(
            {"1.": ORANGE, "2.5": PINK, "4.": GREEN})
        opomin2 = TexMobject("i", "=", "j").scale(0.7)
        opomin2.set_color_by_tex_to_color_map({"i": GREEN, "j": GREEN})

        # ANIMIRANJE OBJEKTOV
        # python -m manim manim_lagrange\manim_lagrange.py IzracunPrimera -pl
        self.play(Write(vrstica1))
        self.wait(1)
        self.play(Transform(vrstica1, vrstica2))
        self.wait(4)
        self.play(FadeOut(vrstica1), ApplyMethod(vrstica24.move_to,
                                                 2.6*UP+6*LEFT), Write(tab3.shift(UP*2.4+4.5*RIGHT).scale(0.8)))
        self.play(Write(LagrangePolinom1))
        self.play(ShowCreation(line))
        self.play(Write(rectangle4))
        ## Lagrangeovi polinomi ##
        # Prvi polinom
        self.play(Write(eq_lg0.shift(5.6*LEFT+1*UP)))
        self.play(Write(eq01.shift(2.97*LEFT+1*UP)))
        self.wait(0.5)
        self.play(Write(enacaj01.move_to(eq01, RIGHT).shift(0.6*RIGHT)))
        self.play(Write(eq02.move_to(enacaj01, RIGHT).shift(1.7*RIGHT)))
        self.play(Write(opomin0.move_to(eq02, UP).shift(0.5*UP)))
        self.wait(1)
        self.play(Transform(eq02, eq02_cancel.move_to(eq02)), FadeOut(opomin0))
        self.play(FadeOut(eq02), Write(
            eq03.move_to(eq02, RIGHT).shift(1.7*RIGHT)))
        self.play(ApplyMethod(eq03.shift, 1.7*LEFT))
        self.play(Write(eq04.move_to(eq03, RIGHT).shift(1.7*RIGHT)))
        self.play(Write(enacaj02.move_to(eq01, DOWN).shift(0.8*DOWN+1.3*LEFT)))
        self.play(Write(eq05.move_to(enacaj02, RIGHT).shift(3.45*RIGHT)))
        self.play(Write(eq06.move_to(eq05, RIGHT).shift(3.8*RIGHT)))
        self.play(FadeOut(eq01), FadeOut(enacaj01), FadeOut(eq03),
                  FadeOut(eq04), FadeOut(enacaj02), FadeOut(eq05))
        self.play(ApplyMethod(eq06.shift, 1.26*UP+3.50*LEFT))
        self.play(ApplyMethod(eq_lg0.set_color, ORANGE),
                  ApplyMethod(eq06.set_color, ORANGE))

        # drugi polinom
        self.play(ApplyMethod(rectangle4.shift, 1.3*RIGHT))
        self.play(Write(eq_lg1.shift(5.6*LEFT)))
        self.play(Write(eq11.shift(2.97*LEFT)))
        self.wait(0.5)
        self.play(Write(enacaj11.move_to(eq11, RIGHT).shift(0.6*RIGHT)))
        self.play(Write(eq12.move_to(enacaj11, RIGHT).shift(1.8*RIGHT)))
        self.play(Write(eq13.move_to(eq12, RIGHT).shift(1.7*RIGHT)))
        self.play(Write(opomin1.move_to(eq13, UP).shift(0.5*UP)))
        self.wait(1)
        self.play(Transform(eq13, eq13_cancel.move_to(eq13)), FadeOut(opomin1))
        self.play(FadeOut(eq13), Write(
            eq14.move_to(eq13, RIGHT).shift(1.7*RIGHT)))
        self.play(ApplyMethod(eq14.shift, 1.7*LEFT))
        self.play(Write(enacaj12.move_to(eq11, DOWN).shift(0.8*DOWN+1.3*LEFT)))
        self.play(Write(eq15.move_to(enacaj12, RIGHT).shift(3.6*RIGHT)))
        self.play(Write(eq16.move_to(eq15, RIGHT).shift(3.8*RIGHT)))
        self.play(FadeOut(enacaj12), FadeOut(eq11), FadeOut(enacaj11),
                  FadeOut(eq12), FadeOut(eq14), FadeOut(eq15))
        self.play(ApplyMethod(eq16.shift, 1.26*UP+3.52*LEFT))
        self.play(ApplyMethod(eq_lg1.set_color, PINK),
                  ApplyMethod(eq16.set_color, PINK))

        # tretji polinom
        self.play(ApplyMethod(rectangle4.shift, 1.3*RIGHT))
        self.play(Write(eq_lg2.shift(5.6*LEFT+1*DOWN)))
        self.play(Write(eq21.shift(2.97*LEFT+1*DOWN)))
        self.wait(0.5)
        self.play(Write(enacaj21.move_to(eq21, RIGHT).shift(0.6*RIGHT)))
        self.play(Write(eq22.move_to(enacaj21, RIGHT).shift(1.8*RIGHT)))
        self.play(Write(eq23.move_to(eq22, RIGHT).shift(1.7*RIGHT)))
        self.play(Write(eq24.move_to(eq23, RIGHT).shift(1.7*RIGHT)))
        self.play(Write(opomin2.move_to(eq24, UP).shift(0.5*UP)))
        self.play(Transform(eq24, eq24_cancel.move_to(eq24)), FadeOut(opomin2))
        self.play(FadeOut(eq24), Write(
            enacaj23.move_to(eq23).shift(1.2*RIGHT)))
        # self.play(ApplyMethod(eq25.shift, 1.7*LEFT))
        self.play(Write(enacaj22.move_to(eq21, DOWN).shift(0.8*DOWN+1.3*LEFT)))
        self.play(Write(eq25.move_to(enacaj22, RIGHT).shift(3.6*RIGHT)))
        self.play(Write(eq26.move_to(eq25, RIGHT).shift(3.8*RIGHT)))
        self.play(FadeOut(enacaj22), FadeOut(enacaj23), FadeOut(enacaj21),
                  FadeOut(eq21),  FadeOut(eq22),  FadeOut(eq23),  FadeOut(eq25))
        self.play(ApplyMethod(eq26.shift, 1.26*UP+3.62*LEFT))
        self.play(ApplyMethod(eq_lg2.set_color, GREEN),
                  ApplyMethod(eq26.set_color, GREEN))
        self.wait(2)


class LagrangeFunk(GraphScene):
    # python -m manim manim_lagrange\manim_lagrange.py LagrangeFunk -pl
    CONFIG = {
        "x_min": -1.65,
        "x_max": 4.65,
        "x_axis_width": 11,
        "x_tick_frequency": 0.5,
        "x_leftmost_tick": -1,  # Change if different from x_min
        "y_min": -1,
        "y_max": 1,
        "y_tick_frequency": 0.5,
        "graph_origin": 3.5*LEFT,
        "axes_color": WHITE,
        "x_labeled_nums": range(-1, 5, 1),
        "y_labeled_nums": range(-2, 2, 1),
        "exclude_zero_label": True,
        "default_graph_colors": [ORANGE, PINK, GREEN],
    }

    def func_to_graph0(self, x):
        # f = np.cos(x)  # lahko spremenite v drugo funkcijo
        def lagrange(x, x_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            return Lx
        n = 3
        x_vhod = np.linspace(1, 4, n)
        f = lagrange(x, x_vhod, i=0)
        return f

    def func_to_graph1(self, x):
        # f = np.cos(x)  # lahko spremenite v drugo funkcijo
        def lagrange(x, x_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            return Lx
        n = 3
        x_vhod = np.linspace(1, 4, n)
        f = lagrange(x, x_vhod, i=1)
        return f

    def func_to_graph2(self, x):
        # f = np.cos(x)  # lahko spremenite v drugo funkcijo
        def lagrange(x, x_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            return Lx
        n = 3
        x_vhod = np.linspace(1, 4, n)
        f = lagrange(x, x_vhod, i=2)
        return f

    def construct(self):
        # TABELA VREDNOSTI
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(np.cos(x0), decimals=2)

        # tekst
        vrstica11 = TextMobject("Lagrangeve polinome ")
        vrstica12 = TextMobject(r"$l_i(x)$").set_color(YELLOW)
        vrstica13 = TextMobject("lahko izrišemo.")
        vrstica1 = VGroup(vrstica11, vrstica12, vrstica13)
        vrstica1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(2*UP+2*RIGHT).scale(0.75)

        vrstica21 = TextMobject("Vidimo, da je v pripadajočih točkah")
        vrstica22 = TextMobject(r"$x_i$").set_color(TEAL)
        vrstica23 = TextMobject("vrednost Lagrangevega polinoma")
        vrstica24 = TextMobject(r"$l_i(x)=1,$").set_color(YELLOW)
        vrstica25 = TextMobject("v nepripadajočih")
        vrstica26 = TextMobject(r"$x_k$").set_color(TEAL)
        vrstica27 = TextMobject(", kjer je")
        vrstica28 = TextMobject(r"$k \neq i $").set_color(TEAL)
        vrstica29 = TextMobject(" pa ")
        vrstica30 = TextMobject(r"$l_i(x)=0.$").set_color(YELLOW)
        vrstica2_1 = VGroup(vrstica21, vrstica22, vrstica23, vrstica24)
        vrstica2_1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/4).shift(1*DOWN).scale(0.75)
        vrstica2_2 = VGroup(vrstica25, vrstica26, vrstica27, vrstica28, vrstica29, vrstica30)
        vrstica2_2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/4).shift(2*DOWN).scale(0.75)

        # graf 1
        self.setup_axes(animate=True)

        func_graph0 = self.get_graph(self.func_to_graph0)
        graph_lab0 = self.get_graph_label(func_graph0, label=f"l_0(x)")
        label_coord0 = self.input_to_graph_point(TAU, func_graph0)
        vert_line0 = self.get_vertical_line_to_graph(
            x0[0], func_graph0, color=TEAL)
        horiz_line0 = self.get_horizontal_line_to_graph(
            1, func_graph0, color=TEAL)

        func_graph1 = self.get_graph(self.func_to_graph1)
        graph_lab1 = self.get_graph_label(func_graph1, label=f"l_1(x)")
        label_coord1 = self.input_to_graph_point(TAU, func_graph1)
        vert_line1 = self.get_vertical_line_to_graph(
            x0[1], func_graph1, color=TEAL)
        horiz_line1 = self.get_horizontal_line_to_graph(
            x0[1], func_graph1, color=TEAL)

        func_graph2 = self.get_graph(self.func_to_graph2)
        graph_lab2 = self.get_graph_label(func_graph2, label=f"l_2(x)")
        label_coord2 = self.input_to_graph_point(TAU, func_graph2)
        vert_line2 = self.get_vertical_line_to_graph(
            x0[2], func_graph2, color=TEAL)
        horiz_line2 = self.get_horizontal_line_to_graph(
            x0[2], func_graph2, color=TEAL)

        # python -m manim manim_lagrange\manim_lagrange.py LagrangeFunk -pl
        self.play(Write(vrstica1))
        self.wait(1.0)
        self.play(FadeOut(vrstica1))
        self.play(ShowCreation(func_graph0))
        self.play(ShowCreation(vert_line0), ShowCreation(
            horiz_line0), ShowCreation(graph_lab0))
        self.wait(1)
        self.play(FadeOut(func_graph0), FadeOut(vert_line0),
                  FadeOut(horiz_line0), FadeOut(graph_lab0))
        self.play(ShowCreation(func_graph1))
        self.play(ShowCreation(vert_line1), ShowCreation(
            horiz_line1), ShowCreation(graph_lab1))
        self.wait(1)
        self.play(FadeOut(func_graph1), FadeOut(vert_line1),
                  FadeOut(horiz_line1), FadeOut(graph_lab1))
        self.play(ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line2), ShowCreation(
            horiz_line2), ShowCreation(graph_lab2))
        self.play(Write(vrstica2_1.shift(1*DOWN)))
        self.play(Write(vrstica2_2.shift(0.5*DOWN + 2.83*LEFT)))
        self.wait(2)


class IzracunPolinoma(Scene):
    # python -m manim manim_lagrange\manim_lagrange.py IzracunPolinoma -pl
    def construct(self):

        # TABELA VREDNOSTI
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(np.cos(x0), decimals=2)
        # izdelava številka
        string_print_x = " "
        string_print_y = " "
        for i in range(n):
            convert_string_x = np.array2string(np.around(x0[i], 2))
            convert_string_y = np.array2string(np.around(y0[i], 2))
            string_print_x += f"\quad{convert_string_x}\quad"
            string_print_y += f"{convert_string_y} \quad "
        tabx = TextMobject(string_print_x)
        taby = TexMobject(string_print_y)
        tab1 = VGroup(tabx, taby)
        tab1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        # tabela
        rectangle1 = Rectangle(height=0.8, width=5).shift(
            0.4*DOWN).set_color(RED)
        rectangle2 = Rectangle(height=0.8, width=5).shift(
            0.4*UP).set_color(RED)
        rectangle3 = Rectangle(height=1.6, width=1.6).shift(
            0.1*LEFT).set_color(RED)
        tab2 = VGroup(tab1, rectangle1, rectangle2, rectangle3)
        x0_label = TextMobject(f"$x_i$").shift(3*LEFT+0.4*UP).set_color(TEAL)
        y0_label = TextMobject(f"$y_i$").shift(3*LEFT+0.4*DOWN).set_color(TEAL)
        oznake = TextMobject(r"$i=0 \quad i=1 \quad i=2$").shift(1.2*UP)
        tab3 = VGroup(tab2, x0_label, y0_label, oznake)
        rectangle4 = Rectangle(height=1.23, width=1.3).shift(
            3.1*RIGHT+2.45*UP).set_color(YELLOW)

        # 1 IZRAČUN LAGRANGEVIH FUNKCIJ L0, L1 in L2
        vrstica11 = TextMobject("Za primer diskretnih točk")
        vrstica12 = TextMobject(r"$(x_0, y_0)$").set_color(TEAL)
        vrstica13 = TextMobject("zapišimo interpolacijski polinom")
        vrstica14 = TextMobject(r"$L(x).$").set_color(RED)
        vrstica1 = VGroup(vrstica11, vrstica12, vrstica13, vrstica14)
        vrstica1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF).shift(1*UP).scale(0.8)
        vrstica21 = TextMobject("V prvem koraku za vsak")
        vrstica22 = TextMobject(r"$x_0$").set_color(TEAL)
        vrstica23 = TextMobject("izračunamo Lagrangeov polinom")
        vrstica24 = TextMobject(r"$l_i(x)$").set_color(RED)
        vrstica25 = TextMobject(":").set_color(RED)
        vrstica2 = VGroup(vrstica21, vrstica22,
                          vrstica23, vrstica24, vrstica25)
        vrstica2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF).shift(3*UP).scale(0.8)

        LagrangePolinom1 = TextMobject(
            r"$ = \prod_{j=0, j \neq i}^{n-1} \frac{x-x_j}{x_i-x_j}$").scale(0.8).shift(2.605*UP+4*LEFT).set_color(RED)
        line = Line(np.array([0, 0, 0]), np.array(
            [4, 0, 0])).shift(2.1*UP+6.5*LEFT)
        ### Lagrangevi polinomi ###
        # prvi polinom
        eq_lg0 = TextMobject(r"$l_0(x)=$")
        eq01 = TextMobject(
            r"$\prod_{j=0, j \neq 0}^{2} \frac{x-x_j}{x_0-x_j}$")
        enacaj01 = TextMobject(r"$=$")
        eq02 = TextMobject(r"$(\frac{x-x_0}{x_0-x_0})$")
        eq02_cancel = TextMobject(r"$(\cancel{\frac{x-x_0}{x_0-x_0}})$")
        eq03 = TextMobject(r"$(\frac{x-x_1}{x_0-x_1})$")
        eq04 = TextMobject(r"$(\frac{x-x_2}{x_0-x_2})$")
        enacaj02 = TextMobject(r"$=$")
        eq05 = TextMobject(
            r"$(\frac{x-2.5}{1.0-2.5})(\frac{x-4.0}{1.0-4.0})=$")
        eq06 = TextMobject(r"$\frac{2}{9} (x-4) (x-2.5) $")

        # drugi polinom
        eq_lg1 = TextMobject(r"$l_1(x)=$")
        eq11 = TextMobject(
            r"$\prod_{j=0, j \neq 0}^{2} \frac{x-x_j}{x_1-x_j}$")
        enacaj11 = TextMobject(r"$=$")
        eq12 = TextMobject(r"$(\frac{x-x_0}{x_1-x_0})$")
        eq13 = TextMobject(r"$(\frac{x-x_1}{x_1-x_1})$")
        eq13_cancel = TextMobject(r"$(\cancel{\frac{x-x_1}{x_1-x_1}})$")
        eq14 = TextMobject(r"$(\frac{x-x_2}{x_1-x_2})$")
        enacaj12 = TextMobject(r"$=$")
        eq15 = TextMobject(r"$(\frac{x-1}{2.5-1})(\frac{x-4}{2.5-4})=$")
        eq16 = TextMobject(r"$-\frac{4}{9} (x-4) (x-1) $")

        # tretji polinom
        eq_lg2 = TextMobject(r"$l_2(x)=$")
        eq21 = TextMobject(
            r"$\prod_{j=0, j \neq 0}^{2} \frac{x-x_j}{x_2-x_j}$")
        enacaj21 = TextMobject(r"$=$")
        eq22 = TextMobject(r"$(\frac{x-x_0}{x_2-x_0})$")
        eq23 = TextMobject(r"$(\frac{x-x_1}{x_2-x_1})$")
        eq24 = TextMobject(r"$(\frac{x-x_2}{x_2-x_2})$")
        eq24_cancel = TextMobject(r"$(\cancel{\frac{x-x_2}{x_2-x_2}})$")
        enacaj23 = TextMobject(r"$=$")
        enacaj22 = TextMobject(r"$=$")
        eq25 = TextMobject(r"$(\frac{x-1}{4-1})(\frac{x-2.5}{4-2.5})=$")
        eq26 = TextMobject(r"$\frac{2}{9} (x-1) (x-2.5) $")

        ## 2 LAGRANGEV INTERPOLACIJSKI POLINOM ##
        vrstica31 = TextMobject("Če sedaj")
        vrstica32 = TextMobject(r"$i$-ti").set_color(YELLOW)
        vrstica33 = TextMobject("lagrangev polinom pomnožimo s pripadajočim")
        vrstica34 = TextMobject(r"$y_i$").set_color(TEAL)
        vrstica35 = TextMobject("in seštejemo, dobimo")
        vrstica36 = TextMobject(
            "Lagrangev interpolacijski polinom.").set_color(RED)
        vrstica3_1 = VGroup(vrstica31, vrstica32, vrstica33, vrstica34)
        vrstica3_2 = VGroup(vrstica35, vrstica36)
        vrstica3_1.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(1*UP).scale(0.8)
        vrstica3_2.arrange_submobjects(
            RIGHT, buff=MED_LARGE_BUFF/2).shift(1*UP).scale(0.8)

        # prva vrstica
        LagrangeIntPolinom = TextMobject(
            r"$L(x) = \sum_{i=0}^{n-1}$", r"$ y_i$", r"$l_i(x)$", r"$=$")
        LagrangeIntPolinom.set_color_by_tex_to_color_map(
            {"$L(x) = \sum_{i=0}^{n-1}$": RED, "$ y_i$": TEAL, "$l_i(x)$": YELLOW, "$=$": RED})
        y_0 = TextMobject(r"$y_0$").set_color(TEAL)
        l_0 = TextMobject(r"$l_0(x)$").set_color(ORANGE)
        plus1 = TextMobject(r"$+$")
        y_1 = TextMobject(r"$y_1$").set_color(TEAL)
        l_1 = TextMobject(r"$l_1(x)$").set_color(PINK)
        plus2 = TextMobject(r"$+$")
        y_2 = TextMobject(r"$y_2$").set_color(TEAL)
        l_2 = TextMobject(r"$l_2(x)$").set_color(GREEN)
        p1 = VGroup(y_0, l_0, plus1, y_1, l_1, plus2, y_2, l_2)
        p1.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF/4)
        oklepaji = TextMobject(
            r"$(\quad \quad \quad\quad \quad \quad\quad\quad)$").set_color(PINK)
        enacaj31 = TextMobject(r"$=$")
        enacaj32 = TextMobject(r"$L(x)=$").set_color(RED)

        y00 = TextMobject(f"{y0[0]}").set_color(TEAL)
        y01 = TextMobject(f"{y0[1]}").set_color(TEAL)
        y02 = TextMobject(f"{y0[2]}").set_color(TEAL)

        resitev = TextMobject(r"$ 0.33 x^2 -2.05 x + 2.26 $").set_color(RED)

        resitev_tekst = TextMobject(
            "Lagrangev integracijski polinom postopoma grafično sestavimo.").scale(0.8)

        ### ANIMIRANJE OBJEKTOV ###
        # python -m manim manim_lagrange\manim_lagrange.py IzracunPolinoma -pl

        self.play(
            FadeIn(eq_lg0.shift(1*DOWN+5.5*LEFT).set_color(ORANGE)
                   ), FadeIn(eq06.shift(1*DOWN+2.6*LEFT).set_color(ORANGE)),
            FadeIn(eq_lg1.shift(2*DOWN+5.5*LEFT).set_color(PINK)
                   ), FadeIn(eq16.shift(2*DOWN+2.6*LEFT).set_color(PINK)),
            FadeIn(eq_lg2.shift(3*DOWN+5.5*LEFT).set_color(GREEN)
                   ), FadeIn(eq26.shift(3*DOWN+2.6*LEFT).set_color(GREEN)),
            Write(vrstica3_1.shift(0.5*UP))
        )
        self.play(Write(vrstica3_2.shift(0.5*DOWN)))
        self.wait(2)
        self.play(FadeOut(vrstica3_1), FadeOut(vrstica3_2))
        self.play(Write(LagrangeIntPolinom.shift(3*UP)))
        self.play(Write(p1.shift(2*UP)))
        self.wait(1)

        self.play(
            ApplyMethod(y_0.shift, DOWN+2.8*LEFT),
            ApplyMethod(eq06.shift, 2*UP+0.6*LEFT),
            FadeOut(eq_lg0),
            FadeOut(l_0)
        )

        self.play(
            ApplyMethod(plus1.shift, DOWN),
            ApplyMethod(y_1.shift, DOWN),
            ApplyMethod(eq16.shift, 3*UP+4.55*RIGHT),
            Write(oklepaji.shift(UP+2.0*RIGHT)),
            FadeOut(eq_lg1),
            FadeOut(l_1)
        )

        self.play(
            ApplyMethod(plus2.shift, 2*DOWN+4*LEFT),
            ApplyMethod(y_2.shift, 2*DOWN+4*LEFT),
            ApplyMethod(eq26.shift, 3*UP+2.4*RIGHT),
            FadeOut(eq_lg2),
            FadeOut(l_2)
        )

        self.play(
            ReplacementTransform(y_0, y00.next_to(y_0).shift(1.1*LEFT)),
            ReplacementTransform(y_1, y01.next_to(y_1).shift(0.5*LEFT)),
            ReplacementTransform(y_2, y02.next_to(y_2).shift(0.7*LEFT)),
            ApplyMethod(eq16.shift, 0.5*RIGHT),
            ApplyMethod(oklepaji.shift, 0.5*RIGHT),
            ApplyMethod(eq26.shift, 0.5*RIGHT),
        )
        self.play(
            Write(enacaj31.next_to(eq26, RIGHT)),
            Write(enacaj32.shift(2.7*LEFT+1*DOWN))
        )
        self.play(Write(resitev.next_to(enacaj32, RIGHT)))
        self.play(Write(resitev_tekst.shift(2*DOWN)))
        self.wait(3)


class IzrisPolinoma(PathScene):
    # python -m manim manim_lagrange\manim_lagrange.py IzrisPolinoma -pl
    # 1 IZRIS POLINOMA v kosih
    # 0
    def lagrange_0(self, x):
        def lagrange(x, x_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            return Lx
        n = 3
        x_vhod = np.linspace(1, 4, n)
        f = lagrange(x, x_vhod, i=0)
        return f

    def polinom_0(self, x):
        def lagrange_interpolacija(x, x_int, y_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            y=y_int[i]*Lx
            return y
        n = 3
        i = 0
        x_vhod = np.linspace(1, 4, n)
        y_vhod = np.cos(x_vhod)
        f = lagrange_interpolacija(x, x_vhod, y_vhod , i)
        return f
    # 1

    def lagrange_1(self, x):
        def lagrange(x, x_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            return Lx
        n = 3
        x_vhod = np.linspace(1, 4, n)
        f = lagrange(x, x_vhod, i=1)
        return f

    def polinom_1(self, x):
        def lagrange_interpolacija(x, x_int, y_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            y=y_int[i]*Lx
            return y
        n = 3
        i = 1
        x_vhod = np.linspace(1, 4, n)
        y_vhod = np.cos(x_vhod)
        f = lagrange_interpolacija(x, x_vhod, y_vhod , i)
        return f
    # 2

    def lagrange_2(self, x):
        def lagrange(x, x_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            return Lx
        n = 3
        x_vhod = np.linspace(1, 4, n)
        f = lagrange(x, x_vhod, i=2)
        return f

    def polinom_2(self, x):
        def lagrange_interpolacija(x, x_int, y_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            y=y_int[i]*Lx
            return y
        n = 3
        i = 2
        x_vhod = np.linspace(1, 4, n)
        y_vhod = np.cos(x_vhod)
        f = lagrange_interpolacija(x, x_vhod, y_vhod , i)
        return f

    # 01

    def polinom_01(self, x):
        def lagrange_interpolacija(x, x_int, y_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            y=y_int[i]*Lx
            return y
        n = 3
        x_vhod = np.linspace(1, 4, n)
        y_vhod = np.cos(x_vhod)
        f0 = lagrange_interpolacija(x, x_vhod, y_vhod, i=0)
        f1 = lagrange_interpolacija(x, x_vhod, y_vhod, i=1)
        f = f0 + f1
        return f

    # koncni
    def koncni_polinom(self, x):
        def lagrange_interpolacija(x, x_int, y_int, i):
            Lx = 1.0
            for j in range(len(x_int)):
                if j != i:
                    Lx *= (x-x_int[j]) / (x_int[i]-x_int[j])
            y=y_int[i]*Lx
            return y
        n = 3
        x_vhod = np.linspace(1, 4, n)
        y_vhod = np.cos(x_vhod)
        f0 = lagrange_interpolacija(x, x_vhod, y_vhod, i=0)
        f1 = lagrange_interpolacija(x, x_vhod, y_vhod, i=1)
        f2 = lagrange_interpolacija(x, x_vhod, y_vhod, i=2)
        f = f0 + f1 + f2
        return f

    def construct(self):  # KREIRANJE OBJEKTOV ###
        # 1 PRIKAZ TOČK
        self.setup_axes(animate=True)
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(1.7*np.cos(x0), decimals=2)
        koordinate_za_interpolirat = [coord(x0[i], y0[i]) for i in range(n)]
        new_points = np.array(koordinate_za_interpolirat)
        new_points_labels = np.array(koordinate_za_interpolirat)
        new_dots = self.get_dots(new_points[:, :2])
        VGroup(new_dots).set_color(TEAL).shift(1.62*LEFT+0.2*DOWN).scale(1.75)
        dot0_label = TextMobject(r"$(x_0, y_0)$").set_color(ORANGE)
        dot1_label = TextMobject(r"$(x_1, y_1)$").set_color(PINK)
        dot2_label = TextMobject(r"$(x_2, y_2)$").set_color(GREEN)

        # 2 GRAF
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(np.cos(x0), decimals=2)
        # Lagrange v int. polinom 0
        lagrange_0_graf = self.get_graph(self.lagrange_0, self.function_color)
        lagrange_0_lab = self.get_graph_label(lagrange_0_graf, label=f"l_0(x)")
        lagrange_0_coord = self.input_to_graph_point(TAU, lagrange_0_graf)
        polinom_0_graf = self.get_graph(self.polinom_0, self.function_color)
        polinom_0_lab = self.get_graph_label(polinom_0_graf, label=f"L_0(x)")
        polinom_0_coord = self.input_to_graph_point(TAU, polinom_0_graf)

        # lagrange 1 v polinom 1
        lagrange_1_graf = self.get_graph(self.lagrange_1, self.function_color)
        lagrange_1_lab = self.get_graph_label(lagrange_1_graf, label=f"l_0(x)")
        lagrange_1_coord = self.input_to_graph_point(TAU, lagrange_1_graf)
        polinom_1_graf = self.get_graph(self.polinom_1, self.function_color)
        polinom_1_lab = self.get_graph_label(polinom_1_graf, label=f"L_1(x)")
        polinom_1_coord = self.input_to_graph_point(TAU, polinom_1_graf)

        # lagrange 2 v polinom 2
        lagrange_2_graf = self.get_graph(self.lagrange_2, self.function_color)
        lagrange_2_lab = self.get_graph_label(
            lagrange_2_graf, label=f"l_0(x)").shift(0.2*UP)
        lagrange_2_coord = self.input_to_graph_point(TAU, lagrange_2_graf)
        polinom_2_graf = self.get_graph(self.polinom_2, self.function_color)
        polinom_2_lab = self.get_graph_label(
            polinom_2_graf, label=f"L_1(x)")
        polinom_2_coord = self.input_to_graph_point(TAU, polinom_2_graf)

        # polinom 0 in polinom 1 skupaj
        polinom_01_graf = self.get_graph(self.polinom_01, self.function_color)
        polinom_01_lab = self.get_graph_label(
            polinom_01_graf, label=f"L_1(x)+L_2(x)").shift(0.5*UP)
        polinom_01_coord = self.input_to_graph_point(TAU, polinom_01_graf)

        # koncni polinom
        koncni_polinom_graf = self.get_graph(
            self.koncni_polinom, self.function_color)
        koncni_polinom_lab = self.get_graph_label(
            koncni_polinom_graf, label=f"L(x)=L_1(x)+L_2(x)+L_3(x)").shift(1.2*UP+0.5*LEFT)
        koncni_polinom_coord = self.input_to_graph_point(
            TAU, koncni_polinom_graf)

        # 3 ENAČBA
        # python -m manim manim_lagrange\manim_lagrange.py IzrisPolinoma -pl
        LagrangeIntPolinom = TextMobject(
            r"$L(x) = \sum_{i=0}^{n-1}$", r"$ y_i$", r"$l_i(x)$")
        LagrangeIntPolinom.set_color_by_tex_to_color_map(
            {"$L(x) = \sum_{i=0}^{n-1}$": RED, "$ y_i$": TEAL, "$l_i(x)$": YELLOW})
        LagrangeZnak = TextMobject(
            r"$L(x) = $").set_color(RED)
        y_0 = TextMobject(r"$y_0$").set_color(ORANGE)
        l_0 = TextMobject(r"$l_0(x)$").set_color(ORANGE)
        plus1 = TextMobject(r"$+$").set_color(RED)
        y_1 = TextMobject(r"$y_1$").set_color(PINK)
        l_1 = TextMobject(r"$l_1(x)$").set_color(PINK)
        plus2 = TextMobject(r"$+$").set_color(RED)
        y_2 = TextMobject(r"$y_2$").set_color(GREEN)
        l_2 = TextMobject(r"$l_2(x)$").set_color(GREEN)
        p1 = VGroup(y_0, l_0, plus1, y_1, l_1, plus2, y_2, l_2)
        p1.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF/4)
        oklepaji = TextMobject(
            r"$(\quad \quad \quad\quad \quad \quad\quad\quad)$").set_color(PINK)
        enacaj31 = TextMobject(r"$=$")
        enacaj32 = TextMobject(r"$L(x)=$").set_color(RED)

        y00 = TextMobject(f"{y0[0]}").set_color(TEAL)
        y01 = TextMobject(f"{y0[1]}").set_color(TEAL)
        y02 = TextMobject(f"{y0[2]}").set_color(TEAL)

        resitev1 = TextMobject(r"$ 0.48 x^2 -2.56 x + 2.62 $").set_color(RED)
        resitev2 = TextMobject(r"$ 0.33 x^2 -2.05 x + 2.26 $").set_color(RED)

        # 4 TABELA VREDNOSTI
        n = 3
        x0 = np.linspace(1, 4, n)
        y0 = np.around(np.cos(x0), decimals=2)
        # izdelava številk
        string_print_x = []
        string_print_y = []
        for i in range(n):
            convert_string_x = np.array2string(np.around(x0[i], 2))
            convert_string_y = np.array2string(np.around(y0[i], 2))
            string_print_x.append(f"\quad{convert_string_x}\quad")
            string_print_y.append(f"{convert_string_y} \quad ")
        tabx = TextMobject(
            string_print_x[0],
            string_print_x[1],
            string_print_x[2]
        )
        tabx.set_color_by_tex_to_color_map({
            string_print_x[0]: ORANGE,
            string_print_x[1]: PINK,
            string_print_x[2]: GREEN
        })
        taby = TextMobject(
            string_print_y[0],
            string_print_y[1],
            string_print_y[2]
        )
        taby.set_color_by_tex_to_color_map({
            string_print_y[0]: ORANGE,
            string_print_y[1]: PINK,
            string_print_y[2]: GREEN
        })
        tab1 = VGroup(tabx, taby)
        tab1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        # tabela
        rectangle1 = Rectangle(height=0.8, width=5).shift(
            0.4*DOWN).set_color(WHITE)
        rectangle2 = Rectangle(height=0.8, width=5).shift(
            0.4*UP).set_color(WHITE)
        rectangle3 = Rectangle(height=1.6, width=1.6).shift(
            0.1*LEFT).set_color(WHITE)
        tab2 = VGroup(tab1, rectangle1, rectangle2, rectangle3)
        x0_label = TextMobject(f"$x_i$").shift(3*LEFT+0.4*UP).set_color(TEAL)
        y0_label = TextMobject(f"$y_i$").shift(3*LEFT+0.4*DOWN).set_color(TEAL)
        oznake = TextMobject(r"$i=0$", r"$\quad i=1$",
                             r"$\quad i=2$").shift(1.2*UP)
        oznake.set_color_by_tex_to_color_map({
            "$i=0$": ORANGE,
            "$\quad i=1$": PINK,
            "$\quad i=2$": GREEN
        })
        tab3 = VGroup(tab2, x0_label, y0_label, oznake)
        rectangle4 = Rectangle(height=1.23, width=1.3).shift(
            3.1*RIGHT+2.45*UP).set_color(YELLOW)

        ## ANIMIRANJE ##
        # python -m manim manim_lagrange\manim_lagrange.py IzrisPolinoma -pl

        # TOČKE
        self.play(Write(new_dots))
        self.play(
            Write(dot0_label.move_to(ORIGIN+2.25*UP+2.6*LEFT)),
            Write(dot1_label.move_to(ORIGIN+1.85*DOWN)),
            Write(dot2_label.move_to(ORIGIN+2.5*RIGHT+1.4*DOWN)),
        )
        self.wait(1)
        self.play(
            FadeOut(dot0_label),
            FadeOut(dot1_label),
            FadeOut(dot2_label),
            Write(LagrangeIntPolinom.shift(3.5*DOWN+5*LEFT).scale(0.8))
        )
        self.wait(1)

        # GRAF
        # lagrange 0 v polinom 0
        self.play(
            ShowCreation(lagrange_0_graf.set_color(ORANGE)),
            ShowCreation(lagrange_0_lab.set_color(ORANGE)),
            Transform(LagrangeIntPolinom, LagrangeZnak.shift(
                3.53*DOWN+6.13*LEFT).scale(0.8)),
            Write(l_0.next_to(LagrangeZnak, RIGHT).scale(0.8).shift(0.2*LEFT))
        )
        self.wait(1)
        self.play(
            Transform(lagrange_0_graf, polinom_0_graf.set_color(ORANGE)),
            Transform(lagrange_0_lab, polinom_0_lab.set_color(ORANGE)),
            Write(y_0.next_to(l_0, RIGHT).scale(0.8).shift(0.2*LEFT))
        )
        self.wait(1)
        # lagrange 1 v polinom 1
        self.play(
            ShowCreation(lagrange_1_graf.set_color(PINK)),
            ShowCreation(lagrange_1_lab.set_color(PINK)),
            Write(l_1.next_to(y_0, RIGHT).scale(0.8).shift(0.4*RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(lagrange_1_graf, polinom_1_graf.set_color(PINK)),
            Transform(lagrange_1_lab, polinom_1_lab.set_color(PINK)),
            Write(y_1.next_to(l_1, RIGHT).scale(0.8).shift(0.2*LEFT))
        )
        self.wait(1)
        # lagrange 2 v polinom 2
        self.play(
            ShowCreation(lagrange_2_graf.set_color(GREEN)),
            ShowCreation(lagrange_2_lab.set_color(GREEN)),
            Write(l_2.next_to(y_1, RIGHT).scale(0.8).shift(0.4*RIGHT))
        )
        self.wait(1)
        self.play(
            Transform(lagrange_2_graf, polinom_2_graf.set_color(GREEN)),
            Transform(lagrange_2_lab, polinom_2_lab.set_color(GREEN)),
            Write(y_2.next_to(l_2, RIGHT).scale(0.8).shift(0.2*LEFT))
        )
        self.wait(1)
        self.wait(2)
        self.play(Write(plus1.next_to(y_0, RIGHT).scale(0.8)))
        # polinom 0 + polinom 1
        self.play(
            Transform(lagrange_0_graf, polinom_01_graf.set_color(RED)),
            Transform(lagrange_1_graf, polinom_01_graf.set_color(RED)),
            Transform(lagrange_0_lab, polinom_01_lab.set_color(RED)),
            Transform(lagrange_1_lab, polinom_01_lab.set_color(RED)),
            Transform(y_0, resitev1.set_color(RED).scale(
                0.8).next_to(LagrangeZnak, RIGHT).shift(0.1*LEFT)),
            Transform(l_0, resitev1),
            Transform(plus1, resitev1),
            Transform(y_1, resitev1),
            Transform(l_1, resitev1),
            Write(plus2.next_to(y_1, 3*RIGHT).scale(0.8)),
            ApplyMethod(l_2.shift, 0.5*RIGHT),
            ApplyMethod(y_2.shift, 0.5*RIGHT)
        )
        self.wait(2)

        # končni polinom
        self.play(
            Transform(lagrange_0_graf, koncni_polinom_graf),
            Transform(lagrange_1_graf, koncni_polinom_graf),
            Transform(lagrange_2_graf, koncni_polinom_graf),
            Transform(lagrange_0_lab, koncni_polinom_lab),
            Transform(lagrange_1_lab, koncni_polinom_lab),
            Transform(lagrange_2_lab, koncni_polinom_lab),
            Transform(y_0, resitev2.set_color(RED).scale(
                0.8).next_to(LagrangeZnak, RIGHT).shift(0.1*LEFT)),
            Transform(l_0, resitev2),
            Transform(plus1, resitev2),
            Transform(y_1, resitev2),
            Transform(l_1, resitev2),
            Transform(plus2, resitev2),
            Transform(l_2, resitev2),
            Transform(y_2, resitev2),
        )
        self.wait(1)

        self.play(Write(tab3.scale(0.8).shift(2.5*UP+4*RIGHT)))
        self.wait(14)

class Credits(Scene):
    # python -m manim manim_lagrange\manim_lagrange.py Credits -pl

    def construct(self):  # KONSTRUKCIJA VSEH OBJEKTOV ##
        # 1 NASLOV
        naslov = TextMobject(
            "Interpolacija z Lagrangevo metodo").set_color(YELLOW).scale(1.1).shift(3*UP+2*LEFT)

        # 2 GLAsBA
        glasba = TextMobject("Glasba: https://www.bensound.com/").scale(0.8).set_color(RED)

        # 2 MAnim
        Manim1 = TextMobject("Narejeno z MAnim").scale(0.8).set_color(TEAL)
        Manim2 = TextMobject("https://github.com/3b1b/manim").scale(0.8).set_color(TEAL)

        ### ANIMIRANJE OBJEKTOV ###
        self.play(Write(naslov))
        self.play(
            Write(Manim1.shift(5.05*LEFT+2*DOWN)),
            Write(Manim2.shift(3.8*LEFT+2.5*DOWN))
            )
        self.play(Write(glasba.shift(3.4*LEFT+3.5*DOWN)))
        self.wait(5)
