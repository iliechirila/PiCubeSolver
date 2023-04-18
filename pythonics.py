from itertools import permutations

from Codebase.Common.Cube import Cube
from Codebase.Solvers.CrossSolver import choose_valid_turns
# color = ['r','b','g']
# # perm = frozenset(map(''.join, permutations(color)))
# perm = permutations(color)
# color2 =  ['b','g','r']
# # perm2 = frozenset(map(''.join, permutations(color2)))
# perm2 = permutations(color2)
#
# print(color != color2)
# def _cubie_key(color):
#     return frozenset(map(''.join, permutations(color)))
# f2l_pair = 'gr'
# d_color = 'y'
# cube = Cube()
# goal_perm = cube.cube_dict
# f2l_key = [_cubie_key(f2l_pair),
#                    _cubie_key(f2l_pair + d_color)]
# # slot_coord = tuple(goal_perm[f2l_key[0]][0])
#
# print(tuple("abs"))
#
# # print("whot")
#
# print(f2l_key)
# i = "i"
# j = "j"

# for l in range(4):
#     for k in range(3):
#         if k == 2:
#             break
#         print(i, l, j, k)
# front = "green"
# back  = "blue"
# right = "red"
# my_dict = {(0,0,1): [front, back, right]}
# print(my_dict)
# front = "white"
# print(my_dict)


my_list = ['', 'g', '']
result = next((s for s in my_list if s), None)
print(result)  # Output: "g"