from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

from shadow_elements import shadow_elements_main
from mvc.view.interface.chartsview import ChartsView

from mvc.view.mainmenu.ui_mainmenu import Ui_MainWindow

class MainView(QMainWindow):
    def __init__(self) -> None:
        super(MainView, self).__init__()
        self.charts_view = ChartsView()

        self.build_ui()

    def build_ui(self) -> None:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_shadow_effects()
        
        self.show()


    def setup_shadow_effects(self) -> None:
        for shadow_el in shadow_elements_main:
            effect = QGraphicsDropShadowEffect(self.ui)
            effect.setBlurRadius(15)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 5, 5, 255))
            getattr(self.ui, shadow_el).setGraphicsEffect(effect)