from PySide6.QtWidgets import QMainWindow, QMessageBox, QLabel
from PySide6.QtGui import QMovie

from mvc.view.mainmenu.ui_mainmenu import Ui_MainWindow

class MainView(QMainWindow):    
    def __init__(self) -> None:
        super(MainView, self).__init__()
        self.message = QMessageBox()
        self.movie = QMovie()
        self.build_ui()

    def build_ui(self) -> None:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.show()

    def show_message(self, title: str, text: str) -> None:
        self.message.setWindowTitle(title)
        self.message.setText(text)
        self.message.exec_()

    def start_movie(self, path: str, label: QLabel) -> None:
        self.stop_movie()
        self.movie.setFileName(path)
        label.setMovie(self.movie)
        self.movie.start()

    def stop_movie(self) -> None:
        self.movie.stop()
        self.ui.label_15.clear()