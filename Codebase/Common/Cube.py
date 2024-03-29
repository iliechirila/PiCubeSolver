from itertools import product

# from matplotlib import pyplot as plt

from Common.Turns import TURN_MAPPING_DICT, X, Y, Z, ORIENTATION, TARGET_AXIS, TARGET_REORIENTATION, CCW, DT

import numpy as np

class Cube:
    """
    The cube contains 6 faces: 6 centers, 12 edges and 8 corners. 
    The number of small cubies is 54 (9 on each face)

                  |************|
                  |*U1**U2**U3*|
                  |************|
                  |*U4**U5**U6*|
                  |************|
                  |*U7**U8**U9*|
                  |************|
     |************|************|************|************|
     |*L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*|
     |************|************|************|************|
     |*L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*|
     |************|************|************|************|
     |*L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*|
     |************|************|************|************|
                  |************|
                  |*D1**D2**D3*|
                  |************|
                  |*D4**D5**D6*|
                  |************|
                  |*D7**D8**D9*|
                  |************|
    
    The initial plan was to store the cubies colors and positions in a different class called Face, but a 
    more friendly approach would be to store the coordinates of a piece in a 3-dimensional coordinate frame.
    Thus, a piece would have a position of (x,y,z).
    
    Center piece -> 2 zeros and a value of 1 or -1
    Edge piece -> 1 zero and 2 values of 1 or -1
    Corner piece -> 0 zeros and 3 values of 1 or -1

    At coordinates (0,0,0) is the core of the cube, so there is no piece. It will not be considered.
    
    """

    def __init__(self, faces_strings: list = 0):
        """
        For easier processing, the cube will receive a list of 6 elements, each element being a string of 
        9 characters describing each face of the cube. The standard face notation order is: U, L, F, R, B, D.
        White is assumed to be on the Up face. Green on front.
        """
        # process the cube_string into the 6 faces
        self.cube_dict = self.process_string_list(cube_list=faces_strings)

    @staticmethod
    def process_string_list(cube_list: list):
        if cube_list == 0:
            cube_list = ["wwwwwwwww", "ooooooooo", "ggggggggg", "rrrrrrrrr", "bbbbbbbbb", "yyyyyyyyy"]
        else:
            # Check if the centers of the cube are mapped correctly
            # Each face is a list of each 9-characters, then the center is at the 5th char, so index 4
            cube_centers = list(face[4] for face in cube_list)
            if len(set(cube_centers)) != 6:
                raise Exception(f"Centers of the cube are not mapped correctly: {cube_centers}")

        # Prepare coordinates to give them colors
        c = range(-1, 2)
        cube_dict = {coord: ['', '', ''] for coord in list(product(c, repeat=3))}
        cube_dict.pop((0, 0, 0))

        # Split the faces strings into rows for more accesibility in the next step
        # 'abcdefghi' -> ['abc','def','ghi']
        cube_split_by_rows = []
        for face_str in cube_list:
            n = 3
            chunks = [face_str[i:i + n] for i in range(0, len(face_str), n)]
            cube_split_by_rows.append(chunks)

        # Assign colors at each coordinate and depending on orientations
        # Orientation matters a lot. We ignore the orientations 0 (there is nothing to assign there)
        # Axis are the following (chosen using the right hand rule):
        # X axis: Red   (pos), Orange (neg)
        # Y axis: White (pos), Yellow (neg)
        # Z axis: Green (pos), Blue   (neg)
        def get_color_from_coordinates_X(cubie):
            # Case Orange face -> X == -1
            # Case Red face -> X == 1
            pass

        def get_color_from_coordinates_Y(cubie):
            # Case Yellow face -> Y == -1
            # Case White face -> Y == 1
            pass

        def get_color_from_coordinates_Z(cubie):
            # Case Blue face -> Z == -1
            # Case Green face -> Z == 1
            pass

        # Reverse search: we find the colors using the coordinates mapping them to the colors matrix
        for cubie in cube_dict:
            if cubie[X] == 1:
                i, j, k = 3, abs(cubie[Y] - 1), abs(cubie[Z] - 1)
                cube_dict[cubie][0] = cube_split_by_rows[i][j][k]
            if cubie[X] == -1:
                i, j, k = 1, abs(cubie[Y] - 1), cubie[Z] + 1
                cube_dict[cubie][0] = cube_split_by_rows[i][j][k]
            if cubie[Y] == 1:
                i, j, k = 0, cubie[Z] + 1, cubie[X] + 1
                cube_dict[cubie][1] = cube_split_by_rows[i][j][k]
            if cubie[Y] == -1:
                i, j, k = 5, abs(cubie[Z] - 1), cubie[X] + 1
                cube_dict[cubie][1] = cube_split_by_rows[i][j][k]
            if cubie[Z] == 1:
                i, j, k = 2, abs(cubie[Y] - 1), cubie[X] + 1
                cube_dict[cubie][2] = cube_split_by_rows[i][j][k]
            if cubie[Z] == -1:
                i, j, k = 4, abs(cubie[Y] - 1), abs(cubie[X] - 1)
                cube_dict[cubie][2] = cube_split_by_rows[i][j][k]

        return cube_dict

    def apply_alg_std(self, alg: str):
        # Format the alg string into the notation used in the TURN_MAPPING_DICT
        while alg[-1] == ' ':
            alg = alg[:len(alg)-1]
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
            # self.turn((rot, face))

    def apply_alg_tuple(self, alg: list):
        for move in alg:
            self.turn((move[0], move[1]))

    @staticmethod
    def format_alg_to_turns(alg: str):
        # Separates each move, taking into
        prev = ''
        alg_split = alg.split()
        turns = []
        for move in alg_split:
            face = move[0]
            direction = 'cw'
            if len(move) > 1:
                if move[1] == '2':
                    direction = 'dt'
                elif move[1] == "'":
                    direction = 'ccw'
            turns.append((face, direction))
        return turns

    @staticmethod
    def format_turns_to_alg(alg: list):
        result = ''
        for face, rot_type in alg:
            rot_str = ''
            if rot_type == CCW:
                rot_str = '\''
            elif rot_type == DT:
                rot_str = '2'
            result = result + face + rot_str + ' '

        return result



    def turn(self, turn_tuple):
        # new configuration for the pieces that will turn
        face, rot_type = turn_tuple
        new_config = {}
        relevant_axis = ORIENTATION[face][0]
        orientation = ORIENTATION[face][1]
        perm = TURN_MAPPING_DICT[rot_type][face]
        cube_dict = self.cube_dict.copy().items()

        if relevant_axis is None:
            raise Exception(f"{face} is not a valid move notation.")

        for cubie, colors in cube_dict:
            # find the relevant cubies by axis and orientation
            if cubie[relevant_axis] == orientation:
                key = [None, None, None]
                key[perm[X][TARGET_AXIS]] = perm[X][TARGET_REORIENTATION] * cubie[X]
                key[perm[Y][TARGET_AXIS]] = perm[Y][TARGET_REORIENTATION] * cubie[Y]
                key[perm[Z][TARGET_AXIS]] = perm[Z][TARGET_REORIENTATION] * cubie[Z]
                val = [None, None, None]
                val[perm[X][TARGET_AXIS]] = colors[X]
                val[perm[Y][TARGET_AXIS]] = colors[Y]
                val[perm[Z][TARGET_AXIS]] = colors[Z]
                new_config[tuple(key)] = val

        self.cube_dict.update(new_config)

    # def graph_cube(self, gap_color='k', gap_width=2, bg_color='w',
    #                w='ghostwhite', y='gold', g='forestgreen',
    #                b='midnightblue', r='crimson', o='darkorange'):
    #     """
    #     Graphs the cube for easy visualization with optional arguments for
    #     visual preference

    #     Parameters:
    #     gap_color - (default 'k') The color of the gap between all of the
    #                  stickers
    #     gap_width - (default 2) The width of the gap between of the stickers.
    #     bg_color - (default 'w') The background color of the plot
    #     w - (default ghostwhite) The color of the white stickers
    #     y - (default gold) The color of the yellow stickers
    #     g - (default forestgreen) The color of the green stickers
    #     b - (default midnightblue) The color of the blue stickers
    #     r - (default crimson) The color of the red stickers
    #     o - (default darkorange) The color of the orange stickers
    #     """
    #     X, Y = np.meshgrid([0, 1], [0, 1])
    #     Z = np.array([[0.5, 0.5], [0.5, 0.5]])

    #     # Creating the color scheme for each cubie
    #     colors = {'w': w, 'y': y, 'g': g, 'b': b, 'r': r, 'o': o, '': ''}
    #     perm_colors = {}
    #     for cubie in self.cube_dict:
    #         c = self.cube_dict[cubie]
    #         perm_colors[cubie] = [colors[c[0]], colors[c[1]], colors[c[2]]]

    #     # Create figure for plot
    #     fig = plt.figure()
    #     ax = fig.add_subplot(111, projection='3d')
    #     ax.set_xlim(-1, 2)
    #     ax.set_ylim(-1, 2)
    #     ax.set_zlim(-1, 2)
    #     ax.set_facecolor(bg_color)
    #     ax.axis('off')

    #     # Will create square of appropriate color at appropriate coordinate
    #     for cubie in perm_colors:
    #         if cubie[0] != 0:
    #             ax.plot_surface(Y + cubie[2], Z + cubie[0] * 1.5, X + cubie[1],
    #                             edgecolors=gap_color, linewidth=gap_width,
    #                             color=perm_colors[cubie][0])
    #         if cubie[1] != 0:
    #             ax.plot_surface(Y + cubie[2], X + cubie[0], Z + cubie[1] * 1.5,
    #                             edgecolors=gap_color, linewidth=gap_width,
    #                             color=perm_colors[cubie][1])
    #         if cubie[2] != 0:
    #             ax.plot_surface(Z + cubie[2] * 1.5, X + cubie[0], Y + cubie[1],
    #                             edgecolors=gap_color, linewidth=gap_width,
    #                             color=perm_colors[cubie][2])

    #     plt.show()

