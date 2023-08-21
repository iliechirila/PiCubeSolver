from Common.Cube import Cube
from Solvers.CrossSolver import CrossSolver
from Solvers.F2LSolver import F2LSolver
from Solvers.OLLSolver import OLLSolver
from Solvers.PLLSolver import PLLSolver

class Solver:
    def __init__(self):
        self.cube = Cube()

    def update_cube_dict(self, cube_dict: dict):
        self.cube.cube_dict = cube_dict

    def update_cube_dict_from_colors_list(self, lst: list):
        new_cube_dict = self.cube.process_string_list(lst)
        self.update_cube_dict(new_cube_dict)

    def solve_cube(self):
        alg_cross = self.solve_cross()
        alg_f2l = self.solve_f2l()
        alg_oll = self.solve_oll()
        alg_pll = self.solve_pll()

        # CORNER CASES WHEN THERE IS AN OLL SKIP
        if alg_oll:
            alg_oll = self.cube.format_alg_to_turns(alg_oll)
        else:
            alg_oll = []

        if alg_pll:
            alg_pll = self.cube.format_alg_to_turns(alg_pll)
        else:
            alg_pll = []
        #######################
        # DEBUGGING
        #######################
        # self.cube.graph_cube()
        return self.give_solution_formatted(alg_cross, alg_f2l, alg_oll, alg_pll)


    def solve_cross(self):
        cs = CrossSolver(self.cube.cube_dict)
        alg = cs.alg
        self.cube.apply_alg_tuple(alg)
        return alg

    def solve_f2l(self):
        f2l = F2LSolver(self.cube.cube_dict)
        f2l_algs = f2l.alg_overall
        f2l_algs_one_list = []
        for alg in f2l_algs:
            self.cube.apply_alg_tuple(alg)
            f2l_algs_one_list = f2l_algs_one_list + alg
        return f2l_algs_one_list

    def solve_oll(self):
        oll = OLLSolver(self.cube.cube_dict)
        if oll.oll_alg:
            self.cube.apply_alg_std(oll.oll_alg)
        return oll.oll_alg

    def solve_pll(self):
        pll = PLLSolver(self.cube.cube_dict)
        if pll.pll_alg:
            self.cube.apply_alg_std(pll.pll_alg)
        return pll.pll_alg

    def give_solution_formatted(self, cross, f2l, oll, pll):
        solution_tuples = cross + f2l + oll + pll
        cross_std = self.cube.format_turns_to_alg(cross)
        f2l_std = self.cube.format_turns_to_alg(f2l)
        oll_std = self.cube.format_turns_to_alg(oll)
        pll_std = self.cube.format_turns_to_alg(pll)

        solution_std = self.cube.format_turns_to_alg(solution_tuples)
        solution_formatted = f"Cross alg: {cross_std}\nF2L alg: {f2l_std}\nOLL alg: {oll_std}\nPLL alg: {pll_std}\nFinal solution: {cross_std} {f2l_std} {oll_std} {pll_std}\nMove count: {len(solution_tuples)}"

        return solution_formatted, solution_std, solution_tuples
