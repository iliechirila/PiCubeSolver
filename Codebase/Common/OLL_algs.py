oll_algs = {
    # "Dummy": [
    #     {(-1, 1, -1): (False, False, False), (0, 1, -1): (False, False, False), (1, 1, -1): (False, False, False),
    #      (-1, 1, 0): (False, False, False), (1, 1, 0): (False, False, False),
    #      (-1, 1, 1): (False, False, False), (0, 1, 1): (False, False, False), (1, 1, 1): (False, False, False)},
    #     "REEEEEEEEEEEE"
    # ],
    "OLL 29 - Spotted Chameleon": [ #OK
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U' R U' R' F' U' F R U R'"
    ],
    "OLL 30 - Anti-Spotted Chameleon": [ #OK
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, False, True), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F R' F R2 U' R' U' R U R' F2"
    ],
    "OLL 41 - Awkward Fish, Dalmation": [ #OK
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U R U2 R' F R U R' U' F'"
    ],
    "OLL 42 - Lefty Awkward Fish, Anti-Dalmation": [ #OK
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R' U' R U' R' U2 R F R U R' U' F'"
    ],
    "OLL 39 - Fung": [ #OK
        {(-1, 1, -1):(False, False, True), (0, 1, -1):(False, False, True), (1, 1, -1):(False, True, False),
         (-1, 1, 0):(False, True, False),                        (1, 1, 0):(False, True, False),
         (-1, 1, 1):(False, True, False), (0, 1, 1):(False, False, True), (1, 1, 1):(True, False, False)},
        "L F' L' U' L U F U' L'"
    ],
    "OLL 40 - Anti-Fung": [ #OK
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R' F R U R' U' F' U R"
    ],
    "OLL 34 - City (C and T)": [ #OK
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R2 U' R' F R U R U' F'"
    ],
    "OLL 46 - Seein' Headlights (C and headlights)": [ #OK
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R' U' R' F R F' U R"
    ],
    "OLL 28 - Stealth, Arrow, Arrowhead, Fish": [ #OK
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F R U R' U' F' U2 F R U R' U' F'"
    ],
    "OLL 57 - Mummy, H, I, Brick": [ #OK
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U' L R' F R F' L'" # adapted so it does not contain slices or wide moves
    ],
    "OLL 21 - H, Double Sune, Cross": [ #OK
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R U R' U R U' R' U R U2 R'"
    ],
    "OLL 22 - Pi": [ #OK
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R U2 R2 U' R2 U' R2 U2 R"
    ],
    "OLL 23 - Headlights, Superman": [ #OK
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "R2 D' R U2 R' D R U2 R"
    ],
    "OLL 24 - T, Chameleon": [ #OK
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "L F R' F' L' F R F'"
    ],
    "OLL 25 - L, Triple-Sune": [ #ok
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "R U R' U R U' R' U R U' R' U R U2 R'"
    ],
    "OLL 26 - S-, Antisune": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "L' U' L U' L' U2 L"
    ],
    "OLL 27 - Sune": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R U R' U R U2 R'"
    ],
    "OLL 1 - Blank": [ #ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R U2 R2 F R F' U2' R' F R F'"
    ],
    "OLL 2 - Zamboni": [# ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "F R U R' U' F' B U L U' L' B'"
    ],
    "OLL 3 - Anti-Mouse": [ #ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "B U L U' L' B' U' F R U R' U' F'"
    ],
    "OLL 4 - Mouse": [ # ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "B U L U' L' B' U F R U R' U' F'"
    ],
    "OLL 17 - Diagonal": [ #OK
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U R' F R F' U2 R' F R F'"
    ],
    "OLL 18 - Crown": [ #OK
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U2 R2 F R F' U2 L R' F R F' L'"
    ],
    "OLL 19 - Bunny": [ #okcred
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "F R U R' U' F' R U2 R2 F R F' R U2 R'"
    ],
    "OLL 20 - X, Checkers": [ #cool
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "L' R B R B R' B' L2 R2 F R F' L'"
    ],
    "OLL 9 - Kite": [ #cool
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
    "OLL 35 - Fish Salad": [#ok
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (False, True, False)},
        "R U2 R2 F R F' R U2 R'"
    ],
    "OLL 37 - Mounted Fish": [#ok
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F R' F' R U R U' R'"
    ],
    "OLL 51 - Bottlecap": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "F U R U' R' U R U' R' F'"
    ],
    "OLL 52 - Rice Cooker": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R U R' U R U' B U' B' R'"
    ],
    "OLL 55 - Highway": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R U2 R2 U' R U' R' U2 F R F'"
    ],
    "OLL 56 - Streetlights": [ #ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "L F L' U R U' R' U R U' R' L F' L'"
    ],
    "OLL 13 - Trigger": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "F U R U' R2 F' R U R U' R'"
    ],
    "OLL 14 - Anti-Trigger": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R' F R U R' F' R F U' F'"
    ],
    "OLL 15 - Squeegee": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "L' B' L R' U' R U L' B L"
    ],
    "OLL 16 - Anti-Squeegee": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R B R' L U L' U' R B' R'"
    ],
    "OLL 31 - P Shape": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R' U' F U R U' R' F' R"
    ],
    "OLL 32 - P Shape": [#ok
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "L U F' U' L' U L F L'"
    ],
    "OLL 43 - P Shape": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F' U' L' U L F"
    ],
    "OLL 44 - P Shape": [#ok
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "F U R U' R' F'"
    ],
    "OLL 47 - Anti-Breakneck": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R' U' R' F R F' R' F R F' U R"
    ],
    "OLL 48 - Breakneck": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "F R U R' U' R U R' U' F'"
    ],
    "OLL 49 - Right back squeezy": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "R B' R2 F R2 B R2 F' R"
    ],
    "OLL 50 - Right front squeezy": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R B' R B R2' U2 F R' F' R"
    ],
    "OLL 53 - Frying Pan": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "F R U R' U' F' R U R' U' R' F R F'"
    ],
    "OLL 54 - Anti-Frying Pan": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "F' L' U' L U L' U L U' L' U' L F"
    ],
    "OLL 7 - Wide Sune": [#ok
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "F R' F' R U2 R U2 R'"
    ],
    "OLL 8 - Left Wide Sune (LWS)": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U2 R' U2 R' F R F'"
    ],
    "OLL 11 - Downstairs": [#ok
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, False, True), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, True, False), (1, 1, 1): (False, False, True)},
        "R U' R' U' R U' R' U2 F' U F U' R U R'"
    ],
    "OLL 12 - Upstairs": [#ok
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, True, False), (1, 1, 1): (True, False, False)},
        "F R U R' U' F' U F R U R' U' F'"
    ],
    "OLL 5": [ #OK
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (True, False, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, False, True)},
        "R' F2 L F L' F R"
    ],
    "OLL 6": [ #OK
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "L F2 R' F' R F' L'"
    ],
    "OLL 33 - Key": [#OK
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (False, False, True), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "R U R' U' R' F R F'"
    ],
    "OLL 45 - T": [#OK
        {(-1, 1, -1): (True, False, False), (0, 1, -1): (False, False, True), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "F R U R' U' F'"
    ],
    "OLL 36 - Wario": [#OK
        {(-1, 1, -1): (False, True, False), (0, 1, -1): (False, True, False), (1, 1, -1): (False, False, True),
         (-1, 1, 0): (True, False, False), (1, 1, 0): (False, True, False),
         (-1, 1, 1): (True, False, False), (0, 1, 1): (False, False, True), (1, 1, 1): (False, True, False)},
        "L' U' L U' L' U L U L F' L' F"
    ],
    "OLL 38 - Mario": [#OK
        {(-1, 1, -1): (False, False, True), (0, 1, -1): (False, True, False), (1, 1, -1): (False, True, False),
         (-1, 1, 0): (False, True, False), (1, 1, 0): (True, False, False),
         (-1, 1, 1): (False, True, False), (0, 1, 1): (False, False, True), (1, 1, 1): (True, False, False)},
        "R U R' U R U' R' U' R' F R F'"
    ],
}
