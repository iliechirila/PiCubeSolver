import json
import time

import cv2
import numpy as np
from PyQt5 import Qt
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal, pyqtSlot, QSize, QMutex
from PyQt5.QtGui import QColor, QImage, QPixmap, QPainter, QPen, QFont
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QLabel, QDialog, QVBoxLayout

from Codebase.Camera_Detection.PointsController import PointsController
from Codebase.Common.Cube import Cube
from Codebase.GUI.GeneratedDesign.mainWindow import *
# from Codebase.Motors.MotorsController import MotorsController
from Codebase.Solvers.Solver import Solver

MIN = 0
MAX = 1
HUE = 0
SATURATION = 1
VALUE = 2
MAIN_PAGE = 0
DEBUG_PAGE = 1

class CameraThread(QThread):
    frame_ready = pyqtSignal(QImage)

    def __init__(self, name, index, coordinates):
        super(CameraThread, self).__init__()
        self.name = name
        self.video = cv2.VideoCapture(index)
        self.coordinates = coordinates
        self.mutex = QMutex()
        self.apply_filter = False
        self.lower_color = np.array([0,0,0])
        self.upper_color = np.array([255,255,255])

    def set_apply_filter(self, value, lower_color=[0,0,0], upper_color=[255,255,255]):
        self.mutex.lock()
        self.apply_filter = value
        self.lower_color = np.array(lower_color)
        self.upper_color = np.array(upper_color)
        print(value, lower_color, upper_color)
        self.mutex.unlock()

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def run(self):
        while True:
            ret, frame = self.video.read()
            if ret:
                # resource sharing
                self.mutex.lock()
                apply_filter = self.apply_filter
                self.mutex.unlock()

                if self.apply_filter:
                    # Convert frame to HSV
                    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    # Define lower and upper bounds for the color range
                    lower_color = np.array([10, 100, 100])  # Adjust the values for your desired color range
                    upper_color = np.array([20, 255, 255])  # Adjust the values for your desired color range

                    # Apply the color filter
                    mask = cv2.inRange(hsv_image, self.lower_color, self.upper_color)
                    filtered_image = cv2.bitwise_and(frame, frame, mask=mask)
                else:
                    filtered_image = frame

                # Draw points on the filtered frame
                for point in self.coordinates:
                    x = point.x
                    y = point.y
                    cv2.circle(filtered_image, (x, y), 5, (0, 0, 255), -1)

                # Convert filtered frame to RGB for display in PyQt
                rgb_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

                self.frame_ready.emit(q_image)

class SolverThread(QThread):
    solution_found = pyqtSignal(str, str, list)

    def __init__(self, solver):
        super().__init__()
        self.solver = solver

    def run(self):
        start_time = time.time()
        solution_formatted, solution_std, solution_tuples = self.solver.solve_cube()
        self.solution_found.emit(solution_formatted, solution_std, solution_tuples)
        print(time.time()-start_time)

class LoadingWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading")
        self.setFixedSize(200, 100)

        layout = QVBoxLayout()

        label = QLabel("Finding solution...")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)


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
        self.frame_top_bar.hide()
        self.load_color_intervals()
        self.setup_cube_projection()
        self.main_cam.setFixedSize(QSize(310, 245))
        self.main_cam_2.setFixedSize(QSize(310, 245))
        self.cap = CameraThread("Cam1", 0, [])
        self.cap2 = CameraThread("Cam2", 1, [])
        self.solver = Solver()
        self.loading_window = LoadingWindow()
        self.cube_list = []
        self.solution_std = ''
        self.solution_tuple = []
        self.rpm = 30
        self.slider_rpm.setValue(30)
        # self.motors_controller = MotorsController()
        self.center_colors = ['w', 'o', 'g', 'r', 'b', 'y']
        self.current_table_face = None
        self.aspect_ratio = 1280 / 720
        self.tableWidget.setRowCount(0)  # the table is empty
        self.points_controller = PointsController()
        self.connect_events()
        self.disable_hsv_layout()
        self.update_table_values()
        print("Created Main Window GUI in Controller")

    def change_rpm(self):
        self.rpm = int(self.slider_rpm.value())
        self.label_rpm.setText(str(self.rpm))

    # def setup_motors_pins(self):
    #     self.motors_controller.add_pins_configuration("U",1,1,1)
    #
    # def solve_with_motor(self):
    #     self.motors_controller.solve_cube(self.solution_tuple, self.rpm)
    #
    @pyqtSlot(QImage)
    def update_frame(self, q_image):
        pixmap = QPixmap.fromImage(q_image)
        pixmap = pixmap.scaled(self.main_cam.width(), self.main_cam.height())
        if self.main_cam.isVisible():
            self.main_cam.setPixmap(pixmap)
        elif self.main_cam_debug_3.isVisible():
            self.main_cam_debug_3.setPixmap(pixmap)

    @pyqtSlot(QImage)
    def update_frame_2(self, q_image):
        pixmap = QPixmap.fromImage(q_image)
        pixmap = pixmap.scaled(self.main_cam_2.width(), self.main_cam_2.height())
        if self.main_cam_2.isVisible():
            self.main_cam_2.setPixmap(pixmap)
        elif self.main_cam_debug_4.isVisible():
            self.main_cam_debug_4.setPixmap(pixmap)

    def load_color_intervals(self):
        with open("./Common/color_intervals.json", 'r') as json_file:
            self.color_ranges = json.load(json_file)

    def write_color_intervals_to_file(self):
        with open("./Common/color_intervals.json", 'w') as json_file:
            json.dump(self.color_ranges, json_file)

    def connect_events(self):
        #rpm
        self.slider_rpm.valueChanged.connect(self.change_rpm)

        self.label_warning_faces.setText("Invalid centers configuration!")
        self.label_warning_faces.setFont(QFont("Arial", 12, QFont.Bold))
        self.label_warning_faces.setStyleSheet("color: red;")
        self.label_warning_faces.hide()

        # Pages buttons
        self.button_main_page.clicked.connect(lambda: self.stackedWidget_content.setCurrentIndex(MAIN_PAGE))
        self.button_debug_page.clicked.connect(lambda: self.stackedWidget_content.setCurrentIndex(DEBUG_PAGE))

        # heh nice sizing hack
        size = QSize(20, 20)
        self.o4.setFixedSize(size)
        self.o5.setFixedSize(size)
        self.o6.setFixedSize(size)
        self.g4.setFixedSize(size)
        self.g5.setFixedSize(size)
        self.g6.setFixedSize(size)
        self.r4.setFixedSize(size)
        self.r5.setFixedSize(size)
        self.r6.setFixedSize(size)
        self.b4.setFixedSize(size)
        self.b5.setFixedSize(size)
        self.b6.setFixedSize(size)
        self.w2.setFixedSize(size)
        self.w5.setFixedSize(size)
        self.w8.setFixedSize(size)
        self.g2.setFixedSize(size)
        self.g8.setFixedSize(size)
        self.y2.setFixedSize(size)
        self.y5.setFixedSize(size)
        self.y8.setFixedSize(size)
        # Centers detection & Table stuff
        self.checkBox_detect_centers.stateChanged.connect(self.toggle_centers_detection)
        self.comboBox_up_color.currentIndexChanged.connect(self.check_centers_detection)
        self.comboBox_front_color.currentIndexChanged.connect(self.check_centers_detection)
        self.button_update_table_up.clicked.connect(lambda: self.set_coordinates("Up"))
        self.button_update_table_left.clicked.connect(lambda: self.set_coordinates("Left"))
        self.button_update_table_front.clicked.connect(lambda: self.set_coordinates("Front"))
        self.button_update_table_right.clicked.connect(lambda: self.set_coordinates("Right"))
        self.button_update_table_back.clicked.connect(lambda: self.set_coordinates("Back"))
        self.button_update_table_down.clicked.connect(lambda: self.set_coordinates("Down"))
        self.button_display_all_points.clicked.connect(self.display_all_points)
        self.button_clear_all_points.clicked.connect(self.clear_all_coordinates)
        self.button_update_coordinate_file.clicked.connect(self.points_controller.update_file)
        self.tableWidget.itemChanged.connect(self.update_coordinates_from_table_update)
        self.button_detect_all_colors.clicked.connect(self.detect_colors_method)

        # HSV
        self.checkBox_edit_color_intervals.stateChanged.connect(self.toggle_hsv_detection)
        self.comboBox_colors_HSV.currentIndexChanged.connect(self.change_hsv_filter)
        self.slider_hue_min.valueChanged.connect(lambda: self.update_color_intervals_and_label_from_slider(MIN, HUE, self.slider_hue_min.value(), self.hue_min))
        self.slider_hue_max.valueChanged.connect(lambda: self.update_color_intervals_and_label_from_slider(MAX, HUE, self.slider_hue_max.value(), self.hue_max))
        self.slider_saturation_min.valueChanged.connect(lambda: self.update_color_intervals_and_label_from_slider(MIN, SATURATION, self.slider_saturation_min.value(), self.saturation_min))
        self.slider_saturation_max.valueChanged.connect(
            lambda: self.update_color_intervals_and_label_from_slider(MAX, SATURATION, self.slider_saturation_max.value(), self.saturation_max))
        self.slider_value_min.valueChanged.connect(lambda: self.update_color_intervals_and_label_from_slider(MIN, VALUE, self.slider_value_min.value(), self.value_min))
        self.slider_value_max.valueChanged.connect(lambda: self.update_color_intervals_and_label_from_slider(MAX, VALUE, self.slider_value_max.value(), self.value_max))
        self.button_save_hsv_to_file.clicked.connect(self.write_color_intervals_to_file)
        # Solver
        self.button_find_solution.clicked.connect(self.find_solution)
        # Cameras
        self.cap.frame_ready.connect(self.update_frame)
        self.cap.start()
        self.cap2.frame_ready.connect(self.update_frame_2)
        self.cap2.start()


    def display_all_points(self):
        self.set_all_coordinates()
        self.update_table_values_all()

    def toggle_centers_detection(self):
        check = self.checkBox_detect_centers.isChecked()
        self.comboBox_up_color.setDisabled(check)
        self.comboBox_front_color.setDisabled(check)
        if check:
            self.check_centers_detection()
        else:
            self.button_detect_all_colors.setEnabled(True)

    def toggle_hsv_detection(self):
        print("Toggled")
        if self.checkBox_edit_color_intervals.isChecked():
            print("Checked")
            self.enable_hsv_layout(enable=True)
            self.change_hsv_filter()
        else:
            print("Unchecked")
            self.disable_hsv_layout(disable=True)

    def enable_hsv_layout(self, enable = True):
        self.comboBox_colors_HSV.setEnabled(enable)
        self.slider_hue_max.setEnabled(enable)
        self.slider_hue_min.setEnabled(enable)
        self.hue_max.setEnabled(enable)
        self.hue_min.setEnabled(enable)
        self.slider_saturation_max.setEnabled(enable)
        self.slider_saturation_min.setEnabled(enable)
        self.saturation_max.setEnabled(enable)
        self.saturation_min.setEnabled(enable)
        self.slider_value_max.setEnabled(enable)
        self.slider_value_min.setEnabled(enable)
        self.value_max.setEnabled(enable)
        self.value_min.setEnabled(enable)
        self.button_save_hsv_to_file.setEnabled(enable)
        self.cap.set_apply_filter(True)
        self.cap2.set_apply_filter(True)

    def disable_hsv_layout(self, disable = True):
        self.comboBox_colors_HSV.setDisabled(disable)
        self.slider_hue_max.setDisabled(disable)
        self.slider_hue_min.setDisabled(disable)
        self.hue_max.setDisabled(disable)
        self.hue_min.setDisabled(disable)
        self.slider_saturation_max.setDisabled(disable)
        self.slider_saturation_min.setDisabled(disable)
        self.saturation_max.setDisabled(disable)
        self.saturation_min.setDisabled(disable)
        self.slider_value_max.setDisabled(disable)
        self.slider_value_min.setDisabled(disable)
        self.value_max.setDisabled(disable)
        self.value_min.setDisabled(disable)
        self.button_save_hsv_to_file.setDisabled(disable)
        self.cap.set_apply_filter(False)
        self.cap2.set_apply_filter(False)

    def change_hsv_filter(self):
        color = self.comboBox_colors_HSV.currentText().lower()

        self.slider_hue_min.setValue(self.color_ranges[color][MIN][HUE])
        self.slider_hue_max.setValue(self.color_ranges[color][MAX][HUE])
        self.slider_saturation_min.setValue(self.color_ranges[color][MIN][SATURATION])
        self.slider_saturation_max.setValue(self.color_ranges[color][MAX][SATURATION])
        self.slider_value_min.setValue(self.color_ranges[color][MIN][VALUE])
        self.slider_value_max.setValue(self.color_ranges[color][MAX][VALUE])

        self.cap.set_apply_filter(True, self.color_ranges[color][0], self.color_ranges[color][1])
        self.cap2.set_apply_filter(True, self.color_ranges[color][0], self.color_ranges[color][1])

    def update_color_intervals_and_label_from_slider(self, min_max, hsv, value, label: QLabel):
        color = self.comboBox_colors_HSV.currentText().lower()
        self.color_ranges[color][min_max][hsv] = value
        label.setText(str(value))
        self.change_hsv_filter()

    def check_centers_detection(self):
        W, O, G, R, B, Y = 'W', 'O', 'G', 'R', 'B', 'Y'
        opposite_colors = {W: Y, Y: W, R: O, O: R, G: B, B: G}
        up_text = self.comboBox_up_color.currentText()[0]
        front_text = self.comboBox_front_color.currentText()[0]
        if up_text == front_text or up_text == opposite_colors[front_text]:
            self.label_warning_faces.show()
            self.button_detect_all_colors.setDisabled(True)
            self.center_colors = ['w', 'o', 'g', 'r', 'b', 'y']
        else:
            self.label_warning_faces.hide()
            self.find_cube_orientation()
            self.button_detect_all_colors.setEnabled(True)

    def find_cube_orientation(self):
        up_color = self.comboBox_up_color.currentText()[0]
        front_color = self.comboBox_front_color.currentText()[0]
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
        self.center_colors = [item.lower() for item in [up_color, left_color, front_color, opposite_colors[left_color],
                              opposite_colors[front_color], opposite_colors[up_color]]
        ]

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

        # cap1 or cap2
        if face in ["Left", "Front", "Up"]:
            self.cap.set_coordinates(coordinates)
            self.cap2.set_coordinates([])
        elif face in ["Right", "Back", "Down"]:
            self.cap2.set_coordinates(coordinates)
            self.cap.set_coordinates([])

    def set_all_coordinates(self):
        coordinates_cap = []
        coordinates_cap2 = []
        for face, points in self.points_controller.points_dict.items():
            if face in ["Left", "Front", "Up"]:
                coordinates_cap.extend(points)
            elif face in ["Right", "Back", "Down"]:
                coordinates_cap2.extend(points)
        self.cap.set_coordinates(coordinates_cap)
        self.cap2.set_coordinates(coordinates_cap2)

    def clear_all_coordinates(self):
        self.cap.set_coordinates([])
        self.cap2.set_coordinates([])
        self.clear_table()

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
        self.cube_list = cube_list
        grids = [self.grid_white, self.grid_orange, self.grid_green, self.grid_red, self.grid_blue, self.grid_yellow]
        colors = {'w': "white", 'o': "orange", 'g': "green", 'r': "red", 'b': "blue", 'y': "yellow", 'u': "black"}
        for face, grid in zip(cube_list, grids):
            for i in range(9):
                label = grid.itemAtPosition(int(i / 3), i % 3).widget()
                label.setStyleSheet(f"background-color: {colors[face[i]]}; border: 1px solid black;")

    def clear_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    def update_table_values(self, face=None):
        # !!!!! important, otherwise we enter an infinite loop (1/2)
        self.tableWidget.itemChanged.disconnect()
        if face:
            self.tableWidget.setRowCount(9)
            self.current_table_face = face
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
        # !!!!! important, otherwise we enter an infinite loop (2/2)
        self.tableWidget.itemChanged.connect(self.update_coordinates_from_table_update)

    def update_table_values_all(self):
        # !!!!! important, otherwise we enter an infinite loop (1/2)
        self.tableWidget.itemChanged.disconnect()
        self.tableWidget.setRowCount(54)
        row_cnt = 0
        for face, points_lst in self.points_controller.points_dict.items():
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
        # !!!!! important, otherwise we enter an infinite loop (2/2)
        self.tableWidget.itemChanged.connect(self.update_coordinates_from_table_update)

    def identify_color(self, hsv):
        for color, (lower, upper) in self.color_ranges.items():
            if np.alltrue(np.greater_equal(hsv, lower)) and np.alltrue(np.less_equal(hsv, upper)):
                return color
        return "Unknown"

