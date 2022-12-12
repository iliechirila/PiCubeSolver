###################################3
"""
File containing enums used to ease access to faces, colors, cubies.
"""

from enum import IntEnum

colors_dict = {
    "U":0,
    "R":1,
    "F":2,
    "D":3,
    "L":4,
    "B":5
}

class Color(IntEnum):
    """ The possible colors of the cube facelets. Color U refers to the color of the U(p)-face etc.
    Also used to name the faces itself."""
    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5

class Corner(IntEnum):
    """The names of the corner positions of the cube. Corner URF e.g. has an U(p), a R(ight) and a F(ront) facelet."""
    URF = 0
    UFL = 1
    ULB = 2
    UBR = 3
    DFR = 4
    DLF = 5
    DBL = 6
    DRB = 7

class Edge(IntEnum):
    """The names of the edge positions of the cube. Edge UR e.g. has an U(p) and R(ight) facelet."""
    UR = 0
    UF = 1
    UL = 2
    UB = 3
    DR = 4
    DF = 5
    DL = 6
    DB = 7
    FR = 8
    FL = 9
    BL = 10
    BR = 11


class Move(IntEnum):
    """The moves in the faceturn metric. Not to be confused with the names of the facelet positions in class Facelet."""
    U1 = 0
    U2 = 1
    U_prime = 2
    R1 = 3
    R2 = 4
    R_prime = 5
    F1 = 6
    F2 = 7
    F_prime = 8
    D1 = 9
    D2 = 10
    D_prime = 11
    L1 = 12
    L2 = 13
    L_prime = 14
    B1 = 15
    B2 = 16
    B_prime = 17
