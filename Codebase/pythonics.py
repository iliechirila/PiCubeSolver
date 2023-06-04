import json

from Codebase.Camera_Detection.PointsController import Point

with open('./Common/positions.json') as file:
    data = json.load(file)
    basic_color = "Unknown"
    points_dict = dict()
    for face, points in data.items():
        lst = list()
        for index, coords in points.items():
            lst.append(Point(face, int(index), int(coords[0]), int(coords[1]), basic_color))
        points_dict.update({face: lst})


