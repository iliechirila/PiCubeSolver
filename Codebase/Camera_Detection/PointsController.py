import json


class PointsController:
    # def __init__(self, table, label_matrices, label_cam1=None, label_cam2=None, winGUI=None):
        # self.table = table
        # self.label_matrices = label_matrices
        # self.label_cam1 = label_cam1
        # self.label_cam2 = label_cam2
        # self.WinGUI = winGUI
        # self.points_colors = self.initiate_points()
    def __init__(self):
        self.points_dict = self.initiate_points()

    def initiate_points(self):
        with open('./Common/positions.json') as file:
            data = json.load(file)
            basic_color = "Unknown"
            points_dict = dict()
            for face, points in data.items():
                lst = list()
                for index, coords in points.items():
                    lst.append(Point(face, int(index), int(coords[0]), int(coords[1]), basic_color))
                points_dict.update({face:lst})
            return points_dict

    def update_point(self, face, index, x, y, color):
        for point in self.points_dict[face]:
            if point.index == index:
                point.x = x
                point.y = y
                point.color = color
                break

    def update_file(self):
        with open('./Common/positions.json', 'w') as file:
            file.seek(0)
            data = dict()
            for face, points in self.points_dict.items():
                data.update({face: []})
                for point in points:
                    data[face].append({point.index: [point.x, point.y]})
            json.dump(data, file, indent=2)

class Point:

    def __init__(self, face, index, x, y, color):
        self.face = face
        self.index = index
        self.x = x
        self.y = y
        self.color = color