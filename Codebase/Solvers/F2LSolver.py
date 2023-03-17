import itertools
from collections import deque
from copy import copy

from Codebase.Common.Cube import general_turn
from Codebase.Common.Turns import U, D, R, L, F, B, CW, CCW, DT
from Codebase.Solvers.BaseSolver import BaseSolver
from Codebase.Solvers.CrossSolver import generate_turn_space, choose_valid_turns


class F2LSolver(BaseSolver):

    def __init__(self, cube_dict):
        super().__init__(cube_dict)

        f2l_pairs = ['go', 'gr', 'bo', 'br']

        self.alg_overall, self.open_sets_overall, self.closed_sets_overall = [], [], []
        self.centers = self._centers_key_color()
        self.cross = self._find_pos_of_solved_cross_edges()

        self.init_config = self.cross.copy()
        self.goal_config = self.cross.copy()

        for f2l_pair in f2l_pairs:
            # Add current/solved position to init_perm/goal_perm, respectively
            self._add_pair(f2l_pair)

            alg, open_sets, closed_sets = self._find_path()

            self.alg_overall.append(alg)
            self.open_sets_overall.append(open_sets)
            self.closed_sets_overall.append(closed_sets)

    def _add_pair(self, f2l_pair: str):
        color1 = f2l_pair[0]
        color2 = f2l_pair[1]

        for coord, colors in self.cube_dict.items():
            if color1 in colors and color2 in colors:
                if coord.count(0) == 1:
                    edge_coord = coord
                elif self.d_color in colors:
                    corner_coord = coord

        # Add initial cubies to the init_config
        self.init_config[edge_coord] = self.cube_dict[edge_coord]
        self.init_config[corner_coord] = self.cube_dict[corner_coord]

        self.goal_config[edge_coord] = self.solved_cube[edge_coord]
        self.goal_config[corner_coord] = self.solved_cube[corner_coord]


    def _find_path(self):
        """
        A* pathfinding algorithm to solve the first 2 layers of the cube.
        """
        slot_coord = (-1,0,-1) # just because
        fn = F2LNode(self.cube_dict, self.solved_cube, [],
                          self.d_color, [], slot_coord)

        # Every single possible turn
        turn_space = generate_turn_space()

        self.open_set = deque([fn])
        closed_set = []

        while True:
            # Take object with lowest f_cost
            current = self.open_set[0]
            # Find current turn_space
            if current.alg:
                turn = current.alg[-1]
                turn_space_current = choose_valid_turns(copy(turn_space), turn)
            else:
                turn_space_current = turn_space

            # Remove from open set
            self.open_set.remove(current)
            # Move last node to top of tree
            self.open_set.rotate()
            # Compare it downwards
            self._move_down()
            # Add to closed set
            closed_set.append(current.cur_config)

            # Return if perm is equal to solved perm
            print(current.abs_h_cost)
            # if not current.abs_h_cost:
            if current.abs_h_cost == 4:
                return current.alg, len(self.open_set), len(closed_set)

            # Create new objects and put in open_set to
            # check next if perm hasn't already been found
            new_alg_len = len(current.alg) + 1
            for turn in turn_space_current:
                new_perm = current.apply_turn(turn)
                new_alg = copy(current.alg)
                new_alg.append(turn)
                if new_perm in closed_set or new_alg_len == 12:
                    continue

                fn = F2LNode(new_perm, self.goal_config, new_alg, self.d_color,current.did_slot_turn, current.slot_coord)
                self._move_up(fn)


