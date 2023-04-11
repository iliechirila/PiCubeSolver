from Codebase.Common.Cube import general_turn
from Codebase.Common.OLL_algs import oll_algs
from Codebase.Common.Turns import Y, CW, U, DT, CCW
from Codebase.Solvers.BaseSolver import BaseSolver


class OLLSolver(BaseSolver):

    def __init__(self, cube_dict):
        super().__init__(cube_dict)
        self.turns_needed = [(), (U, CW), (U, DT), (U, CCW)]
        self.top_cubies = {}
        self.check_top_color = {}
        for i in range(4):
            self.top_cubies = self._top_cubies()
            self.check_top_color = self._check_top_color()
            self.oll_alg = self._find_oll_alg()
            if self.oll_alg:
                print("Found him")
                break
            self.cube_dict = general_turn(self.cube_dict, (U, CW))

    def _find_oll_alg(self):
        for name, perm_alg in oll_algs.items():
            print(perm_alg[1])
            if perm_alg[0] == list(self.check_top_color.values()):
                print(name)
                return perm_alg[1]
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