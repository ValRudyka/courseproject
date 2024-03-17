from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor

from config import shadow_elements_charts
from mvc.view.interface.ui_interface import Ui_ChartsWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Canvas(FigureCanvas):
    def __init__(self, width: int, height: int) -> None:
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
        super(Canvas, self).__init__(fig)

class ChartsView(QMainWindow):
    def __init__(self) -> None:
        super(ChartsView, self).__init__()
        self.__canvas = Canvas(10, 6)
        self.build_ui()

    def build_ui(self) -> None:
        self.ui = Ui_ChartsWindow()
        self.ui.setupUi(self)

        self.canvas_layout = QVBoxLayout()
        self.canvas_widget = QWidget()
        self.canvas_widget.setLayout(self.canvas_layout)
        self.ui.frame_16.layout().addWidget(self.canvas_widget)

    def clear_layout(self) -> None:
        for i in reversed(range(self.canvas_layout.count())):
            self.canvas_layout.itemAt(i).widget().setParent(None)

    def display_line_chart(self, predicted_data: tuple) -> None:
        self.__canvas.axes.clear()
        actual_prices, pred_prices, pred_timestamps, actual_timestamps = predicted_data

        self.__canvas.axes.plot(actual_timestamps, actual_prices.values, color='r', label='Actual prices')
        self.__canvas.axes.plot(pred_timestamps, pred_prices, color='b', label='Predicted prices')

        self.__canvas.axes.set_title('BTC price prediction')
        self.__canvas.axes.set_xlabel('Date')
        self.__canvas.axes.set_ylabel('Prices (USD)')
        self.__canvas.axes.legend()

        self.canvas_layout.addWidget(self.__canvas)
        self.__canvas.draw()

    def display_area_chart(self, predicted_data: tuple) -> None:
        self.clear_layout()
        actual_prices, pred_prices, pred_timestamps, actual_timestamps = predicted_data
        
        self.__canvas.axes.clear()
        self.__canvas.axes.plot(actual_timestamps, actual_prices.values, color='r', label='Actual prices')
        self.__canvas.axes.fill_between(actual_timestamps, actual_prices.values, color='r', alpha=0.3)
        self.__canvas.axes.plot(pred_timestamps, pred_prices, color='b', label='Predicted prices')
        self.__canvas.axes.fill_between(pred_timestamps, pred_prices, color='b', alpha=0.3)
        
        self.__canvas.axes.set_title('BTC prices comparison')
        self.__canvas.axes.set_xlabel('Date')
        self.__canvas.axes.set_ylabel('Prices (USD)')
        self.__canvas.axes.legend()

        self.canvas_layout.addWidget(self.__canvas)
        self.__canvas.draw()
    
    # def display_bar_chart(self, predicted_data: tuple) -> None:
    #     pass

    def display_scatter_plot(self, predicted_data: tuple) -> None:
        self.clear_layout()
        actual_prices, pred_prices, pred_timestamps, _ = predicted_data

        self.__canvas.axes.clear()
        self.__canvas.axes.scatter(actual_prices.index, actual_prices, color='b', label='Actual prices')
        self.__canvas.axes.scatter(pred_timestamps, pred_prices, color='r', label='Predicted prices')

        self.__canvas.axes.set_title('BTC prices Actual vs Predicted')
        self.__canvas.axes.set_xlabel('Date')
        self.__canvas.axes.set_ylabel('Prices (USD)')
        self.__canvas.axes.legend()
        self.__canvas.axes.grid(True)

        self.canvas_layout.addWidget(self.__canvas)
        self.__canvas.draw()

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