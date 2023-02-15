from Codebase.Common.Cube import Cube
from sys import getsizeof

from Codebase.Solvers.CrossSolver import CrossSolver

"""
This is the main file where everything is supposed to run from at this point in time.
"""


if __name__ == '__main__':
    # For scramble: L' D2 B' L2 U2 B R2 D2 U2 F2 U2 F2 L' R2 D' L R2 F' R
    cubestring = ['rowwwoyry', 'wrbwowgrb', 'rbgbggwgr', 'oboorbyry', 'gybybobwr', 'oygyygwgo']
    cube = Cube()
    print(cube.cube_dict)
    cube.apply_alg_std("L' D2 B' L2 U2 B R2 D2 U2 F2 U2 F2 L' R2 D' L R2 F' R")

    cs = CrossSolver()
    alg = cs.solve(cube,[],0,0)

    print(alg)