#######################################
# TODO FIX CAUSE IT BREAKS HERE IN AN INCONSISTENT WAY WTF
#######################################
    def detect_colors_method(self):
        colors_list = []
        if self.cap.video:
            ret, frame = self.cap.video.read()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            up_left_front = ["Up", "Left", "Front"]
            # for face, points_lst in self.points_controller.points_dict.items():
            for face in up_left_front:
                points_lst = self.points_controller.points_dict[face]
                colors_current_face = ''
                for point in points_lst:
                    x, y = point.x, point.y
                    hsv_color = hsv_frame[y, x]
                    point.color = self.identify_color(hsv_color)
                    colors_current_face = colors_current_face + point.color[0].lower()
                colors_list.append(colors_current_face)
        else:
            print("Camera 1 not capturing.")

        if self.cap2.video:
            ret, frame = self.cap2.video.read()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            right_back_down = ["Right", "Back", "Down"]
            # for face, points_lst in self.points_controller.points_dict.items():
            for face in right_back_down:
                points_lst = self.points_controller.points_dict[face]
                colors_current_face = ''
                for point in points_lst:
                    x, y = point.x, point.y
                    hsv_color = hsv_frame[y, x]
                    point.color = self.identify_color(hsv_color)
                    colors_current_face = colors_current_face + point.color[0].lower()
                colors_list.append(colors_current_face)
        else:
            print("Camera 2 not capturing.")

        # in case the cube orientation is not standard, or we do not use center detection,
        # simply replace the colors in the centers
        if not self.checkBox_detect_centers.isChecked():
            for i in range(6):
                colors = colors_list[i]
                center = self.center_colors[i]
                new_colors = colors[:4] + center + colors[5:]
                colors_list[i] = new_colors
        print(colors_list)
        self.update_cube_projection(colors_list)
        self.update_table_values()

    def find_solution(self):
        ##################
        # REMOVE THIS
        ##################
        # self.solver.cube.apply_alg_std("F' D' U B F2 L U' R B F2 R2 D2 F U L' R' F2 D U B' R B2 R' F R2 F' L2 D2 B R2")
        self.solver.update_cube_dict_from_colors_list(self.cube_list)
        self.solution_thread = SolverThread(self.solver)
        self.solution_thread.solution_found.connect(self.update_solution)
        self.loading_window.show()
        self.solution_thread.start()

    def update_solution(self, solution_formatted, solution_std, solution_tuples):
        self.solution_std = solution_std
        self.solution_tuple = solution_tuples
        self.plainText_cfop.setPlainText(solution_formatted)
        self.loading_window.close()
