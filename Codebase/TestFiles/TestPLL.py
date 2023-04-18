from Codebase.Common.Cube import Cube
from Codebase.Solvers.PLLSolver import PLLSolver

if __name__ == '__main__':
    cube = Cube()

    cube.apply_alg_std("U2 L' U R' U2 L U' R U L' U R' U2 L U' R U2")
    pll = PLLSolver(cube.cube_dict)
    print(pll.pll_alg)
    cube.apply_alg_std(pll.pll_alg)
    cube.graph_cube()