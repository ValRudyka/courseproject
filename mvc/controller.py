from PySide6.QtCore import QObject, QCoreApplication
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QMessageBox, QFileDialog

from mvc.model import Model, PDF
from mvc.view.view import View

from config import TITLE, CHARTS_WIDTH, LOADING_SPINNER_PATH
from utils import create_filepath

class Controller(QObject):
    def __init__(self, model: Model, view: View) -> None:
        super().__init__()
        self.model = model 
        self.view = view
        self.pdf = PDF()

        self.view.main.ui.QPushButton.clicked.connect(lambda: self.view.toggleStyleSheet(self.model))
        self.view.main.ui.fetchButton.clicked.connect(self.fetch_data)
        self.view.main.ui.predictPrices.clicked.connect(self.make_prediction)
        self.view.main.ui.loadDataset.clicked.connect(self.save_dataset)
        self.view.main.ui.convertPDF.clicked.connect(self.convert_to_pdf)

        self.view.charts.ui.line_chart_btn.clicked.connect(self.line_chart)
        self.view.charts.ui.area_chart_btn.clicked.connect(self.area_chart)
        self.view.charts.ui.scatter_plot_btn.clicked.connect(self.scatter_plot)    

    def fetch_data(self) -> None:
        self.view.main.start_movie(LOADING_SPINNER_PATH, self.view.main.ui.label_15)
        try:
            QCoreApplication.processEvents()
            self.model.get_crypto_data()
            self.view.main.stop_movie()
            self.view.main.ui.label_15.setText("Success!")
        except ValueError as val_err:
            self.view.main.stop_movie()
            self.view.main.show_message('Fetching data error', str(val_err))

    def save_dataset(self) -> None:
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self.view.main.ui.MainWindow, "Save Dataset", "", 
                                                "CSV files (.csv);;Excel files (.xlsx);;All files (*)", options=options)        
        
        if filename:
            try:
                ending = filename[filename.find('.'):]
                self.model.save_cache(filename, ending)
                QMessageBox.information(self.view.main.ui.MainWindow, 'File has been saved successfully')
            except Exception as error:
                self.view.main.show_message('Saving file error', str(error))

    def convert_to_pdf(self) -> None:
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self.view.main.ui.MainWindow, "Save Dataset", "", 
                                                  "PDF files (.pdf)", options=options) 

        if filename:
            try:
                self.pdf.add_page()
                self.pdf.create_title(TITLE)

                # self.view.main.ui.label_14.setText("Constructing line chart...")
                line_file = create_filepath(filename, 'line_chart.png')
                self.model.generate_line_chart(filename=line_file, isPDF=True)
                self.pdf.write_to_pdf("1. The line chart which displays future BTC prices")
                self.pdf.ln(15)

                self.pdf.image(line_file, w=CHARTS_WIDTH)
                self.pdf.ln(40)

                self.pdf.add_page()
                # self.view.main.ui.label_14.setText("Constructing area chart...")
                area_file = create_filepath(filename, 'area_chart.png')
                self.model.generate_area_chart(filename=area_file, isPDF=True)
                self.pdf.write_to_pdf(""" 2. The area chart which describes actual and future BTC prices changing over time """)
                
                self.pdf.ln(15)
                self.pdf.image(area_file, w=CHARTS_WIDTH)
                self.pdf.ln(40)

                self.pdf.add_page()
                # self.view.main.ui.label_14.setText("Constructing scatter plot...")
                scatter_file = create_filepath(filename, 'scatter_plot.png')
                self.model.generate_scatter_plot(filename=scatter_file, isPDF=True)
                self.pdf.write_to_pdf(""" 3. The scatter plot which compares actual and future BTC prices over time """)
                
                # self.view.main.ui.label_14.setText("Creating pdf report...")
                self.pdf.ln(15)
                self.pdf.image(scatter_file, w=CHARTS_WIDTH)

                self.pdf.output(filename, 'F')
                self.view.main.show_message('Successful converting', 'File has been created successfully')    
            except Exception:
                self.view.main.show_message('PDF converting error', 'An error occured during converting. Please try again')

    def line_chart(self) -> None:
        self.view.charts.display_line_chart(self.model.generate_line_chart)        

    def area_chart(self) -> None:
        self.view.charts.display_area_chart(self.model.generate_area_chart)

    def scatter_plot(self) -> None:
        self.view.charts.display_scatter_plot(self.model.generate_scatter_plot)

    def make_prediction(self) -> None:
        interval = self.view.main.ui.spinBox.value()
        name_interval = self.view.main.ui.timeIntervals.currentText()

        match name_interval:
            case 'weeks':
                interval *= 7 
            case 'months':
                interval *= 31
            case 'years':
                interval *= 365
        self.view.main.start_movie(LOADING_SPINNER_PATH, self.view.main.ui.label_16)
        try:
            QCoreApplication.processEvents()
            # self.view.main.ui.label_13.setText("Training the model...")
            self.model.train_lstm_model()
            self.view.main.start_movie(LOADING_SPINNER_PATH, self.view.main.ui.label_16)
            QCoreApplication.processEvents()
            # self.view.main.ui.label_13.setText("Predicting prices...")
            self.model.predict_model(interval)
            # self.view.main.ui.label_13.setText("Prices predicted successfully...")
            self.view.main.stop_movie()

            self.view.charts.show()
            self.view.setup_shadow_effects('charts')
            
            self.view.charts.display_line_chart(self.model.generate_line_chart)
        except ValueError as val_e:
            self.view.main.stop_movie()
            self.view.main.show_message('File is empty error', str(val_e))  