class F2LNode:
    # what the actual
    def __init__(self, current_config, goal_config, alg, d_color, slot_turn, slot_coord):
        self.d_color = d_color
        self.alg = alg  # alg so far

        self.cur_config = current_config  # current config of the cubies
        self.goal_config = goal_config

        self.slot_coord = slot_coord
        self.did_slot_turn = self._slot(slot_turn, slot_coord)
        self.rel_goal_config = self._rel_goal_perm()

        # Metrics
        self.flip_penalty = 2 * self._flip_penalty()
        self.rel_h_cost = self._slot_metric()
        self.g_cost = len(self.alg)

        self.h_cost = self.rel_h_cost + self.flip_penalty
        self.abs_h_cost = self._metric() + self.flip_penalty
        self.f_cost = self.h_cost + self.g_cost

    def _rel_goal_perm(self):
        if not self.did_slot_turn or self.did_slot_turn[0] == '_':
            return self.goal_config.copy()

        return self.apply_turn(self.did_slot_turn)

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
            (-1, 0, -1): [(B, CW), (B, CCW), (B, DT), (L, CW), (L, CCW), (L, DT)],
            # Front Left
            (-1, 0, 1): [(F, CW), (F, CCW), (F, DT), (L, CW), (L, CCW), (L, DT)],
            # Back Right
            (1, 0, -1): [(B, CW), (B, CCW), (B, DT), (R, CW), (R, CCW), (R, DT)],
            # Front Right
            (1, 0, 1): [(F, CW), (F, CCW), (F, DT), (R, CW), (R, CCW), (R, DT)]
        }

        valid_moves = turn_dict[slot_coord]
        # Check if the slot moved out of its initial pos
        if self.alg[-1] in valid_moves:
            # Check if the face of the last move corresponds with the face of the
            # turn that got the slot out of place
            # print(valid_moves)
            # print(self.alg[-1])
            # If the last move does not affect the pair, pass the last slot_turn
            if slot_turn and self.alg[-1][0] != slot_turn[0]:
                return slot_turn

            # print(self.alg[-1][0], slot_turn)
            # Otherwise, generate a new turn
            def get_swap_dict(d):
                return {v: k for k, v in d.items()}

            tool_dict = {
                '_': 0,
                CW: 1,
                CCW: 2,
                DT: 3
            }

            # basically tells what kind of rotation was the last move (cw,ccw,dt)
            last_turn_ori = self.alg[-1][1]
            # tells what kind of rotation was the last move that got the slot out
            if slot_turn:
                slot_ori = slot_turn[1]
            else:
                slot_ori = '_'
                slot_turn = '_'
            # ori of the new turn
            new_ori = (tool_dict[last_turn_ori]+tool_dict[slot_ori]) % 4
            # Reverse the tool dict
            tool_dict = get_swap_dict(tool_dict)
            new_ori = tool_dict[new_ori] # it is reversed so wwe get the str
            if not slot_turn:
                slot_turn = tool_dict[slot_turn]
            # either same move or the other face of the pair but same orientation???
            if new_ori:
                # new orientation and the face of the slot
                new_turn = (slot_turn[0],new_ori)
            else:
                new_turn = ()

            return new_turn
        return slot_turn

    def _flip_penalty(self):
        """
        Counts number of edge pieces that are wrongly flipped.
        """
        bad_flip = 0
        for coord, colors in self.cur_config.items():
            # Can only be wrongly flipped if on D or U face
            if coord[1] != 0:
                # But white sticker isn't on D or U face
                if self.d_color in [colors[0], colors[2]]:
                    bad_flip += 1
        return bad_flip

    def _slot_metric(self):
        """
        The metric but reletive to the slot as determined by self._slot
        """
        if not len(self.alg) or not self.did_slot_turn:
            return self._metric()

        # Create a copy of goal_perm and update it with where the slot is
        new_goal_perm = self.goal_config.copy()
        new_goal_perm.update(self.rel_goal_config)

        return self._metric(new_goal_perm)
    def _metric(self, goal_config={}):
        """
        Sums the difference of each coordinate dimension
        """
        goal_config = goal_config or self.goal_config
        tot_distance = 0

        tot_distance = 0

        def find_key(dct, chars):
            for key, value in dct.items():
                if sorted(value) == sorted(chars):
                    return key
            return ''

        for coord, color in self.cur_config.items():
            tot_distance += sum(map(lambda x, y: abs(x - y),
                                    coord, list(find_key(goal_config, color))))
        return tot_distance


    def apply_turn(self, turn):
        return general_turn(self.cur_config, turn)
