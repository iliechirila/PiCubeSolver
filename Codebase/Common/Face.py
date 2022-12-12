
from Variables import colors_dict
import numpy as np


class Face:
    """
    A face of the cube contains 9 cubies, stored in a matrix of 3x3.      
    """
    def __init__(self, face_string:str, center:str):
        print(face_string)
        self.face_matrix = None
        self.face_matrix_str = None
        self.center = center
        self.process_string(face_string)

    def __str__(self):
        return f"Face {self.center}:\n{self.face_matrix}\n"

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
        



if __name__ == '__main__':
    face = Face(face_string="UBBBULFFFD", center = "U")
    face2 = Face(face_string="UBBBULFFF", center = "B")
    
    print("This is gonna be awesome!")