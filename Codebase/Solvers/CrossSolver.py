from copy import copy

from Codebase.Common.Cube import Cube
from Codebase.Common.Turns import Y, X, Z, TURN_MAPPING_DICT, CW, CCW, DT

SOLVED = 4


def choose_valid_turns(alg):
    """
    This is done to eliminate the possibility of infinite loops such as U -> U' -> U ...
    The other reason is to avoid U -> U since it is equivalent to U2
    """
    if len(alg)==0:
        last_turn = "congrats you found this string"
    else:
        last_turn = alg[-1]
    valid_turns = []
    for turn_ori in TURN_MAPPING_DICT.keys():
        for turn_face in TURN_MAPPING_DICT[turn_ori].keys():
            if turn_face != last_turn[1]:
                valid_turns.append((turn_ori, turn_face))
    return valid_turns


class CrossSolver:
    def __init__(self):
        print("Created Cross Solver")

    def solve(self, current_cube: Cube, alg, move_cnt, current_progress):
        print(move_cnt)
        print(alg)
        prog = self.cross_progress(current_cube.cube_dict)
        if move_cnt > 10:
            return 0
        if prog == SOLVED:
            return alg
        valid_turns = choose_valid_turns(alg)

        for turn in valid_turns:
            cpy_alg = copy(alg)
            cpy_cube = copy(current_cube)
            cpy_cube.turn(turn)
            cpy_alg.append(turn)
            self.solve(cpy_cube, cpy_alg, copy(move_cnt)+1, prog)

    def cross_progress(self, cube_dict: dict):
        top_edges = [(-1,1,0),(1,1,0),(0,1,1),(0,1,-1)]
        solved_pieces = 0
        # iterates through the cubies and looks for the edges on top (Y axis points up)
        # yes, the cross is built on top at this moment in time
        for cubie  in top_edges:
            colors = cube_dict[cubie]
            if colors[Y] == 'w':
                if cubie[X] != 0:
                    if colors[X] == cube_dict[cubie[X],0,0]:
                        solved_pieces += 1
                elif cubie[Z] != 0:
                    if colors[Z] == cube_dict[0, 0, cubie[Z]]:
                        solved_pieces += 1
        return solved_pieces