def general_turn(cube_dict, turn_tuple):
    """
    Returns a new configuration for the cubies on the layer that will be turned.
    To be used together with the update built-in method for main cube dictionaries.

    Parameters:
    cube_dict - Current configuration of the cubies.
    turn_tuple - Tuple formed by the rotation type (cw, ccw, dt) and the face that will turn (U, F, D, B, R, L)

    Returns:
    new_config - dict containing information about cubies that changed
    """
    # new configuration for the pieces that will turn
    face, rot_type = turn_tuple
    new_config = {}
    relevant_axis = ORIENTATION[face][0]
    orientation = ORIENTATION[face][1]
    perm = TURN_MAPPING_DICT[rot_type][face]

    if relevant_axis is None:
        raise Exception(f"{face} is not a valid move notation.")

    for cubie, colors in cube_dict.items():
        # find the relevant cubies by axis and orientation
        if cubie[relevant_axis] == orientation:
            key = [None, None, None]
            key[perm[X][TARGET_AXIS]] = perm[X][TARGET_REORIENTATION] * cubie[X]
            key[perm[Y][TARGET_AXIS]] = perm[Y][TARGET_REORIENTATION] * cubie[Y]
            key[perm[Z][TARGET_AXIS]] = perm[Z][TARGET_REORIENTATION] * cubie[Z]
            val = [None, None, None]
            val[perm[X][TARGET_AXIS]] = colors[X]
            val[perm[Y][TARGET_AXIS]] = colors[Y]
            val[perm[Z][TARGET_AXIS]] = colors[Z]
            new_config[tuple(key)] = val
        else:
            new_config[cubie] = colors

    # Returns the cubies that change orientation
    return new_config


