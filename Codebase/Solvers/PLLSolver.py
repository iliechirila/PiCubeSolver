from Codebase.Common.Cube import general_turn
from Codebase.Common.PLL_algs import pll_algs_dict
from Codebase.Common.Turns import Y, U, CW, DT, CCW
from Codebase.Solvers.BaseSolver import BaseSolver


class PLLSolver(BaseSolver):

    def __init__(self, cube_dict):
        super().__init__(cube_dict)
        self.pll_alg = None
        self.turns_needed = ['', 'U', 'U2', "U'"]
        self.turns_needed_tuple = [(), (U, CW), (U, DT), (U, CCW)]

        # TODO Add PLL skip check
        self.side_colors = self._side_colors()
        self.side_colors_rotations = [(lambda lst, i: lst[i:] + lst[:i])(self.side_colors, i) for i in range(len(self.side_colors))]
        self._find_alg()

    def _side_colors(self):
        side_colors = []
        for coord in [(0, 0, 1), (-1, 0, 0), (0, 0, -1), (1, 0, 0)]:
            side_colors.append(next((s for s in self.cube_dict[coord] if s), None))
        return side_colors

    def _find_alg(self):
        # for every side colors configuration
        for i in range(4):
            front, left, back, right = self.side_colors_rotations[i]
            pll_algs = pll_algs_dict(self.u_color, front, left, back, right)
            # check each alg with turns needed
            for j in range(4):
                cpy_cube_dict = self.cube_dict.copy()
                if self.turns_needed_tuple[j]:
                    cpy_cube_dict = general_turn(cpy_cube_dict, self.turns_needed_tuple[j])
                self.top_cubies = self._top_cubies(cpy_cube_dict)
                # ugh multiple for-ladders. It is what it is
                alg = self._check_algs_rotation(pll_algs)
                print(alg)
                if alg:
                    print(j)
                    self.pll_alg = self.turns_needed[j] + " " + alg + " " + self.turns_needed[4-i]
                    break
            if alg:
                break

    def _check_algs_rotation(self, pll_algs):
        for name, perm_alg in pll_algs.items():
            perm, alg = perm_alg
            found = True
            if name == "G Permutation: a":
                print(self.top_cubies)
                print(perm)
            for coord, colors_pattern in perm.items():

                if self.top_cubies[coord] != list(colors_pattern):
                    found = False
                    break
            if found:
                return alg
        return False


    def _top_cubies(self, cube_dict):
        top_cubies = {}
        for coord, color in cube_dict.items():
            if coord[Y] == 1:
                top_cubies.update({coord: color})
        return top_cubies