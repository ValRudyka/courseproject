from PySide6.QtCore import QObject

from mvc.model import Model
from mvc.view.ui_config import MAIN_MENU_DARK, MAIN_MENU_LIGHT
from mvc.view.mainmenu.mainview import MainView 
from mvc.view.interface.chartsview import ChartsView

class Controller(QObject):
    def __init__(self, model: Model, main_menu: MainView, charts_view: ChartsView) -> None:
        super().__init__()
        self.model = model 
        self.main_menu = main_menu
        self.charts_view = charts_view

        self.main_menu.ui.QPushButton.clicked.connect(self.toggleStyleSheet)
        self.main_menu.ui.fetchButton.clicked.connect(self.show_charts)

    def show_charts(self) -> None:
        self.model.get_crypto_data()
        print("Request completed")
        self.charts_view.show()
        self.charts_view.charts_shadow_effects()

    def toggleStyleSheet(self) -> None:
        if self.model.theme == "light":
            self.model.theme = 'dark'
            self.main_menu.ui.QPushButton.setText('Light mode')
            self.main_menu.ui.MainWindow.setStyleSheet(MAIN_MENU_DARK)
            self.charts_view.dark_mode()
        else:
            self.model.theme = "light"
            self.main_menu.ui.QPushButton.setText('Dark mode')
            self.main_menu.ui.MainWindow.setStyleSheet(MAIN_MENU_LIGHT)
            self.charts_view.light_mode()

        self.main_menu.setup_shadow_effects()
        self.charts_view.charts_shadow_effects()

    
        