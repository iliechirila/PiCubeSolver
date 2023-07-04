from Codebase.Common.Cube import Cube
from Codebase.Solvers.CrossSolver import CrossSolver
from Codebase.Solvers.F2LSolver import F2LSolver
from Codebase.Solvers.OLLSolver import OLLSolver
from Codebase.Solvers.PLLSolver import PLLSolver

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
    # cube.apply_alg_std("L2 R' U2 D2 B L B2 F R D R' L' D2 B' F2 R2 F U L' R2")
    ################ BAD SCRAMBLE FLIPS 3 PIECES IN F2L #####################################
    # cube.apply_alg_std("F L' D U F D L U R2 D2 L' R2 B2 F2 L2 R2 D' F2 R2 B2 L R2 B' U R2 B2 L' U2 F D")
    # cube.apply_alg_std("F R2 B' R2 B' U2 F' D' L R D' U2 B2 U L D2 B' F' L2 D' L2 R U R F")
    #########################################################################################
    # ok
    # F' D' U B F2 L U' R B F2 R2 D2 F U L' R' F2 D U B' R B2 R' F R2 F' L2 D2 B R2
    cube.apply_alg_std("F' D' U B F2 L U' R B F2 R2 D2 F U L' R' F2 D U B' R B2 R' F R2 F' L2 D2 B R2")

    cs = CrossSolver(cube.cube_dict)
    alg = cs.alg
    cube.apply_alg_tuple(alg)
    print(f"Cross alg: {alg}")
    # F R' B L' D R' D2 R
    # cube.graph_cube()

    print("F2L algs:")

    f2l = F2LSolver(cube.cube_dict)
    f2l_algs = f2l.alg_overall
    for alg in f2l_algs:
        print(alg)
        cube.apply_alg_tuple(alg)
    # f2l_algs = [[('L', 'cw'), ('U', 'dt'), ('L', 'dt'), ('U', 'dt'), ('L', 'cw')],
    # [('R', 'cw'), ('B', 'ccw'), ('U', 'ccw'), ('B', 'cw'), ('R', 'cw'), ('B', 'ccw'), ('R', 'ccw'), ('B', 'cw'),('R', 'ccw')],
    # [('L', 'ccw'), ('B', 'ccw'), ('L', 'dt'), ('U', 'cw'), ('L', 'dt'), ('B', 'cw'), ('L', 'dt'), ('U', 'ccw'),('L', 'ccw'), ('U', 'cw'), ('L', 'cw'), ('U', 'ccw'), ('L', 'ccw')],
    # [('U', 'dt'), ('R', 'ccw'), ('U', 'cw'), ('R', 'ccw'), ('F', 'cw'), ('R', 'cw'), ('F', 'ccw'), ('R', 'cw')]]
    # for alg in f2l_algs:
    #     cube.apply_alg_tuple(alg)
    cube.graph_cube()


    # cube.graph_cube()

    oll = OLLSolver(cube.cube_dict)
    print("OLL Alg:")
    if oll.oll_alg:
        print(oll.oll_alg)
        cube.apply_alg_std(oll.oll_alg)
    cube.graph_cube()

    pll = PLLSolver(cube.cube_dict)
    print("PLL Alg:")
    if pll.pll_alg:
        print(pll.pll_alg)
        cube.apply_alg_std(pll.pll_alg)
    cube.graph_cube()
    print(cube.cube_dict)

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