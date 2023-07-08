from PyQt5 import QtWidgets
from pyqtgraph import mkQApp
from Codebase.MainAppStuff.MainWindowGUIControllerClass import MainWindowGUIControllerClass

try:
    app = mkQApp("CubeSolver")
    window = MainWindowGUIControllerClass()

    window.show()
    app.exec()

except Exception as e:
    print("Exception occurred:", str(e))

