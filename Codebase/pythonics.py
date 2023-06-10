
def find_cube_orientation(up_color: str, front_color: str):
    W, O, G, R, B, Y = 'W', 'O', 'G', 'R', 'B', 'Y'
    look_up_dict = {
        W: [B, O, G, R],
        O: [W, B, Y, G],
        G: [W, O, Y, R],
        R: [W, G, Y, B],
        B: [W, R, Y, O],
        Y: [G, O, B, R]
    }
    look_up_index = {
        0: 3,
        1: 0,
        2: 1,
        3: 2,
    }
    opposite_colors = {W: Y, Y: W, R: O, O: R, G: B, B: G}
    index_up_to_front = look_up_dict[up_color].index(front_color)
    index_left = look_up_index[index_up_to_front]
    left_color = look_up_dict[up_color][index_left]

    return up_color, left_color, front_color, opposite_colors[left_color], opposite_colors[front_color], opposite_colors[up_color]



my_string = "wwwwwwwww"
index = 4  # Index of the character to replace
replacement = 'X'  # Character to replace with

new_string = my_string[:index] + replacement + my_string[index + 1:]

print(new_string)

# print(find_cube_orientation('R', 'G'))