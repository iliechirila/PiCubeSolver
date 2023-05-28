import cv2
import numpy as np
from PyQt5 import Qt
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QImage, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QApplication
from Codebase.GUI.GeneratedDesign.mainWindow import *


class MainWindowGUIControllerClass(QtWidgets.QMainWindow, Ui_MainWindow):
    color_ranges = {
        'white': ([0, 0, 100], [180, 30, 255]),
        'green': ([35, 50, 50], [85, 255, 255]),
        'yellow': ([20, 100, 100], [40, 255, 255]),
        'orange': ([10, 100, 100], [20, 255, 255]),
        'red': ([0, 100, 100], [10, 255, 255]),
        'blue': ([90, 100, 100], [130, 255, 255])
    }
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.setup_cube_projection()
        self.cap = cv2.VideoCapture(0)
        self.aspect_ratio = 1280 / 720
        self.points = []
        self.connect_events()
        print("Created Main Window GUI in Controller")

    def connect_events(self):
        self.detect_colors.clicked.connect(self.detect_colors_Up_Left_Front)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(100)
        self.main_cam.setScaledContents(True)
        self.main_cam.mousePressEvent = self.mousePressEventAddPoint


    def setup_cube_projection(self):
        for i in range(9):
            whiteLabel = self.grid_white.itemAt(i).widget()
            whiteLabel.setStyleSheet("background-color: white; border: 1px solid black;")
            whiteLabel.setText('')

            greenLabel = self.grid_green.itemAt(i).widget()
            greenLabel.setStyleSheet("background-color: green; border: 1px solid black;")
            greenLabel.setText('')

            yellowLabel = self.grid_yellow.itemAt(i).widget()
            yellowLabel.setStyleSheet("background-color: yellow; border: 1px solid black;")
            yellowLabel.setText('')

            orangeLabel = self.grid_orange.itemAt(i).widget()
            orangeLabel.setStyleSheet("background-color: orange; border: 1px solid black;")
            orangeLabel.setText('')

            redLabel = self.grid_red.itemAt(i).widget()
            redLabel.setStyleSheet("background-color: red; border: 1px solid black;")
            redLabel.setText('')

            blueLabel = self.grid_blue.itemAt(i).widget()
            blueLabel.setStyleSheet("background-color: blue; border: 1px solid black;")
            blueLabel.setText('')

    def update_cube_projection(self, cube_list = None):
        if not cube_list:
            cube_list = ["wwwwwwwww", "ooooooooo", "ggggggggg", "rrrrrrrrr", "bbbbbbbbb", "yyyyyyyyy"]
        grids = [self.grid_white, self.grid_orange, self.grid_green, self.grid_red, self.grid_blue, self.grid_yellow]
        colors = {'w': "white", 'o': "orange", 'g': "green", 'r': "red", 'b': "blue", 'y': "yellow", 'u':"black"}
        for face, grid in zip(cube_list, grids):
            for i in range(9):
                # print(i, int(i/3), i%3)
                label = grid.itemAtPosition(int(i/3), i%3).widget()
                # print(label.objectName(), colors[face[i]])
                label.setStyleSheet(f"background-color: {colors[face[i]]}; border: 1px solid black;")


    def set_color_to_component(self, component, color):
        component.setPixmap(self.colors[color])

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            width = int(self.main_cam.height() * self.aspect_ratio)
            height = self.main_cam.height()
            frame = cv2.resize(frame, (height, width))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            if self.points:
                for pos in self.points:
                    pixmap = self.addPoint(pixmap, pos)
            self.main_cam.setPixmap(pixmap)

    def mousePressEventAddPoint(self, event):
        if event.button() == Qt.LeftButton:
            position = event.pos()
            position.setX(int(position.x() / self.aspect_ratio))
            position.setY(int(position.y() * self.aspect_ratio))

            print(position, position/self.aspect_ratio)
            self.points.append(position)
            self.update_camera()

    def addPoint(self, pixmap, position):
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        point_size = 3
        point_color = Qt.red

        pen = QPen(point_color)
        pen.setWidth(point_size)
        painter.setPen(pen)

        painter.drawPoint(position)
        painter.end()

        return pixmap

    def identify_color(self, hsv):
        for color, (lower, upper) in self.color_ranges.items():
            if np.alltrue(np.greater_equal(hsv, lower)) and np.alltrue(np.less_equal(hsv, upper)):
                return color
        return "Unknown"

    def detect_colors_Up_Left_Front(self):
        ret, frame = self.cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # PyQt5.QtCore.QPoint(147, 127)
        # PyQt5.QtCore.QPoint(168, 113)
        # PyQt5.QtCore.QPoint(188, 101)
        # PyQt5.QtCore.QPoint(173, 132)
        # PyQt5.QtCore.QPoint(184, 123)
        # PyQt5.QtCore.QPoint(215, 110)
        # PyQt5.QtCore.QPoint(206, 140)
        # PyQt5.QtCore.QPoint(225, 128)
        # PyQt5.QtCore.QPoint(244, 115)
        coords_up = [(75, 158),(81, 149),(87, 142),(83, 161),(88, 156),(95, 145),(92, 165),
                        (97, 160),(103, 149)]
        colors_up = ''
        for coords in coords_up:
            x, y = coords
            hsv_color = hsv_frame[y, x]
            colors_up = colors_up + self.identify_color(hsv_color)[0].lower()

        self.update_cube_projection([colors_up])
