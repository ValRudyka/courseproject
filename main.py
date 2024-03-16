from PySide6.QtWidgets import  QApplication
from dotenv import load_dotenv

from mvc.model import Model
from mvc.controller import Controller 
from mvc.view.mainmenu.mainview import MainView
from mvc.view.interface.chartsview import ChartsView

import os


if __name__ == "__main__":
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
    load_dotenv()
    
    app = QApplication([])
    controller = Controller(Model(), MainView(), ChartsView())
    app.exec()