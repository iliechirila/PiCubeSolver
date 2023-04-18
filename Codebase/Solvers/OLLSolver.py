from Codebase.Common.Cube import general_turn
from Codebase.Common.OLL_algs import oll_algs
from Codebase.Common.Turns import Y, CW, U, DT, CCW
from Codebase.Solvers.BaseSolver import BaseSolver


class OLLSolver(BaseSolver):

    def __init__(self, cube_dict):
        super().__init__(cube_dict)
        self.turns_needed = ['', 'U ', 'U2 ', "U' "]
        self.top_cubies = {}
        self.check_top_color = {}
        # TODO Add OLL skip check
        for i in range(4):
            self.top_cubies = self._top_cubies()
            self.check_top_color = self._check_top_color()
            self.oll_alg = self._find_oll_alg()
            if self.oll_alg:
                # print("Found him")
                print(f"OLL Index is {i}")
                self.oll_alg = self.turns_needed[i] + self.oll_alg
                break
            self.cube_dict = general_turn(self.cube_dict, (U, CW))

    def _find_oll_alg(self):
        for name, perm_alg in oll_algs.items():
            # print(perm_alg[1])
            perm, alg = perm_alg
            found = True
            for coord, yellow_pattern in perm.items():
                if self.check_top_color[coord] != yellow_pattern:
                    found = False
                    break
            if found:
                return alg
        return False
    def _check_top_color(self):
        top_color = {}
        for coord, color in self.top_cubies.items():
            color_check = tuple(x == y for x,y in zip(color, (self.u_color, self.u_color, self.u_color)))
            top_color.update({coord: color_check})
        return top_color
    def _top_cubies(self):
        top_cubies = {}
        for coord, color in self.cube_dict.items():
            if coord[Y] == 1:
                top_cubies.update({coord: color})
        return top_cubies