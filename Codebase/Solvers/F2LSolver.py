import itertools
from collections import deque
from copy import copy
from operator import add

from Codebase.Common.Cube import general_turn, Cube
from Codebase.Common.Turns import U, D, R, L, F, B, CW, CCW, DT, TURN_SPACE, ORIENTATION, TURN_MAPPING_DICT, X, \
    TARGET_AXIS, TARGET_REORIENTATION, Y, Z
from Codebase.Solvers.BaseSolver import BaseSolver
from Codebase.Solvers.CrossSolver import generate_turn_space, choose_valid_turns


class F2LSolver(BaseSolver):

    def __init__(self, cube_dict):
        super().__init__(cube_dict)
        self.cube_perm = {cubie_key(color): (list(coord), color)
                          for coord, color in cube_dict.items()}
        f2l_pairs = ['go', 'gr', 'bo', 'br']
        self.d_color = ''.join(cube_dict[(0, -1, 0)])
        self.u_color = ''.join(cube_dict[(0, 1, 0)])
        self.alg_overall, self.open_sets_overall, self.closed_sets_overall = [], [], []
        self.centers = self._centers()
        self.cross = self._find_pos_of_solved_cross_edges()
        self.index = 0
        self.init_config = self.cross.copy()
        self.goal_config = self.cross.copy()
        for f2l_pair in f2l_pairs:
            # Add current/solved position to init_perm/goal_config, respectively
            self._add_pair(f2l_pair)
            # print(f"Goal for pair {f2l_pair}: {self.goal_config}")
            alg, open_sets, closed_sets, cur_config = self._find_path(f2l_pair)
            # print(f"Current config:{cur_config}")
            self.init_config = self.goal_config.copy()
            self.alg_overall.append(alg)
            self.open_sets_overall.append(open_sets)
            self.closed_sets_overall.append(closed_sets)
            # TURN DUDE JUST TURN
            self.apply_alg_tuple(alg)

    def apply_alg_tuple(self, alg: list):
        for move in alg:
            self.cube_perm = _new_turn(move, self.cube_perm)

    def _centers(self):
        """
        Returns a dict of the 6 centers
        """
        colors = ['w', 'o', 'g', 'r', 'b', 'y']

        centers = {frozenset(c): self.cube_perm[frozenset(c)] for c in colors}

        return centers
    def _find_pos_of_solved_cross_edges(self):
        """
        Finds the position of the cross edges when solved
        """
        colors = ['w', 'o', 'g', 'r', 'b', 'y']
        colors.remove(self.d_color)
        colors.remove(self.u_color)

        cross = {frozenset((c + self.d_color, self.d_color + c)):
                     self.cube_perm[frozenset((c + self.d_color, self.d_color + c))]
                 for c in colors}

        return cross

    def _add_pair(self, f2l_pair: str):
        edge_key = cubie_key(f2l_pair)
        corner_key = cubie_key(f2l_pair + self.d_color)

        # Add current position cubies to init_perm
        self.init_config[edge_key] = self.cube_perm[edge_key]
        self.init_config[corner_key] = self.cube_perm[corner_key]

        # Find centers that the F2L pair is between
        pair_centers = (self.centers[frozenset(f2l_pair[0])],
                        self.centers[frozenset(f2l_pair[1])])
        # Add coords and colors together to get solved position of edge piece
        edge_coord = list(map(add, pair_centers[0][0], pair_centers[1][0]))
        edge_color = list(map(add, pair_centers[0][1], pair_centers[1][1]))
        # Convert above for the solved position of corner piece
        corner_coord = list(map(add, edge_coord, [0, -1, 0]))
        corner_color = list(map(add, edge_color, ['', self.d_color, '']))
        # Add both pieces to goal_config
        self.goal_config[edge_key] = (edge_coord, edge_color)
        self.goal_config[corner_key] = (corner_coord, corner_color)

    def _find_path(self, f2l_pair):
        """
        A* pathfinding algorithm to solve the first 2 layers of the cube.
        """
        f2l_key = [cubie_key(f2l_pair),
                   cubie_key(f2l_pair + self.d_color)]
        slot_coord = tuple(self.goal_config[f2l_key[0]][0])
        print(slot_coord)
        fn = F2LNode(self.init_config, self.goal_config, [],
                     self.d_color, [], slot_coord)

        # Every single possible turn
        turn_space = generate_turn_space()

        self.open_set = deque([fn])
        closed_set = []

        while True:
            # Take object with lowest f_cost
            current = self.open_set.popleft()
            # Find current turn_space
            if current.alg:
                turn = current.alg[-1]
                turn_space_current = choose_valid_turns(copy(turn_space), turn)
            else:
                turn_space_current = turn_space

            # # Remove from open set
            # self.open_set.remove(current)
            # Move last node to top of tree
            self.open_set.rotate(1)
            # Compare it downwards
            self._move_down()
            # Add to closed set
            closed_set.append(current.cur_config)

            # Return if perm is equal to solved perm
            if current.abs_h_cost == 0:
                return current.alg, len(self.open_set), len(closed_set), current.cur_config

            # Create new objects and put in open_set to
            # check next if perm hasn't already been found
            for turn in turn_space_current:
                self.index += 1
                print(self.index, current.abs_h_cost, current.did_slot_turn, current.alg)
                new_perm = current.apply_turn(turn)
                # new_perm = {cubie_key(color): (list(coord), color)
                #               for coord, color in new_perm.items()}
                new_alg = copy(current.alg)
                new_alg.append(turn)
                if new_perm in closed_set:
                    continue

                fn = F2LNode(new_perm, self.goal_config, new_alg, self.d_color, current.did_slot_turn, slot_coord)
                self._move_up(fn)


