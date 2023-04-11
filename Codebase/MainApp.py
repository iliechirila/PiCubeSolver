from Codebase.Common.Cube import Cube
from Codebase.Solvers.CrossSolver import CrossSolver
from Codebase.Solvers.F2LSolver import F2LSolver
from Codebase.Solvers.OLLSolver import OLLSolver

"""
This is the main file where everything is supposed to run from at this point in time.
"""


if __name__ == '__main__':
    # For scramble: L' D2 B' L2 U2 B R2 D2 U2 F2 U2 F2 L' R2 D' L R2 F' R
    # cross alg: D' R B D L' D B' D'

    # For scramble: D' F2 R U2 L B2 F2 L D2 L2 D2 R B' L B2 R' U' R' D B'
    # R2 F D2 B2 D R' B2

    cube = Cube()
    # cube.apply_alg_std("D' F2 R U2 L B2 F2 L D2 L2 D2 R B' L B2 R' U' R' D B'")
    cube.apply_alg_std("L2 R' U2 D2 B L B2 F R D R' L' D2 B' F2 R2 F U L' R2")

    cs = CrossSolver(cube.cube_dict)
    alg = cs.alg
    cube.apply_alg_tuple(alg)
    print(f"Cross alg: {alg}")
    # F R' B L' D R' D2 R
    # cube.graph_cube()

    # rg_alg = [('U', 'dt'), ('R', 'cw'), ('U', 'cw'), ('R', 'ccw')]
    # cube.apply_alg_tuple(rg_alg)
    # f2l_pairs = [(('r', 'b'), ('r', 'g', 'w'), 'cw'),
    #              (('r', 'g'), ('o', 'g', 'w'), 'ccw'),
    #              (('o', 'g'), ('o', 'b', 'w'), 'cw'),
    #              (('o', 'b'), ('r', 'b', 'w'), 'ccw')]
    f2l = F2LSolver(cube.cube_dict)
    for alg in f2l.alg_overall:
        cube.apply_alg_tuple(alg)
    cube.graph_cube()

    oll = OLLSolver(cube.cube_dict)
    if oll.oll_alg:
        cube.apply_alg_std(oll.oll_alg)
    cube.graph_cube()

"""
['go', 'gr', 'bo', 'br']
Pair: go
[[('F', 'ccw'), ('U', 'cw'), ('F', 'cw'), ('U', 'ccw'), ('F', 'dt'), ('L', 'dt'), ('F', 'dt'), ('L', 'dt')]]
[[('U', 'cw'), ('F', 'cw'), ('U', 'dt'), ('F', 'dt'), ('L', 'cw'), ('F', 'cw'), ('L', 'ccw')]]
AND IT WORKS
Pair: gr
[('U', 'cw'), ('B', 'ccw'), ('L', 'ccw'), ('U', 'cw'), ('L', 'cw')]
Pair: bo
[('B', 'ccw'), ('R', 'cw'), ('F', 'cw'), ('R', 'cw'), ('D', 'ccw'), ('F', 'cw'), ('U', 'cw'), ('B', 'cw')]
Pair: br
[('R', 'ccw'), ('F', 'cw'), ('R', 'ccw'), ('B', 'ccw'), ('R', 'cw'), ('F', 'cw'), ('U', 'cw'), ('B', 'ccw'), ('D', 'cw'), ('B', 'ccw')]

Process finished with exit code 0


"""