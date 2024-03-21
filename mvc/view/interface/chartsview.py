from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from mvc.view.interface.ui_interface import Ui_ChartsWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Canvas(FigureCanvas):
    def __init__(self, width: int, height: int) -> None:
        self.fig = Figure((width, height))
        self.axes = self.fig.add_subplot()
        super(Canvas, self).__init__(self.fig)


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

    def display_line_chart(self, generate_line) -> None:
        self.clear_layout()
        self.__canvas.axes.clear()
        generate_line(self.__canvas.axes)
        self.canvas_layout.addWidget(self.__canvas)
        self.__canvas.draw()                

    def display_area_chart(self, generate_area) -> None:
        self.clear_layout()
        self.__canvas.axes.clear()
        generate_area(self.__canvas.axes)
        self.canvas_layout.addWidget(self.__canvas)
        self.__canvas.draw()        

    def display_scatter_plot(self, generate_scatter) -> None:
        self.clear_layout()
        self.__canvas.axes.clear()
        generate_scatter(self.__canvas.axes)
        self.canvas_layout.addWidget(self.__canvas)
        self.__canvas.draw()        
        