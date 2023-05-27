from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from Codebase.GUI.GeneratedDesign.mainWindow import *


class MainWindowGUIControllerClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.setup_cube_projection()
        print("Created Main Window GUI in Controller")

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
        colors = {'w': "white", 'o': "orange", 'g': "green", 'r': "red", 'b': "blue", 'y': "yellow"}
        for face, grid in zip(cube_list, grids):
            for i in range(9):
                print(i, int(i/3), i%3)
                label = grid.itemAtPosition(int(i/3), i%3).widget()
                print(label.objectName(), colors[face[i]])
                label.setStyleSheet(f"background-color: {colors[face[i]]}; border: 1px solid black;")


    def set_color_to_component(self, component, color):
        component.setPixmap(self.colors[color])
