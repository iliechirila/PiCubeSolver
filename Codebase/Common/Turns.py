########################################################################
# File containing the dictionaries that help apply the turns on the cube
########################################################################

"""
The logic:
Each piece has a number of max 3 faces, each with their orientation.
When making a turn, we not only want to move the pieces to other coordinates, but reorient them.

There are 2 (3) possible ways to turn: clockwise (cw), counterclockwise (ccw) (and double turn (dt)). For each type of
turn, we have 6 faces that can turn. Then, we have 3 coordinates where we store a tuple:
(a,b) -> a tells on what axis the color on the (current) axis will go
      -> b tells how the relative orientation will change (+1 -> -1; -1 -> +1)
* Axis indices: x-0, y-1, z-2
Example:
     When doing a cw U:
     0) (1, -1) -> the color on the current x-axis will go on the y-axis, and invert the sign
     1) (0, 1)  -> the color on the current y-axis will go on the x-axis, and maintain the sign
     2) (1, 1)  -> the color on the current z-axis will stay on the z-axis, and maintain the sign
"""
TURN_DICT = {
    "cw": {
        "U": [(1, -1), (0, 1), (2, 1)], "D": [(1, 1), (0, -1), (2, 1)],
        "R": [(0, 1), (2, 1), (1, -1)], "L": [(0, 1), (2, -1), (1, 1)],
        "F": [(2, -1), (1, 1), (0, 1)], "B": [(2, 1), (1, 1), (0, -1)]
    },
    "ccw": {
        "U": [(1, 1), (0, -1), (2, 1)], "D": [(1, -1), (0, 1), (2, 1)],
        "R": [(0, 1), (2, -1), (1, 1)], "L": [(0, 1), (2, 1), (1, -1)],
        "F": [(2, 1), (1, 1), (0, -1)], "B": [(2, -1), (1, 1), (0, 1)]
    }
}

CW = "cw"
CCW = "ccw"
TARGET_AXIS = 0
TARGET_REORIENTATION = 1
X, Y, Z = 0, 1, 2

ORIENTATION = {
    "U": (Z, 1), "R": (X, 1), "F": (Y, 1),
    "D": (Z, -1), "L": (X, -1), "B": (Y, -1)
}