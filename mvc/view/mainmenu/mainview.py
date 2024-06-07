from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QMovie

from mvc.view.mainmenu.ui_mainmenu import Ui_MainWindow
from config import LOADING_SPINNER_PATH

class MainView(QMainWindow):    
    def __init__(self) -> None:
        super(MainView, self).__init__()
        self.message = QMessageBox()
        self.movie = QMovie(fileName=LOADING_SPINNER_PATH)
        self.__build_ui()

    def __build_ui(self) -> None:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.show()

    def show_message(self, title: str, text: str) -> None:
        self.message.setWindowTitle(title)
        self.message.setText(text)
        self.message.exec_()

    def start_movie(self, type: str) -> None:
        match type:
            case 'fetch':
                self.ui.label_15.setMovie(self.movie)
            case 'model':
                self.ui.label_16.setMovie(self.movie)
            case 'pdf':
                self.ui.label_17.setMovie(self.movie)
        self.movie.start()

    def stop_movie(self) -> None:
        self.movie.stop()
        self.ui.label_15.clear()