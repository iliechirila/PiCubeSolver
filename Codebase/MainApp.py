from copy import deepcopy

from Codebase.Common.Cube import Cube
from sys import getsizeof

from Codebase.Solvers.CrossSolver import CrossSolver
from Codebase.Solvers.F2LSolver import F2LSolver

"""
This is the main file where everything is supposed to run from at this point in time.
"""


if __name__ == '__main__':
    # For scramble: L' D2 B' L2 U2 B R2 D2 U2 F2 U2 F2 L' R2 D' L R2 F' R
    # cross alg: D' R B D L' D B' D'

    # For scramble: D' F2 R U2 L B2 F2 L D2 L2 D2 R B' L B2 R' U' R' D B'
    # R2 F D2 B2 D R' B2

    cube = Cube()
    cube.apply_alg_std("D' F2 R U2 L B2 F2 L D2 L2 D2 R B' L B2 R' U' R' D B'")
    cube_cpy = deepcopy(cube)

    cs = CrossSolver(cube.cube_dict)
    alg = cs.alg
    cube.apply_alg_tuple(alg)
    print(alg)

    # cube.graph_cube()


    f2l = F2LSolver(cube.cube_dict)
    alg_f2l = f2l.alg_overall[-1]
    print(alg_f2l)

    cube_cpy.apply_alg_tuple(alg_f2l)
    cube_cpy.graph_cube()