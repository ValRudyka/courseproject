from PySide6.QtCore import QObject, QCoreApplication
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QMessageBox, QFileDialog

from mvc.model import Model
from mvc.view.ui_config import MAIN_MENU_DARK, MAIN_MENU_LIGHT
from mvc.view.mainmenu.mainview import MainView 
from mvc.view.interface.chartsview import ChartsView

import os

class Controller(QObject):
    def __init__(self, model: Model, main_menu: MainView, charts_view: ChartsView) -> None:
        super().__init__()
        self.model = model 
        self.main_menu = main_menu
        self.charts_view = charts_view

        self.main_menu.ui.QPushButton.clicked.connect(self.toggleStyleSheet)
        self.main_menu.ui.fetchButton.clicked.connect(self.fetch_data)
        self.main_menu.ui.predictPrices.clicked.connect(self.make_prediction)
        self.main_menu.ui.clearModel.clicked.connect(self.clear_model)
        self.main_menu.ui.loadDataset.clicked.connect(self.save_dataset)

        self.charts_view.ui.line_chart_btn.clicked.connect(self.line_chart)
        self.charts_view.ui.area_chart_btn.clicked.connect(self.area_chart)
        # self.charts_view.ui.probability_distr_btn.clicked.connect(self.probability_distribution)
        self.charts_view.ui.scatter_plot_btn.clicked.connect(self.scatter_plot)

    # charts
    def line_chart(self) -> None:
        self.charts_view.display_line_chart(self.model.get_actual_data())        

    def area_chart(self) -> None:
        self.charts_view.display_area_chart(self.model.get_actual_data())

    def probability_distribution(self) -> None:
        self.charts_view.display_distribution(self.model.get_actual_data())

    def scatter_plot(self) -> None:
        self.charts_view.display_scatter_plot(self.model.get_actual_data())

    # model and data    
    def clear_model(self) -> None:
        self.model.clear_cache(os.getenv('MODEL_CACHE_PATH'))

    def clear_data(self) -> None:
        self.model.clear_cache(os.getenv('BTC_CACHE_PATH'))

    def fetch_data(self) -> None:
        movie = QMovie('icons\loading_spinner.svg')
        
        self.main_menu.ui.label_15.setMovie(movie)
        movie.start()

        QCoreApplication.processEvents()
        self.model.get_crypto_data()
        movie.stop()
        self.main_menu.ui.label_15.setText("Success!")

    def save_dataset(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self.main_menu.ui.MainWindow, "Save Dataset", "", 
                                                "CSV files (.csv);;Excel files (.xlsx);;All files (*)", options=options)        
        
        if filename:
            try:
                ending = filename[filename.find('.'):]
                self.model.save_cache(filename, ending)
                QMessageBox.information(self.main_menu.ui.MainWindow, 'File has been saved successfully')
            except Exception as error:
                QMessageBox.warning(self.main_menu.ui.MainWindow, "Invalid file type", f"An error occured: {str(error)}")

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

    def make_prediction(self) -> None:
        interval = self.main_menu.ui.spinBox.value()
        name_interval = self.main_menu.ui.timeIntervals.currentText()

        match name_interval:
            case 'weeks':
                interval *= 7 
            case 'months':
                interval *= 31
        try:
            self.model.train_lstm_model()
            self.model.predict_model(interval)

            self.charts_view.show()
            self.charts_view.charts_shadow_effects()

            self.charts_view.display_line_chart(self.model.get_actual_data())
        except ValueError as val_e:
            msg = QMessageBox()
            msg.setText(str(val_e))
            msg.setWindowTitle("File is empty error")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 

            retval = msg.exec_()