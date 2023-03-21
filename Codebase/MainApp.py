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

    cs = CrossSolver(cube.cube_dict)
    alg = cs.alg
    cube.apply_alg_tuple(alg)
    print(f"Cross alg: {alg}")

    # cube.graph_cube()

    # go_alg = [('L', 'ccw'), ('D', 'dt'), ('R', 'dt')]

    # cube.apply_alg_tuple(go_alg)

    # cube.graph_cube()
    f2l = F2LSolver(cube.cube_dict)
    for alg in f2l.alg_overall:
        cube.apply_alg_tuple(alg)
        cube.graph_cube()

"""
['go', 'gr', 'bo', 'br']
Pair: go
[('L', 'ccw'), ('D', 'dt'), ('R', 'dt')]
Pair: gr
[('U', 'cw'), ('B', 'ccw'), ('L', 'ccw'), ('U', 'cw'), ('L', 'cw')]
Pair: bo
[('B', 'ccw'), ('R', 'cw'), ('F', 'cw'), ('R', 'cw'), ('D', 'ccw'), ('F', 'cw'), ('U', 'cw'), ('B', 'cw')]
Pair: br
[('R', 'ccw'), ('F', 'cw'), ('R', 'ccw'), ('B', 'ccw'), ('R', 'cw'), ('F', 'cw'), ('U', 'cw'), ('B', 'ccw'), ('D', 'cw'), ('B', 'ccw')]

Process finished with exit code 0


"""