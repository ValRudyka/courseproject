from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

from shadow_elements import shadow_elements_charts

from mvc.view.interface.ui_interface import Ui_ChartsWindow


class ChartsView(QMainWindow):
    def __init__(self) -> None:
        super(ChartsView, self).__init__()
        self.build_ui()

    def build_ui(self) -> None:
        self.ui = Ui_ChartsWindow()
        self.ui.setupUi(self)

    def dark_mode(self) -> None:
        self.ui.centralwidget.setStyleSheet(u"@font-face {\n"
        "    font-family: NovaFlat;\n"
        "    src: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf) format(\"truetype\");\n"
        "}\n"
        "*{\n"
        "color: #fff;\n"
        "font-family: NovaFlat;\n"
        "font-size: 12px;\n"
        "border: nine;\n"
        "background: none;\n"
        "}\n"
        "#centralwidget{\n"
        "background-color: rgb(33, 43, 51);\n"
        "}\n"
        "#left_menu_widget, #percentage_bar_chart, #nested_donuts,\n"
        "#line_charts, #bar_charts, #temperature_bar_chart\n"
        "{\n"
        "background-color: rgba(61, 80, 95, 100)\n"
        "}\n"
        "#header_frame, #frame_3, #frame_5{\n"
        "background-color: rgb(61, 80, 95);\n"
        "}\n"
        "#frame_4 QPushButton{\n"
        "padding: 10px;\n"
        "border-radius: 5px;\n"
        "background-color: rgba(33, 43, 51, 100);\n"
        "}\n"
        "#header_nav QPushButton{\n"
        "	background-color: rgb(61, 80, 95);\n"
        "	border-radius: 15px;\n"
        "	border: 3px solid rgb(120, 157, 186);\n"
        "}\n"
        "#header_nav QPushButton:hover{\n"
        "	background-color: rgb(120, 157, 186);\n"
        "}\n"
        "")
    
    def light_mode(self):
        self.ui.centralwidget.setStyleSheet(u"@font-face {\n"
        "    font-family: NovaFlat;\n"
        "    src: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf) format(\"truetype\");\n"
        "}\n"
        "* {\n"
        "    color: #000;\n"
        "    font-family: NovaFlat;\n"
        "    font-size: 12px;\n"
        "    border: inherit;\n"
        "    background: none;\n"
        "}\n"
        "\n"
        "#centralwidget {\n"
        "    background: rgb(102, 153, 204);\n"
        "}\n"
        "#left_menu_widget,\n"
        "#percentage_bar_chart,\n"
        "#nested_donuts,\n"
        "#line_charts,\n"
        "#bar_charts,\n"
        "#temperature_bar_chart {\n"
        "    background-color: rgb(255, 255, 240);\n"
        "}\n"
        "#frame_15, #frame_16 {\n"
        "background-color: rgb(255, 255, 240)"
        "}\n"
        "#header_frame, \n"
        "#frame_3,\n"
        "#frame_5 {\n"
        "    background-color: rgb(255, 255, 240);\n"
        "}\n"
        "#frame_4 QPushButton {\n"
        "    padding: 10px;\n"
        "    border-radius: 5px;\n"
        "    background-color: rgba(255, 255, 255, 1);\n"
        "}\n"
        "#header_nav QPushButton {\n"
        "    background-color: #f0f0f0;\n"
        "    border-radius: 15px;\n"
        "    border: 3px solid #789dbe;\n"
        "}\n"
        "#header_nav QPushButton:hover {\n"
        "    background-color: #789dbe;\n"
        "}")

    def charts_shadow_effects(self) -> None:
        for shadow_el in shadow_elements_charts:
            effect = QGraphicsDropShadowEffect(self.ui)
            effect.setBlurRadius(20)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 5, 5, 255))
            getattr(self.ui, shadow_el).setGraphicsEffect(effect)
