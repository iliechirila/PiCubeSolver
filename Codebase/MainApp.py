from Codebase.Common.Cube import Cube

"""
This is the main file where everything is supposed to run from at this point in time.
"""


if __name__ == '__main__':
    # For scramble: L' D2 B' L2 U2 B R2 D2 U2 F2 U2 F2 L' R2 D' L R2 F' R
    cubestring = ['rowwwoyry', 'wrbwowgrb', 'rbgbggwgr', 'oboorbyry', 'gybybobwr', 'oygyygwgo']
    cube = Cube()
    print(cube.cube_dict)
    cube.apply_alg("L' D2 B' L2 U2 B R2 D2 U2 F2 U2 F2 L' R2 D' L R2 F' R")
    # cube.turn("cw", "R")
    print(cube.cube_dict)
