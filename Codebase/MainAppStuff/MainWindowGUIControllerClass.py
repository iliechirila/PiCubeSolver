import cv2
import numpy as np
from PyQt5 import Qt
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal, pyqtSlot, QSize
from PyQt5.QtGui import QColor, QImage, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QTableWidgetItem

from Codebase.Camera_Detection.PointsController import PointsController
from Codebase.GUI.GeneratedDesign.mainWindow import *


class CameraThread(QThread):
    frame_ready = pyqtSignal(QImage)

    def __init__(self, coordinates):
        super(CameraThread, self).__init__()

        self.video = cv2.VideoCapture(0)
        self.coordinates = coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
        print(self.coordinates)

    def run(self):
        while True:
            ret, frame = self.video.read()

            if ret:
                # Draw points on the frame
                for point in self.coordinates:
                    x = point.x
                    y = point.y
                    cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

                self.frame_ready.emit(q_image)


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
        self.main_cam.setFixedSize(QSize(310, 245))
        self.main_cam_2.setFixedSize(QSize(310, 245))
        self.cap = CameraThread([])

        self.aspect_ratio = 1280 / 720
        self.tableWidget.setRowCount(9)  # 9 cubies on every face
        self.points_controller = PointsController()
        self.connect_events()
        self.update_table_values()
        print("Created Main Window GUI in Controller")

    @pyqtSlot(QImage)
    def update_frame(self, q_image):
        pixmap = QPixmap.fromImage(q_image)
        pixmap = pixmap.scaled(self.main_cam.width(), self.main_cam.height())
        self.main_cam.setPixmap(pixmap)

    def connect_events(self):
        self.button_update_table_up.clicked.connect(lambda: self.set_coordinates("Up"))
        self.button_update_table_left.clicked.connect(lambda: self.set_coordinates("Left"))
        self.button_update_table_front.clicked.connect(lambda: self.set_coordinates("Front"))
        self.button_update_table_right.clicked.connect(lambda: self.set_coordinates("Right"))
        self.button_update_table_back.clicked.connect(lambda: self.set_coordinates("Back"))
        self.button_update_table_down.clicked.connect(lambda: self.set_coordinates("Down"))
        self.tableWidget.itemChanged.connect(self.update_coordinates_from_table_update)
        self.detect_colors.clicked.connect(self.detect_colors_Up_Left_Front)
        self.cap.frame_ready.connect(self.update_frame)
        self.cap.start()

    def update_coordinates_from_table_update(self, item):
        if item.column() == 2 or item.column() == 3:
            face = self.tableWidget.item(item.row(), 0).text()
            index = int(self.tableWidget.item(item.row(), 1).text())
            x = int(self.tableWidget.item(item.row(), 2).text())
            y = int(self.tableWidget.item(item.row(), 3).text())
            color = self.tableWidget.item(item.row(), 4).text()
            print(face, index, x, y, color)
        self.points_controller.update_point(face, index, x, y, color)
        self.set_coordinates(face)
    def set_coordinates(self, face):
        coordinates = self.points_controller.points_dict[face]
        self.update_table_values(face)
        self.cap.set_coordinates(coordinates)

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

    def update_cube_projection(self, cube_list=None):
        if not cube_list:
            cube_list = ["wwwwwwwww", "ooooooooo", "ggggggggg", "rrrrrrrrr", "bbbbbbbbb", "yyyyyyyyy"]
        grids = [self.grid_white, self.grid_orange, self.grid_green, self.grid_red, self.grid_blue, self.grid_yellow]
        colors = {'w': "white", 'o': "orange", 'g': "green", 'r': "red", 'b': "blue", 'y': "yellow", 'u': "black"}
        for face, grid in zip(cube_list, grids):
            for i in range(9):
                # print(i, int(i/3), i%3)
                label = grid.itemAtPosition(int(i / 3), i % 3).widget()
                # print(label.objectName(), colors[face[i]])
                label.setStyleSheet(f"background-color: {colors[face[i]]}; border: 1px solid black;")

    def update_table_values(self, face = 'Up'):
        # important, otherwise we enter an infinite loop
        self.tableWidget.itemChanged.disconnect()

        row_cnt = 0
        points_lst = self.points_controller.points_dict[face]
        for point in points_lst:
            table_item = QTableWidgetItem(str(face))
            self.tableWidget.setItem(row_cnt, 0, table_item)
            table_item = QTableWidgetItem(str(point.index))
            self.tableWidget.setItem(row_cnt, 1, table_item)
            table_item = QTableWidgetItem(str(point.x))
            self.tableWidget.setItem(row_cnt, 2, table_item)
            table_item = QTableWidgetItem(str(point.y))
            self.tableWidget.setItem(row_cnt, 3, table_item)
            table_item = QTableWidgetItem(str(point.color))
            self.tableWidget.setItem(row_cnt, 4, table_item)

            row_cnt = row_cnt + 1
        # important, otherwise we enter an infinite loop
        self.tableWidget.itemChanged.connect(self.update_coordinates_from_table_update)

    def set_color_to_component(self, component, color):
        component.setPixmap(self.colors[color])

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            for face, points_lst in self.points_controller.points_dict.items():
                for point in points_lst:
                    pixmap = self.addPoint(pixmap, point.x, point.y)
            self.main_cam.setPixmap(pixmap)

    def mousePressEventAddPoint(self, event):
        if event.button() == Qt.LeftButton:
            position = event.pos()
            position.setX(int(position.x() / self.aspect_ratio))
            position.setY(int(position.y() * self.aspect_ratio))

            print(position, position / self.aspect_ratio)
            self.points.append(position)
            self.update_camera()

    def addPoint(self, pixmap, x, y):
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        point_size = 3
        point_color = Qt.red

        pen = QPen(point_color)
        pen.setWidth(point_size)
        painter.setPen(pen)

        painter.drawPoint(x, y)
        painter.end()

        return pixmap

    def identify_color(self, hsv):
        for color, (lower, upper) in self.color_ranges.items():
            if np.alltrue(np.greater_equal(hsv, lower)) and np.alltrue(np.less_equal(hsv, upper)):
                return color
        return "Unknown"

    def detect_colors_Up_Left_Front(self):
        ret, frame = self.cap.video.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        colors_list = []
        for face, points_lst in self.points_controller.points_dict.items():
            colors_current_face = ''
            for point in points_lst:
                x,y = point.x, point.y
                hsv_color = hsv_frame[y, x]
                point.color = self.identify_color(hsv_color)
                colors_current_face = colors_current_face + point.color[0].lower()
            colors_list.append(colors_current_face)

        self.update_cube_projection(colors_list)
