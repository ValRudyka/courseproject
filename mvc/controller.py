from PySide6.QtCore import QObject, QCoreApplication
from PySide6.QtWidgets import  QFileDialog

from mvc.model import Model, PDF
from mvc.view.view import View

import os

from config import TITLE, CHARTS_WIDTH, LINE_CHART_HEIGHT 
from utils import create_filepath

class Controller(QObject):
    def __init__(self, model: Model, view: View) -> None:
        super().__init__()
        self.__model = model 
        self.__view = view
        self.pdf = PDF('landscape')

        # Main menu event handlers
        self.__view.main.ui.QPushButton.clicked.connect(lambda: self.__view.toggleStyleSheet(self.__model))
        self.__view.main.ui.clearCache.clicked.connect(lambda: os.getenv("BTC_CACHE_PATH"))
        self.__view.main.ui.fetchButton.clicked.connect(self.fetch_data)
        self.__view.main.ui.predictPrices.clicked.connect(self.make_prediction)
        self.__view.main.ui.loadDataset.clicked.connect(self.save_dataset)
        self.__view.main.ui.convertPDF.clicked.connect(self.convert_to_pdf)

        # Charts window event handlers
        self.__view.charts.ui.line_chart_btn.clicked.connect(self.line_chart)
        self.__view.charts.ui.area_chart_btn.clicked.connect(self.area_chart)
        self.__view.charts.ui.scatter_plot_btn.clicked.connect(self.scatter_plot)    

    # Controls loading data from API
    def fetch_data(self) -> None:
        self.__view.main.start_movie('fetch')
        try:
            QCoreApplication.processEvents()
            self.__model.get_crypto_data()
            self.__view.main.stop_movie()
            self.__view.main.ui.label_15.setText("Success!")
        except ValueError as val_err:
            self.__view.main.stop_movie()
            self.__view.main.show_message('Fetching data error', str(val_err))

    # Saves cached data as csv or excel file
    def save_dataset(self) -> None:
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self.__view.main.ui.MainWindow, "Save Dataset", "", 
                                                "CSV files (.csv);;Excel files (.xlsx);;All files (*)", options=options)        
        
        if filename:
            try:
                ending = filename[filename.find('.'):]
                self.__model.save_cache(filename, ending)
                self.__view.main.show_message('Successfull saving', 'File has been saved successfully')
            except Exception as error:
                self.__view.main.show_message('Saving file error', str(error))

    # Converts prediction results into pdf report
    def convert_to_pdf(self) -> None:
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self.__view.main.ui.MainWindow, "Save Dataset", "", 
                                                  "PDF files (.pdf)", options=options) 

        if filename:
            try:
                self.pdf.add_page()
                self.__view.main.show_message('1st stage', 'Generating line chart...')
                self.pdf.create_title(TITLE)

                line_file = create_filepath(filename, 'line_chart.png')
                self.__model.generate_line_chart(filename=line_file, isPDF=True)
                self.pdf.write_to_pdf("1. The line chart which displays future BTC prices")
                self.pdf.ln(10)
                self.pdf.image(line_file, h=LINE_CHART_HEIGHT, w=CHARTS_WIDTH)
                self.pdf.ln(40)

                self.pdf.add_page()
                self.__view.main.show_message('2nd stage', 'Generating area chart...')
                area_file = create_filepath(filename, 'area_chart.png')
                self.__model.generate_area_chart(filename=area_file, isPDF=True)
                self.pdf.write_to_pdf(""" 2. The area chart which describes actual and future BTC prices changing over time """)
                
                self.pdf.ln(10)
                self.pdf.image(area_file, w=CHARTS_WIDTH)
                self.pdf.ln(40)

                self.pdf.add_page()
                self.__view.main.show_message('3rd stage', 'Generating scatter plot...')
                scatter_file = create_filepath(filename, 'scatter_plot.png')
                self.__model.generate_scatter_plot(filename=scatter_file, isPDF=True)
                self.pdf.write_to_pdf(""" 3. The scatter plot which compares actual and future BTC prices over time """)

                self.pdf.ln(10)
                self.pdf.image(scatter_file, w=CHARTS_WIDTH)

                self.pdf.output(filename, 'F')
                self.__view.main.show_message('Successful converting', 'File has been created successfully')    
            except Exception:
                self.__view.main.show_message('PDF converting error', 'An error occured during converting. Please try again')

    # Abstraction over displaying methods 
    def line_chart(self) -> None:
        self.__view.charts.display_line_chart(self.__model.generate_line_chart)        

    def area_chart(self) -> None:
        self.__view.charts.display_area_chart(self.__model.generate_area_chart)

    def scatter_plot(self) -> None:
        self.__view.charts.display_scatter_plot(self.__model.generate_scatter_plot)

    # Controls price prediction based on given interval
    def make_prediction(self) -> None:
        interval = self.__view.main.ui.spinBox.value()
        name_interval = self.__view.main.ui.timeIntervals.currentText()

        match name_interval:
            case 'weeks':
                interval *= 7 
            case 'months':
                interval *= 31
            case 'years':
                interval *= 365
        self.__view.main.start_movie('model')
        QCoreApplication.processEvents()

        try:
            self.__model.train_lstm_model()
            self.__model.predict_model(interval)
            self.__view.main.stop_movie()

            self.__view.main.ui.label_16.clear()
            self.__view.charts.show()
            self.__view.setup_shadow_effects('charts')            
            self.__view.charts.display_line_chart(self.__model.generate_line_chart)
        except ValueError as val_e:
            self.__view.main.stop_movie()
            self.__view.main.show_message('File is empty error', str(val_e))
        finally:
            self.__view.main.ui.label_16.clear()  
