from PySide6.QtWidgets import  QApplication

from mvc.model import Model
from mvc.controller import Controller 
from mvc.view.view import View

if __name__ == "__main__":    
    app = QApplication([])
    Controller(Model(), View())
    app.exec()  