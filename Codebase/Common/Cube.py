from Face import Face

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
    
    """

    def __init__(self, cube_string:str):
        # process the cube_string into the 6 faces
        self.faces = []
        self.process_string(cube_str=cube_string)

    def __str__(self):
        str = ''
        for face in self.faces:
            str = str + face.__str__()
        return str

    def process_string(self, cube_str:str):
        cube_centers = list(cube_str[i] for i in [4,13,22,31,40,49])
        if len(set(cube_centers)) != 6:
            raise Exception(f"Centers of the cube are not mapped correctly: {cube_centers}")
        # Split the string into substrings of len 9 to create the Faces of the cube
        n = 9
        faces_substrings = [cube_str[i:i+n] for i in range(0, len(cube_str), n)]

        self.faces = [Face(face_string = face_str, center = face_str[4]) for face_str in faces_substrings]


if __name__ == '__main__':
    cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
    cube = Cube(cube_string=cubestring)
    print(cube)
