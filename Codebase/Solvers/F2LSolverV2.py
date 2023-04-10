from Codebase.Common.Cube import general_turn
from Codebase.Common.Turns import ORIENTATION, TURN_MAPPING_DICT
from Codebase.Solvers.BaseSolver import BaseSolver


#
#
# def get_color_pairs(cube):
#     """Returns a list of tuples containing the color of the corner piece and its position."""
#     color_pairs = []
#     for position, colors in corner_positions.items():
#         color_pairs.append((cube[position], position))
#     return color_pairs
#
#
# def get_corner_color_to_position_dict():
#     """Returns a dictionary that maps each corner color to its position."""
#     corner_color_to_position = {}
#     for position, colors in corner_positions.items():
#         for color in colors:
#             corner_color_to_position[color] = position
#     return corner_color_to_position
#
#
# def get_edge_color_to_position_dict():
#     """Returns a dictionary that maps each edge color to its position."""
#     edge_color_to_position = {}
#     for position, color in edge_positions.items():
#         edge_color_to_position[color] = position
#     return edge_color_to_position
#
#
# def is_corner_in_place(color_pair, corner_color_to_position):
#     """Returns True if the corner piece is in its correct position, and False otherwise."""
#     color, position = color_pair
#     return position == corner_color_to_position[color]
#
#
# def is_edge_in_place(color_pair, edge_color_to_position):
#     """Returns True if the edge piece is in its correct position, and False otherwise."""
#     color, position = color_pair
#     return position == edge_color_to_position[color]
#
#
# def f2l_solver(cube):
#     # Define the list of F2L pairs
#     f2l_pairs = [(FRONT, RIGHT), (FRONT, LEFT), (BACK, RIGHT), (BACK, LEFT)]
#
#     # Loop through each F2L pair
#     for pair in f2l_pairs:
#         # Get the colors of the F2L pair
#         f_color, r_color = pair
#
#         # Find the location of the corner piece with the F2L pair
#         corner_location = find_corner_location(cube, f_color, r_color)
#
#         # If the corner piece is already in place, move on to the next F2L pair
#         if corner_location == f_color + r_color + CENTER:
#             continue
#
#         # If the corner piece is in the top layer, move it down to the bottom layer
#         if corner_location[1] == TOP:
#             move_sequence(cube, "U R U' R' U' F' U F")
#             corner_location = find_corner_location(cube, f_color, r_color)
#
#         # If the corner piece is in the middle layer, move it to the top layer
#         if corner_location[1] == MIDDLE:
#             face, direction = corner_location[0], corner_location[2]
#             move_sequence(cube, f"{direction} {face}' {direction}' {face}")
#             corner_location = find_corner_location(cube, f_color, r_color)
#
#         # If the corner piece is in the bottom layer, move it to the top layer
#         while corner_location[1] == BOTTOM:
#             face, direction = corner_location[0], corner_location[2]
#             move_sequence(cube, f"{direction} {face}' {direction}' {face}")
#             corner_location = find_corner_location(cube, f_color, r_color)
#
#         # Insert the corner piece into its correct position and orientation
#         face, direction = corner_location[0], corner_location[2]
#         move_sequence(cube, f"{direction}' {face}' U {face} U' {face}' U {face}")
#
#     return cube
#
#
# class F2LSolverV2(BaseSolver):
#     def __init__(self, cube_dict):
#         super().__init__(cube_dict)
#         f2l_pairs = ['go', 'gr', 'bo', 'br']
#         cross = self._find_pos_of_solved_cross_edges()
#         self.init_config = cross.copy()
#         self.goal_config = cross.copy()
#         for f2l_pair in f2l_pairs:
#             self._add_pair(f2l_pair)
#             alg = self._find_pair_solution()
#
#     def _add_pair(self, f2l_pair: str):
#         color1 = f2l_pair[0]
#         color2 = f2l_pair[1]
#
#         for coord, colors in self.cube_dict.items():
#             if color1 in colors and color2 in colors:
#                 if coord.count(0) == 1:
#                     edge_coord = coord
#                 elif self.d_color in colors:
#                     corner_coord = coord
#
#         # Add initial cubies to the init_config
#         self.init_config[edge_coord] = self.cube_dict[edge_coord]
#         self.init_config[corner_coord] = self.cube_dict[corner_coord]
#
#         for coord, colors in self.solved_cube.items():
#             if color1 in colors and color2 in colors:
#                 if coord.count(0) == 1:
#                     edge_coord = coord
#                 elif self.d_color in colors:
#                     corner_coord = coord
#         self.goal_config[edge_coord] = self.solved_cube[edge_coord]
#         self.goal_config[corner_coord] = self.solved_cube[corner_coord]
#
#     def _find_pair_solution(self):
#
#         pass


