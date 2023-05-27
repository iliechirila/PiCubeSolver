from PyQt5 import QtWidgets
from pyqtgraph import mkQApp
from Codebase.MainAppStuff.MainWindowGUIControllerClass import MainWindowGUIControllerClass

try:
    app = mkQApp("CubeSolver")
    window = MainWindowGUIControllerClass()
    cube_list = ["wwwwwwwww", "orbgrbooo", "ggggggggg", "rrrrrrrrr", "bbbbbbbbb", "yyyyyyyyy"]
    # window.update_cube_projection(cube_list)

    # window.set_color_to_component(window.label, 'b')
    window.show()
    app.exec()

except Exception as e:
    print("Exception occurred:", str(e))

