from PySide6.QtWidgets import  QApplication

from mvc.model import Model
from mvc.controller import Controller 
from mvc.view.mainmenu.mainview import MainView
from mvc.view.interface.chartsview import ChartsView

if __name__ == "__main__":
    app = QApplication([])
    controller = Controller(Model(), MainView(), ChartsView())
    app.exec()