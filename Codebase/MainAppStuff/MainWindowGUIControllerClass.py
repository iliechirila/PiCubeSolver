from PyQt5.QtWidgets import QApplication
from Codebase.GUI.GeneratedDesign.mainWindow import *


class MainWindowGUIControllerClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        print("Created Main Window GUI in Controller")