def cubie_key(color):
    return frozenset(map(''.join, itertools.permutations(color)))


def _new_turn(turn_tuple, config):
    face, rot_type = turn_tuple
    new_config = {}
    relevant_axis = ORIENTATION[face][0]
    orientation = ORIENTATION[face][1]
    perm = TURN_MAPPING_DICT[rot_type][face]

    if relevant_axis is None:
        raise Exception(f"{face} is not a valid move notation.")

    for stickers, cordlor in config.items():
        # find the relevant cubies by axis and orientation
        coord, colors = cordlor
        if coord[relevant_axis] == orientation:
            key = [None, None, None]
            key[perm[X][TARGET_AXIS]] = perm[X][TARGET_REORIENTATION] * coord[X]
            key[perm[Y][TARGET_AXIS]] = perm[Y][TARGET_REORIENTATION] * coord[Y]
            key[perm[Z][TARGET_AXIS]] = perm[Z][TARGET_REORIENTATION] * coord[Z]
            val = [None, None, None]
            val[perm[X][TARGET_AXIS]] = colors[X]
            val[perm[Y][TARGET_AXIS]] = colors[Y]
            val[perm[Z][TARGET_AXIS]] = colors[Z]
            new_config[stickers] = (key, val)
        else:
            new_config[stickers] = cordlor

    # Returns the cubies that change orientation
    return new_config


