
from Variables import colors_dict
import numpy as np

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

class Face:
    
    """
    A face of the cube contains 9 cubies, stored in a matrix of 3x3.      
    """
    def __init__(self, face_string:str, center:str, orientation: tuple):
        self.face_matrix = None
        # TODO self.face_matrix_str = None
        self.center = center
        self.process_string(face_string)
        self.adjacent_rows = np.empty((4,3))
        print(self.adjacent_rows)

    def __str__(self):
        return f"Face {self.center}:\n{self.face_matrix}\n\n{self.adjacent_rows}"

    def process_string(self,face:str):
        """
        Transforms a string of characters into a matrix, mapping
        the letters to integers according to colors_dict
        """
        if len(face) != 9:
            raise Exception(f"Face {self.center} was give a string of size {len(face)} instead of 9.")
        
        face = [
            colors_dict[color] for color in list(face)
        ]   
        
        self.face_matrix = np.array(face).reshape([3,3])        

    def rotate_clockwise(self, rotations: int = 1):
        # rotates the face matrix clockwise
        self.face_matrix = np.rot90(self.face_matrix,k=rotations,axes=(1,0))
        self.adjacent_rows[TOP], self.adjacent_rows[RIGHT], self.adjacent_rows[BOTTOM], self.adjacent_rows[LEFT] = self.adjacent_rows[LEFT], self.adjacent_rows[TOP], self.adjacent_rows[RIGHT], self.adjacent_rows[BOTTOM]


    def set_adjacent_rows(self, top:np.array, right:np.array, bottom:np.array, left:np.array):
        self.adjacent_rows[TOP,:] = top
        self.adjacent_rows[RIGHT,:] = right
        self.adjacent_rows[BOTTOM,:] = bottom
        self.adjacent_rows[LEFT,:] = left


if __name__ == '__main__':
    face = Face(face_string="UUUUUUUUU", center = "U", orientation=(0,0,1))
    face2 = Face(face_string="UBBBULFFF", center = "B",orientation=(0,-1,0))
    
    face.set_adjacent_rows(top = [0,0,0], right = [1,1,1], left = [2,2,2], bottom = [3,3,3])

    print(face)
    face.rotate_clockwise()
    print(face)


    print("This is gonna be awesome!")