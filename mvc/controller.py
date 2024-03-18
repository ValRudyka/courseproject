from PySide6.QtCore import QObject, QCoreApplication
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QMessageBox, QFileDialog

from mvc.model import Model, PDF
from mvc.view.ui_config import MAIN_MENU_DARK, MAIN_MENU_LIGHT
from mvc.view.mainmenu.mainview import MainView 
from mvc.view.interface.chartsview import ChartsView

from config import TITLE
from utils import create_filepath

import os

class Controller(QObject):
    def __init__(self, model: Model, main_menu: MainView, charts_view: ChartsView) -> None:
        super().__init__()
        self.model = model 
        self.main_menu = main_menu
        self.charts_view = charts_view
        self.pdf = PDF()

        self.main_menu.ui.QPushButton.clicked.connect(self.toggleStyleSheet)
        self.main_menu.ui.fetchButton.clicked.connect(self.fetch_data)
        self.main_menu.ui.predictPrices.clicked.connect(self.make_prediction)
        self.main_menu.ui.loadDataset.clicked.connect(self.save_dataset)
        self.main_menu.ui.convertPDF.clicked.connect(self.convert_to_pdf)

        self.charts_view.ui.line_chart_btn.clicked.connect(self.line_chart)
        self.charts_view.ui.area_chart_btn.clicked.connect(self.area_chart)
        self.charts_view.ui.scatter_plot_btn.clicked.connect(self.scatter_plot)

    # charts
    def line_chart(self) -> None:
        self.charts_view.display_line_chart(self.model.generate_line_chart)        

    def area_chart(self) -> None:
        self.charts_view.display_area_chart(self.model.generate_area_chart)

    # def probability_distribution(self) -> None:
    #     self.charts_view.display_distribution(self.model.generate_)

    def scatter_plot(self) -> None:
        self.charts_view.display_scatter_plot(self.model.generate_scatter_plot)

    # model and data    
    def clear_data(self) -> None:
        self.model.clear_cache(os.getenv('BTC_CACHE_PATH'))

    def fetch_data(self) -> None:
        movie = QMovie('icons\loading_spinner.svg')
        
        self.main_menu.ui.label_15.setMovie(movie)
        movie.start()

        try:
            QCoreApplication.processEvents()
            self.model.get_crypto_data()
            movie.stop()
            self.main_menu.ui.label_15.setText("Success!")
        except ValueError as val_err:
            movie.stop()
            self.main_menu.ui.label_15.setText(str(val_err))

    def save_dataset(self) -> None:
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

    def convert_to_pdf(self) -> None:
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self.main_menu.ui.MainWindow, "Save Dataset", "", 
                                                  "PDF files (.pdf)", options=options) 

        if filename:
            try:
                self.pdf.add_page()
                self.pdf.create_title(TITLE)

                self.main_menu.ui.label_14.setText("Constructing line chart...")
                line_file = create_filepath(filename, 'line_chart.png')
                self.model.generate_line_chart(filename=line_file, isPDF=True)
                self.pdf.write_to_pdf("1. The line chart which displays future BTC prices")
                self.pdf.ln(15)

                self.pdf.image(line_file, w=190)
                self.pdf.ln(40)

                self.pdf.add_page()
                self.main_menu.ui.label_14.setText("Constructing area chart...")
                area_file = create_filepath(filename, 'area_chart.png')
                self.model.generate_area_chart(filename=area_file, isPDF=True)
                self.pdf.write_to_pdf(""" 2. The area chart which describes actual and future BTC prices changing over time """)
                
                self.pdf.ln(15)
                self.pdf.image(area_file, w=190)
                self.pdf.ln(40)

                self.pdf.add_page()
                self.main_menu.ui.label_14.setText("Constructing scatter plot...")
                scatter_file = create_filepath(filename, 'scatter_plot.png')
                self.model.generate_scatter_plot(filename=scatter_file, isPDF=True)
                self.pdf.write_to_pdf(""" 3. The scatter plot which compares actual and future BTC prices over time """)
                
                self.main_menu.ui.label_14.setText("Creating pdf report...")
                self.pdf.ln(15)
                self.pdf.image(scatter_file, w=190)

                self.pdf.output(filename, 'F')
                self.main_menu.ui.label_14.setText("PDF report created successfully...")
            except Exception:
                self.main_menu.ui.label_14.setText("An error occured during generating. Please try again!")

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

            self.charts_view.display_line_chart(self.model.generate_line_chart)
        except ValueError as val_e:
            msg = QMessageBox()
            msg.setText(str(val_e))
            msg.setWindowTitle("File is empty error")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 

            retval = msg.exec_()