class F2LNode:
    def __init__(self, current_config, goal_config, alg, d_color, slot_turn, slot_coord):
        self.d_color = d_color
        self.alg = alg  # alg so far

        self.cur_config = current_config  # current config of the cubies
        self.goal_config = goal_config

        self.slot_coord = slot_coord
        self.did_slot_turn = self._slot(slot_turn, slot_coord)
        self.rel_goal_config = self._rel_goal_config()
        # self.rel_goal_config_efficient_colors = self._rel_goal_config_efficient()

        # Metrics
        self.flip_penalty = 2 * self._flip_penalty()
        self.rel_h_cost = self._slot_metric()
        self.g_cost = len(self.alg)

        self.h_cost = self.rel_h_cost + self.flip_penalty
        self.abs_h_cost = self._metric() + self.flip_penalty
        self.f_cost = self.h_cost + self.g_cost

    def _rel_goal_config(self):
        if not self.did_slot_turn or not self.did_slot_turn[0]:
            return self.goal_config.copy()

        new_config = self.apply_turn(self.did_slot_turn, self.goal_config)
        # new_config = {cubie_key(color): (list(coord), color)
        #                   for coord, color in new_config.items()}
        return new_config


    def _slot(self, slot_turn, slot_coord):
        """
        Check if the slot (where the f2l pair will go) is moved out of its place.
        It is checked in order to keep up with the movement of the target position of the pair
        Because we work with 2 pieces at a time, it is not as easy as the cross A*
        We have to preserve the cross and also insert the pairs, ideally take out the target position and
        insert the pair in the auxiliary position; finally insert the pair in the target pos that was lifted.
        """
        # No turn
        if not len(self.alg):
            return ()
        # print(f"alg:{self.alg}")
        # Associate slot turns with their position

        turn_dict = {
            # Back Left
            (-1, 0, -1): [(), (L, CW), (L, DT), (L, CCW), (), (B, CW), (B, DT), (B, CCW)],
            # Front Left
            (-1, 0, 1): [(), (L, CW),(L, DT), (L, CCW), (), (F, CW), (F, DT), (F, CCW)],
            # Back Right
            (1, 0, -1): [(), (R, CW), (R, DT), (R, CCW), (), (B, CW), (B, DT), (B, CCW)],
            # Front Right
            (1, 0, 1): [(), (R, CW), (R, DT), (R, CCW), (), (F, CW), (F, DT), (F, CCW)]
        }

        valid_moves = turn_dict[slot_coord]
        # Check if the slot moved out of its initial pos
        if self.alg[-1] in valid_moves:
            # If it doesn't match the move set
            if slot_turn and valid_moves.index(slot_turn) // 4 != \
                    valid_moves.index(self.alg[-1]) // 4:
                return slot_turn

            turn_val = valid_moves.index(self.alg[-1]) % 4
            slot_val = valid_moves.index(slot_turn) % 4
            new_val = (turn_val + slot_val) % 4

            new_turn = valid_moves[4 * (valid_moves.index(slot_turn) // 4) + new_val]

            return new_turn
        return slot_turn

    def _flip_penalty(self):
        """
        Counts number of cubies that are in the correct position but are
        flipped incorrectly.
        """
        bad_flip = 0

        for stickers, cordlor in self.cur_config.items():
            # The 0th element is coords and 1st element is color
            # So incorrect color but correct coords means it's flipped
            if (self.rel_goal_config[stickers][0] == cordlor[0] and
                    self.rel_goal_config[stickers][1] != cordlor[1]):
                bad_flip += 1

        return bad_flip

    def _slot_metric(self):
        """
        The metric but reletive to the slot as determined by self._slot
        """
        if not len(self.alg) or not self.did_slot_turn:
            return self._metric()

        # Create a copy of goal_config and update it with where the slot is
        new_goal_config = self.goal_config.copy()
        new_goal_config.update(self.rel_goal_config)

        return self._metric(new_goal_config)

    def _metric(self, goal_config={}):
        """
        Sums the difference of each coordinate dimension
        """
        goal_config = goal_config or self.goal_config
        tot_distance = 0

        for stickers, cordlor in self.cur_config.items():
            ## Regular metric
            distance = 0
            for n in range(3):
                diff = abs(cordlor[0][n] - goal_config[stickers][0][n])
                distance += diff
            tot_distance += distance

        return tot_distance
    def apply_turn(self, turn, config=None):
        # transform from the efficient form to the general form
        # cube_dict = {tuple(coord): color for k, (coord, color) in self.cur_config.items()}
        # return general_turn(cube_dict, turn)
        config = config or self.cur_config
        return _new_turn(turn, config)