class F2LSolverV2(BaseSolver):
    def __init__(self, cube_dict, f2l_pairs=None):
        super().__init__(cube_dict)
        self.edges_to_solve = [('r', 'b'), ('r', 'g'), ('o', 'g'), ('o', 'b')]
        self.corner_to_edge_map = {('r', 'g', 'w'): ('r', 'g'), ('r', 'b', 'w'): ('r', 'b'),
                                   ('o', 'g', 'w'): ('o', 'g'), ('o', 'b', 'w'): ('o', 'b')}
        self.edge_position_map = {('r', 'b'): (1, 0, -1), ('r', 'g'): (1, 0, 1),
                                  ('o', 'g'): (-1, 0, 1), ('o', 'b'): (-1, 0, -1)}
        self.f2l_algs = []

        if f2l_pairs is not None:
            for f2l_pair in f2l_pairs:
                self.solve_f2l_pair(f2l_pair)

    def solve_edge(self, edge_color, direction):
        # Find edge cubie
        edge_pos = self.find_edge(edge_color)

        # Rotate top layer to bring edge cubie to U layer
        if edge_pos[1] == 0:
            if edge_pos[0] == -1:
                self.apply_turn(('U', 'cw'))
            else:
                self.apply_turn(('U', 'ccw'))
            edge_pos = self.find_edge(edge_color)

        # Position edge cubie to its correct slot
        if direction == 'cw':
            alg = "U R U' R' U' F' U F"
        else:
            alg = "U' L' U L U F U' F'"
        self.apply_alg_std(alg)
        self.f2l_algs.append(alg)

    def find_edge(self, edge_color):
        for position, colors in self.cube_dict.items():
            if edge_color[0] in colors and edge_color[1] in colors:
                return position

    def solve_f2l_pair(self, f2l_pair):
        edge_color, corner_colors, direction = f2l_pair
        self.solve_edge(edge_color, direction)
        self.solve_edge(self.corner_to_edge_map[corner_colors], 'ccw')

    def solve(self):
        for f2l_pair in self.edges_to_solve:
            self.solve_f2l_pair(f2l_pair)

    def get_corner_colors(self, edge_color):
        for corner, edge in self.corner_to_edge_map.items():
            if edge_color in edge:
                return corner

    def apply_alg_std(self, alg: str):
        # Format the alg string into the notation used in the TURN_MAPPING_DICT
        alg = alg.split(' ')
        # Apply the turns on the cube using the turn method
        for move in alg:
            if '2' in move:
                rot = "dt"
            elif "'" in move:
                rot = "ccw"
            else:
                rot = "cw"
            face = move[0]

            self.cube_dict.update(general_turn(self.cube_dict, (face, rot)))


class F2LSolverV3(BaseSolver):
    def __init__(self, cube):
        super().__init__(cube)
        self.algs_used = []
        self.solve()

    def solve(self):
        while not self.is_solved():
            pair, pair_pos = self.find_f2l_pair()
            if pair:
                self.insert_f2l_pair(pair, pair_pos)
            else:
                self.solve_f2l_corner()

    def find_f2l_pair(self):
        f2l_pairs = [('w', 'o'), ('w', 'r'), ('w', 'g'), ('w', 'b')]
        for pair in f2l_pairs:
            corner_color, edge_color = pair
            corner_coord = self.find_color(corner_color)
            if not corner_coord:
                continue
            for axis in range(3):
                if corner_coord[axis] != 1:
                    continue
                edge_coords = self.find_all_colors(edge_color)
                for edge_coord in edge_coords:
                    if edge_coord[axis] == 1 and self.is_f2l_pair(corner_coord, edge_coord):
                        return pair, (corner_coord, edge_coord)
        return None, None

    def is_f2l_pair(self, corner_coord, edge_coord):
        edge_color = self.cube_dict[edge_coord]
        if edge_coord[0] == corner_coord[0]:
            return edge_color[1] == self.cube_dict[(corner_coord[0], 1, corner_coord[2])][0]
        elif edge_coord[1] == corner_coord[1]:
            return edge_color[1] == self.cube_dict[(1, corner_coord[1], corner_coord[2])][0]
        else:
            return edge_color[1] == self.cube_dict[(corner_coord[0], corner_coord[1], 1)][0]

    def insert_f2l_pair(self, pair, pair_pos):
        corner_color, edge_color = pair
        corner_coord, edge_coord = pair_pos
        while corner_coord != (1, 1, 1):
            axis = max(range(3), key=lambda i: abs(corner_coord[i] - 1))
            if corner_coord[axis] > 1:
                self.apply_turn(('U', 'cw'))
            else:
                self.apply_turn(('U', 'ccw'))
        if edge_coord[1] == corner_coord[1]:
            if edge_coord[0] < corner_coord[0]:
                self.apply_alg_std("F R U' R' U' F'")
            else:
                self.apply_alg_std("F' L' U L U' F")
        elif edge_coord[0] == corner_coord[0]:
            if edge_coord[1] > corner_coord[1]:
                self.apply_alg_std("R U R' U' R' F R F'")
            else:
                self.apply_alg_std("L' U' L U L F' L' F")
        else:
            if edge_coord[0] > corner_coord[0]:
                self.apply_alg_std("R' U R U' R U R' U' R' F R F'")
            else:
                self.apply_alg_std("L U' L' U L' U' L U L F' L' F")

    def solve_f2l_corner(self):
        corner_coords = self.find_all_colors('w')
        for corner_coord in corner_coords:
            if corner_coord == (1, 1, 1):
                continue
            while corner_coord[2] != 0:
                self.apply_turn(('U', 'cw'))
                if corner_coord[0] == 1:
                    if corner_coord[1] == 0:
                        self.apply_alg_std("U' R' U R U F U' F'")
                    else:
                        self.apply_alg_std("U L U' L' U' F' U F")
                elif corner_coord[0] == 0:
                    if corner_coord[1] == 1:
                        self.apply_alg_std("U' F' U F U R U' R'")
                    else:
                        self.apply_alg_std("U' L' U L U F U' F'")
                else:
                    if corner_coord[1] == 0:
                        self.apply_alg_std("U R U' R' U' F' U F")
                    else:
                        self.apply_alg_std("U' F' U F U' L U L'")

    def is_solved(self):
        is_solved = all(self.cube_dict[coord] == color for coord, color in self.solved_cube.items())
        print(is_solved)
        return is_solved

    def find_color(self, color):
        for coord, value in self.cube_dict.items():
            if value[0] == color:
                return coord
        return None

    def find_all_colors(self, color):
        return [coord for coord, value in self.cube_dict.items() if value[0] == color]

    def apply_alg_std(self, alg: str):
        # Format the alg string into the notation used in the TURN_MAPPING_DICT
        alg = alg.split(' ')
        # Apply the turns on the cube using the turn method
        for move in alg:
            if '2' in move:
                rot = "dt"
            elif "'" in move:
                rot = "ccw"
            else:
                rot = "cw"
            face = move[0]

            self.cube_dict.update(general_turn(self.cube_dict, (face, rot)))

        self.algs_used.append(alg)

    def apply_turn(self, turn_tuple):
        # new configuration for the pieces that will turn
        self.algs_used.append(turn_tuple)
        cube_dict = self.cube_dict.copy()
        self.cube_dict.update(general_turn(cube_dict, turn_tuple))


