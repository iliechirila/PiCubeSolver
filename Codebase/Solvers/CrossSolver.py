from collections import deque
from copy import copy

from Codebase.Common.Cube import Cube, general_turn
from Codebase.Common.Turns import Y, X, Z, TURN_MAPPING_DICT, OPPOSITE_COLORS, CW, CCW, DT
from Codebase.Solvers.BaseSolver import BaseSolver


def choose_valid_turns(turn_space: list, last_turn: tuple):
    """
    Remove duplicate moves such as RL=LR, UU=U2, UU'=same config
    This is done to eliminate the possibility of infinite loops such as U -> U' -> U ...
    The other reason is to avoid U -> U since it is equivalent to U2
    """
    for turn in turn_space:
        if turn[1] in (last_turn, OPPOSITE_COLORS[last_turn[1]]):
            turn_space.remove(turn)

    return turn_space
def generate_turn_space():
    turn_space = []
    for ori in TURN_MAPPING_DICT.keys():
        for face in TURN_MAPPING_DICT[ori].keys():
            turn_space.append((ori, face))
    return turn_space


class CrossSolver(BaseSolver):
    def __init__(self, cube_dict):
        super().__init__(cube_dict)
        # Cross specific
        self.current_cross_edges = self._find_cross_edges()
        self.pos_of_solved_cross_edges = self._find_pos_of_solved_cross_edges()
        self.colors_of_side_colors = self._find_solved_side_colors()

        self.alg, self.open_sets, self.closed_sets = self._find_path()

    def _find_cross_edges(self):
        """
        Finds the current position of the cross edges by
        color and coordinates
        """
        cross_edges = {}

        for coord, colors in self.cube_dict.items():
            # Look at edge pieces with d_color color
            if coord.count(0) == 1 and self.d_color in colors:
                cross_edges[coord] = colors

        return cross_edges

    def _find_pos_of_solved_cross_edges(self):
        """
        Finds the position of the cross edges when solved
        """
        center_dict = {}
        # Find side center colors
        for coord, color in self.cube_dict.items():
            # Look only at centers
            if coord.count(0) == 2:
                # Don't look at Up or Down centers
                if coord[1] == 0:
                    center_dict[''.join(color)] = coord

        # Dict with (k, v) = (non-white color, coordinate)
        solved_perm = {}
        for color, coord in center_dict.items():
            solved_perm[color] = (coord[0], -1, coord[2])

        return solved_perm

    def _find_solved_side_colors(self):
        """
        Finds side center colors in the order: L B R F
        """
        # The order wanted
        order = [(-1, -1, 0), (0, -1, -1), (1, -1, 0), (0, -1, 1)]
        side_colors = []

        for n in range(4):
            for color, coord in self.pos_of_solved_cross_edges.items():
                if coord == order[n]:
                    side_colors.append(color)

        return side_colors

    def _find_path(self):
        """
        A* pathfinding algorithm to solve for the cube's cross.
        """
        cn = CrossNode(self.current_cross_edges, [], self.pos_of_solved_cross_edges,
                       self.d_color, self.colors_of_side_colors)

        # Every single possible turn
        turn_space = generate_turn_space()

        self.open_set = deque([cn])
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
            closed_set.append(current.edge_perm)

            # Return if perm is equal to solved perm
            if not current.abs_h_cost:
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

                cn = CrossNode(new_perm, new_alg, self.pos_of_solved_cross_edges,
                               self.d_color, self.colors_of_side_colors)
                self._move_up(cn)


class CrossNode:
    """
    The class represents a node in the A* algorithm.

    The metric from the intial state is defined as the sum of the absolute
    value of the difference of each of the three coordinates. (e.g. the
    difference between [-1, 1, -1] and [1, 1, 1] is 2 + 0 + 2 = 4]. This metric
    is found for the one absolute and three relative positions of the cross.
    This can be imagined like rotating just the side centers and seeing how
    close the cube is to having a cross.

    The absolute measure (abs_h_cost) is used to determine if a cross has been
    found. The relative measure (rel_h_cost) is used with the flip_penatly for
    the h_cost which is used everywhere else. The f_cost is the total metric
    which also sums the current length of the algorithm as a factor.

    Moves are applied to the cube like usual, but only the four cross edges
    are moved since the permuation of the other cubies is irrelevant.

    Parameters:
    edge_perm - The permutation of just the four cross edges in dict form
    alg - The alg used to obtain this current edge_perm from the initial perm
          of the cube
    solved_perm - The color-first dict of the permutation of the edges if they
                   were solved
    d_color - The color of the Down face (i.e. of the cross being solved)
    solved_side_colors - A 4-element list of the side colors of the cross in
                         the order: F R D L to use as a reference for relative
                         positions of the current cross edge pieces
    """

    def __init__(self, edge_perm, alg: list, solved_perm, d_color,
                 solved_side_colors):
        # Constant for every CrossNode object
        self.solved_perm = solved_perm
        self.d_color = d_color

        # Constant for each CrossNode object
        self.edge_perm = edge_perm
        self.solved_side_colors = solved_side_colors
        self.cross_edges = self._cross_edges()
        self.alg = alg

        # Metrics
        # A factor of 2 because a bad flip is equivalent to a metric score
        # of 2. So each bad edge adds 2 to the metric
        self.flip_penalty = 2 * self._flip_penalty()
        self.g_cost = len(self.alg)
        self.rel_h_cost, self.abs_h_cost = self._all_metrics()
        self.abs_h_cost += self.flip_penalty
        self.h_cost = self.rel_h_cost + self.flip_penalty
        self.f_cost = self.h_cost + self.g_cost

    def _cross_edges(self):
        """
        Cross edge dict by (k, v) = (color, coord).
        """
        cross_edge_dict = {}
        for coord, colors in self.edge_perm.items():
            colors_copy = colors.copy()
            colors_copy.remove(self.d_color)
            colors_copy.remove('')

            cross_edge_dict[colors_copy[0]] = coord

        return cross_edge_dict

    def _flip_penalty(self):
        """
        Counts number of edge pieces that are wrongly flipped.
        """
        bad_flip = 0
        for coord, colors in self.edge_perm.items():
            # Can only be wrongly flipped if on D or U face
            if coord[1] != 0:
                # But white sticker isn't on D or U face
                if self.d_color in [colors[0], colors[2]]:
                    bad_flip += 1
        return bad_flip

    def _all_metrics(self):
        """
        Finds the metric for each relative position of the side center pieces
        and returns the value for the minimum of these along with the metric
        for the absolute position.
        """
        # Find the absolute metric
        abs_tot_distance = self._metric(self.solved_perm)
        min_tot_distance = 100
        # Try each of the 3 remaining relative positions
        # (rotations of side centers)
        for turn in range(1, 4):
            rel_solved_perm = {}
            # Rotate colors in side edge dict
            for n, color in enumerate(self.solved_side_colors):
                new_color = self.solved_side_colors[(n + turn) % 4]
                rel_solved_perm[new_color] = self.solved_perm[color]
            # Calculate metric for new dict
            tot_distance = self._metric(rel_solved_perm)

            # Keep value if is less than current minimum
            if tot_distance < min_tot_distance:
                min_tot_distance = tot_distance

        return min(min_tot_distance, abs_tot_distance), abs_tot_distance

    def _metric(self, end_pos):
        """
        Sums the difference of each coordinate dimension
        """
        tot_distance = 0

        for color, coord in self.cross_edges.items():
            tot_distance += sum(map(lambda x, y: abs(x - y),
                                    coord, end_pos[color]))
        return tot_distance

    def apply_turn(self, turn):
        return general_turn(self.edge_perm, turn)
