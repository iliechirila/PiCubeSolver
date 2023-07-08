def pll_algs_dict(top, front, left, back, right):
    pll_dict = {
        "Solved": [
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, back), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (right, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (right, top, front)},
            ""
        ],
        "H permutation": [ # OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, front), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (right, top, ''), (1, 1, 0): (left, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, back), (1, 1, 1): (right, top, front)},
            "R2 U2 R U2 R2 U2 R2 U2 R U2 R2"
        ],
        "U Permutation : a": [ # OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, left), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (right, top, ''), (1, 1, 0): (back, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (right, top, front)},
            "R2 U' R' U' R U R U R U' R"
        ],
        "U Permutation : b": [ #OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, right), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (back, top, ''), (1, 1, 0): (left, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (right, top, front)},
            "R' U R' U' R' U' R' U R U R2"
        ],
        "Z Permutation": [ # OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, left), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (back, top, ''), (1, 1, 0): (front, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, right), (1, 1, 1): (right, top, front)},
            "R' L F' R2 L2 B' R2 L2 F' R' L D2 R2 L2 U"
        ],
        "A Permutation : a": [ # OK
            {(-1, 1, -1): (back, top, right), (0, 1, -1): ('', top, back), (1, 1, -1): (front, top, right),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (right, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (left, top, back)},
            "R' U2 R2 U' L' U R' U' L U R' U2 R"
        ],
        "A Permutation : b": [ # OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, back), (1, 1, -1): (left, top, front),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (right, top, ''),
             (-1, 1, 1): (front, top, right), (0, 1, 1): ('', top, front), (1, 1, 1): (back, top, right)},
            "R B' R F2 R' B R F2 R2"
        ],
        "E Permutation": [ # OK
            {(-1, 1, -1): (back, top, right), (0, 1, -1): ('', top, back), (1, 1, -1): (back, top, left),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (right, top, ''),
             (-1, 1, 1): (front, top, right), (0, 1, 1): ('', top, front), (1, 1, 1): (front, top, left)},
            "R' U L' D2 L U' R L' U R' D2 R U' L"
        ],
        "F Permutation": [ # OK
            {(-1, 1, -1): (back, top, right), (0, 1, -1): ('', top, back), (1, 1, -1): (back, top, left),
             (-1, 1, 0): (right, top, ''), (1, 1, 0): (left, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (right, top, front)},
            "R' U R U' R2 F' U' F U R F R' F' R2 U'"
        ],
        "G Permutation: a": [ #OK?
            {(-1, 1, -1): (right, top, front), (0, 1, -1): ('', top, left), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (front, top, ''), (1, 1, 0): (right, top, ''),
             (-1, 1, 1): (back, top, left), (0, 1, 1): ('', top, back), (1, 1, 1): (front, top, left)},
            "R U2 R' U' F' R U R2 U' R' F R U R2 U2 R' U2"
        ],
        "G Permutation : b": [ #OK!
            {(-1, 1, -1): (front, top, left), (0, 1, -1): ('', top, front), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (back, top, ''), (1, 1, 0): (right, top, ''),
             (-1, 1, 1): (front, top, right), (0, 1, 1): ('', top, left), (1, 1, 1): (left, top, back)},
            "R' U' R U D' R2 U R' U R U' R U' R2 D U'"
        ],
        "G Permutation : c": [ #OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, right), (1, 1, -1): (left, top, front),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (front, top, ''),
             (-1, 1, 1): (front, top, right), (0, 1, 1): ('', top, back), (1, 1, 1): (back, top, right)},
            "L' U' L U L U' F' L' U' L' U L F U' L U2 L' U2"
        ],
        "G Permutation : d": [ # OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, front), (1, 1, -1): (front, top, right),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (back, top, ''),
             (-1, 1, 1): (right, top, back), (0, 1, 1): ('', top, right), (1, 1, 1): (front, top, left)},
            "R U2 R' U B' R' U' R U R B U R' U' R' U R U2"
        ],
        "J Permutation : a": [ #OK
            {(-1, 1, -1): (front, top, left), (0, 1, -1): ('', top, back), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (front, top, ''), (1, 1, 0): (right, top, ''),
             (-1, 1, 1): (back, top, left), (0, 1, 1): ('', top, left), (1, 1, 1): (right, top, front)},
            "L' U R' U2 L U' R U L' U R' U2 L U' R"
        ],
        "J Permutation : b": [ #OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, back), (1, 1, -1): (front, top, right),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (front, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, right), (1, 1, 1): (back, top, right)},
            "R U R' F' R U R' U' R' F R2 U' R' U'"
        ],
        "N Permutation : a": [ #OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, back), (1, 1, -1): (left, top, front),
             (-1, 1, 0): (right, top, ''), (1, 1, 0): (left, top, ''),
             (-1, 1, 1): (right, top, back), (0, 1, 1): ('', top, front), (1, 1, 1): (right, top, front)},
            "F' R U R' U' R' F R2 F U' R' U' R U F' R'"
        ],
        "N Permutation : b": [ #OK
            {(-1, 1, -1): (right, top, front), (0, 1, -1): ('', top, back), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (right, top, ''), (1, 1, 0): (left, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (left, top, back)},
            "R' U R U' R' F' U' F R U R' F R' F' R U' R"
        ],
        "R Permutation : a": [# OKK!!!!!
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, right), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (back, top, ''),
             (-1, 1, 1): (front, top, right), (0, 1, 1): ('', top, front), (1, 1, 1): (front, top, left)},
            "R U2 R' U2 R B' R' U' R U R B R2 U"
        ],
        "R Permutation : b": [ #OK
            {(-1, 1, -1): (back, top, right), (0, 1, -1): ('', top, back), (1, 1, -1): (back, top, left),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (front, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, right), (1, 1, 1): (right, top, front)},
            "R' U2 R U2 R' F R U R' U' R' F' R2' U'"
        ],
        "T Permutation": [ #OK
            {(-1, 1, -1): (left, top, back), (0, 1, -1): ('', top, back), (1, 1, -1): (front, top, right),
             (-1, 1, 0): (right, top, ''), (1, 1, 0): (left, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (back, top, right)},
            "R U R' U' R' F R2 U' R' U' R U R' F'"
        ],
        "V Permutation": [ #OK
            {(-1, 1, -1): (right, top, front), (0, 1, -1): ('', top, right), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (left, top, ''), (1, 1, 0): (back, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (left, top, back)},
            "R' U R' U' B' R' B2 U' B' U B' R B R"
        ],
        "Y Permutation": [ #OK
            {(-1, 1, -1): (right, top, front), (0, 1, -1): ('', top, left), (1, 1, -1): (right, top, back),
             (-1, 1, 0): (back, top, ''), (1, 1, 0): (right, top, ''),
             (-1, 1, 1): (left, top, front), (0, 1, 1): ('', top, front), (1, 1, 1): (left, top, back)},
            "R' U' R U' L R U2 R' U' R U2 L' U R2 U R"
        ]

    }

    return pll_dict