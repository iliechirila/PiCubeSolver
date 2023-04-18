oll_algs = {
    # "Dummy": [
    #     {(-1, 1, -1): (False, False, False), (0, 1, -1): (False, False, False), (1, 1, -1): (False, False, False),
    #      (-1, 1, 0): (False, False, False), (1, 1, 0): (False, False, False),
    #      (-1, 1, 1): (False, False, False), (0, 1, 1): (False, False, False), (1, 1, 1): (False, False, False)},
    #     "REEEEEEEEEEEE"
    # ],
    "OLL 29 - Spotted Chameleon": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U' R U' R' F' U' F R U R'"
    ],
    "OLL 30 - Anti-Spotted Chameleon": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, False, True), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F R' F R2 U' R' U' R U R' F2"
    ],
    "OLL 41 - Awkward Fish, Dalmation": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U R U2 R' F R U R' U' F'"
    ],
    "OLL 42 - Lefty Awkward Fish, Anti-Dalmation": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R' U' R U' R' U2 R F R U R' U' F'"
    ],
    "OLL 39 - Fung": [
        {(-1, 1, -1):(False, False, True), (0, 1, -1):(False, False, True), (1, 1, -1):(False, True, False),
         (-1, 1, 0):(False, True, False),                        (1, 1, 0):(False, True, False),
         (-1, 1, 1):(False, True, False), (0, 1, 1):(False, False, True), (1, 1, 1):(True, False, False)},
        "L F' L' U' L U F U' L'"
    ],
    "OLL 40 - Anti-Fung": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R' F R U R' U' F' U R"
    ],
    "OLL 34 - City (C and T)": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R2 U' R' F R U R U' F'"
    ],
    "OLL 46 - Seein' Headlights (C and headlights)": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R' U' R' F R F' U R"
    ],
    "OLL 28 - Stealth, Arrow, Arrowhead, Fish": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "F R U R' U' F' U2 F R U R' U' F'"
    ],
    "OLL 57 - Mummy, H, I, Brick": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U' L R' F R F' L'" # adapted so it does not contain slices or wide moves
    ],
    "OLL 21 - H, Double Sune, Cross": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R U R' U R U' R' U R U2 R'"
    ],
    "OLL 22 - Pi": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R U2 R2 U' R2 U' R2 U2 R"
    ],
    "OLL 23 - Headlights, Superman": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "R2 D' R U2 R' D R U2 R"
    ],
    "OLL 24 - T, Chameleon": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "L F R' F' L' F R F'"
    ],
    "OLL 25 - L, Triple-Sune": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "R U R' U R U' R' U R U' R' U R U2 R'"
    ],
    "OLL 26 - S-, Antisune": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "R' U L U' R U L'"
    ],
    "OLL 27 - Sune": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R U R' U R U2 R'"
    ],
    "OLL 1 - Blank": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R U2 R2 F R F' U2' R' F R F'"
    ],
    "OLL 2 - Zamboni": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "F (R U R' U') F' B U L U' L' B'"
    ],
    "OLL 3 - Anti-Mouse": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "B U L U' L' B' U' F R U R' U' F'"
    ],
    "OLL 4 - Mouse": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "B U L U' L' B' U F R U R' U' F'"
    ],
    "OLL 17 - Diagonal": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U R' F R F' U2 R' F R F'"
    ],
    "OLL 18 - Crown": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U2 R2 F R F' U2 L R' F R F' L'"
    ],
    "OLL 19 - Bunny": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "L' R B R B R' B' L' R R' D R D'"
    ],
    "OLL 20 - X, Checkers": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "L' R B R B R' B' L2 R2 F R F' L'"
    ],
    "OLL 9 - Kite": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U' R' F R2 U R' U' F'"
    ],
    "OLL 10 - Anti-Kite": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R U R' U R' F R F' R U2 R'"
    ],
    "OLL 35 - Fish Salad": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "R U2 R2 F R F' R U2 R'"
    ],
    "OLL 37 - Mounted Fish": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F R' F' R U R U' R'"
    ],
    "OLL 51 - Bottlecap": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "F U R U' R' U R U' R' F'"
    ],
    "OLL 52 - Rice Cooker": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R U R' U R U' B U' B' R'"
    ],
    "OLL 55 - Highway": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R U2 R2 U' R U' R' U2 F R F'"
    ],
    "OLL 56 - Streetlights": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "L F L' U R U' R' U R U' R' L F' L'"
    ],
    "OLL 13 - Trigger": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "F U R U' R2 F' R U R U' R'"
    ],
    "OLL 14 - Anti-Trigger": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R' F R U R' F' R F U' F'"
    ],
    "OLL 15 - Squeegee": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "L' B' L R' U' R U L' B L"
    ],
    "OLL 16 - Anti-Squeegee": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R B R' L U L' U' R B' R'"
    ],
    "OLL 31 - P Shape": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R' U' F U R U' R' F' R"
    ],
    "OLL 32 - P Shape": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "L U F' U' L' U L F L'"
    ],
    "OLL 43 - P Shape": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F' U' L' U L F"
    ],
    "OLL 44 - P Shape": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "F U R U' R' F'"
    ],
    "OLL 47 - Anti-Breakneck": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R' U' R' F R F' R' F R F' U R"
    ],
    "OLL 48 - Breakneck": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "F R U R' U' R U R' U' F'"
    ],
    "OLL 49 - Right back squeezy": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R B' R2 F R2 B R2 F' R"
    ],
    "OLL 50 - Right front squeezy": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R B' R B R2' U2 F R' F' R"
    ],
    "OLL 53 - Frying Pan": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "F R U R' U' F' R U R' U' R' F R F'"
    ],
    "OLL 54 - Anti-Frying Pan": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "L B R' B R B' R' B R B2 L'"
    ],
    "OLL 7 - Wide Sune": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "F R' F' R U2 R U2 R'"
    ],
    "OLL 8 - Left Wide Sune (LWS)": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U2 R' U2 R' F R F'"
    ],
    "OLL 11 - Downstairs": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R U' R' U' R U' R' U2 F' U F U' R U R'"
    ],
    "OLL 12 - Upstairs": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "F R U R' U' F' U F R U R' U' F'"
    ],
    "OLL 5": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "R' B2 L B L' B R"
    ],
    "OLL 6": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R B2 L' B' L B' R'"
    ],
    "OLL 33 - Key": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U' R' F R F'"
    ],
    "OLL 45 - T": [
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F R U R' U' F'"
    ],
    "OLL 36 - Wario": [
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "L' U' L U' L' U L U L F' L' F"
    ],
    "OLL 38 - Mario": [
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R U R' U R U' R' U' R' F R F'"
    ],
}
