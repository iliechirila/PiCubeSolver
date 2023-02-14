import math
from itertools import product
from Turns import TURN_DICT, X, Y, Z, ORIENTATION, TARGET_AXIS, CW


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

    def process_string_list(self, cube_list: list):
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
            # Each orientation is either -1 or 1
            for orientation in range(0, 2):
                #
                pass
            if cubie[0] == 1:
                i, j, k = 3, abs(cubie[1] - 1), abs(cubie[2] - 1)
                cube_dict[cubie][0] = cube_split_by_rows[i][j][k]
            if cubie[0] == -1:
                i, j, k = 1, abs(cubie[1] - 1), cubie[2] + 1
                cube_dict[cubie][0] = cube_split_by_rows[i][j][k]
            if cubie[1] == 1:
                i, j, k = 0, cubie[2] + 1, cubie[0] + 1
                cube_dict[cubie][1] = cube_split_by_rows[i][j][k]
            if cubie[1] == -1:
                i, j, k = 5, abs(cubie[2] - 1), cubie[0] + 1
                cube_dict[cubie][1] = cube_split_by_rows[i][j][k]
            if cubie[2] == 1:
                i, j, k = 2, abs(cubie[1] - 1), cubie[0] + 1
                cube_dict[cubie][2] = cube_split_by_rows[i][j][k]
            if cubie[2] == -1:
                i, j, k = 4, abs(cubie[1] - 1), abs(cubie[0] - 1)
                cube_dict[cubie][2] = cube_split_by_rows[i][j][k]

        return cube_dict

    def apply_alg(self, alg: str):
        pass

    def turn(self, rot_type: str, face: str):
        # new configuration for the pieces that will turn
        new_config = {}
        relevant_axis = ORIENTATION[face][0]
        orientation = ORIENTATION[face][1]
        perm = TURN_DICT[rot_type][face]
        cube_dict = self.cube_dict.copy().items()


        if relevant_axis is None:
            raise Exception(f"{face} is not a valid move notation.")

        for cubie, colors in cube_dict:
            # find the relevant cubies by axis and orientation
            if cubie[relevant_axis] == orientation:

                key = [None, None, None]
                key[perm[X][TARGET_AXIS]] = math.prod(perm[X])*cubie[X]
                key[perm[Y][TARGET_AXIS]] = math.prod(perm[Y])*cubie[Y]
                key[perm[Z][TARGET_AXIS]] = math.prod(perm[Z])*cubie[Z]
                val = [None, None, None]
                val[perm[X][TARGET_AXIS]] = colors[X]
                val[perm[Y][TARGET_AXIS]] = colors[Y]
                val[perm[Z][TARGET_AXIS]] = colors[Z]
                new_config[tuple(key)] = val
        self.cube_dict.update(new_config)






if __name__ == '__main__':
    # For scramble: L' D2 B' L2 U2 B R2 D2 U2 F2 U2 F2 L' R2 D' L R2 F' R
    cubestring = ['rowwwoyry', 'wrbwowgrb', 'rbgbggwgr', 'oboorbyry', 'gybybobwr', 'oygyygwgo']
    cube = Cube(cubestring)
    cube.turn(CW, "U")
    print(cube.cube_dict)