class F2LSolverV4(BaseSolver):
    def __init__(self, cube: dict):
        super().__init__(cube)
        self.f2l_pairs = [
            ((0, 1, 0), ((1, 1, 0), ('r', 'y', 'g')), "Pair 1"),
            ((1, 0, 0), ((1, 0, -1), ('r', 'y', 'b')), "Pair 2"),
            ((0, -1, 0), ((-1, 0, -1), ('b', 'y', 'r')), "Pair 3"),
            ((-1, 0, 0), ((-1, 1, 0), ('g', 'y', 'w')), "Pair 4")
        ]
        self.algs_used = []
        self.solve()

    def solve(self):
        for pair in self.f2l_pairs:
            self.solve_f2l_pair(pair)

    def solve_f2l_pair(self, pair):
        edge_coord, edge_color = pair[0], pair[1][0]
        corner_coord, corner_colors = pair[0], pair[1][1]

        # Step 1: Place the edge in the correct position
        while self.cube_dict[edge_coord][2] != edge_color:
            self.apply_alg_std("U")

        if edge_coord[0] == 0:
            if edge_coord[2] == 1:
                self.apply_alg_std("F R U R' U' F'")
            else:
                self.apply_alg_std("R U R' U'")

        elif edge_coord[1] == 0:
            if edge_coord[0] == 1:
                self.apply_alg_std("U R U' R' U' F' U F")
            else:
                self.apply_alg_std("U' L' U L U F U' F'")

        else:
            if edge_coord[2] == 1:
                self.apply_alg_std("U F R U R' U' F'")

        # Step 2: Place the corner in the correct position and orientation
        while self.cube_dict[corner_coord] != corner_colors:
            self.apply_alg_std("U")

        if corner_coord == (0, 0, 1):
            if self.cube_dict[(1, 0, 1)][0] == corner_colors[0]:
                self.apply_alg_std("U' R U R' U' R U R'")
            else:
                self.apply_alg_std("R U R' U R U2 R'")

        elif corner_coord == (0, 1, 0):
            if self.cube_dict[(0, 0, 1)][2] == corner_colors[2]:
                self.apply_alg_std("U F' U' F U' F' U F")
            else:
                self.apply_alg_std("U' R U R' U' R U2 R'")

        else:
            if self.cube_dict[(0, 0, 1)][1] == corner_colors[1]:
                self.apply_alg_std("U' R U R' U' R U2 R' U' R U R'")
            else:
                self.apply_alg_std("U2 F R' F' R U2 R U R' U' R U R' U' F' U F")

    def apply_alg_std(self, alg: str):
        # Format the alg string into the notation used in the TURN_MAPPING_DICT
        alg = alg.split(' ')
        # Apply the turns on the cube using the turn method
        for move in alg:
            if '2' in move:
                rot = "dt"
            elif "'" in move:
                rot = "ccw"
            else:
                rot = "cw"
            face = move[0]

            self.cube_dict.update(general_turn(self.cube_dict, (face, rot)))

        self.algs_used.append(alg)

    def apply_turn(self, turn_tuple):
        # new configuration for the pieces that will turn
        self.algs_used.append(turn_tuple)
        cube_dict = self.cube_dict.copy()
        self.cube_dict.update(general_turn(cube_dict, turn_tuple))