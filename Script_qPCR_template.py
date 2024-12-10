
'''
The GUI codes of selecting the number of plates and the file location. 
'''
from PyQt6.QtCore import (QObject, Qt, QAbstractTableModel, QModelIndex)
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
        QApplication,
        QMainWindow,
        QPushButton,
        QLabel,
        QComboBox,
        QGridLayout,
        QWidget, 
        QFileDialog, 
        QTableWidgetItem,
        QMessageBox
        )

import sys

import pandas as pd

# create a QtableModel
class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Select the excel files needed to be transfered")
        self.setGeometry(250, 250, 300, 250)

        layout = QGridLayout()

        widget1 = QLabel("How many plates? ")

        widget2 = QComboBox()
        widget2.addItems(["1", "2", "3", "4", "5", "6", "7"])

        # Sends the current index position of the selected item.
        widget2.currentIndexChanged.connect(self.index_changed)

        # The button doesn't work before, but after changing the btn to global viarable and delete widget3, it works. 
        # Don't change the shit mountain anymore. It works well now so then it will work forever. 
        global btn
        btn = QPushButton(self)
        btn.setText("Select the file")
        btn.clicked.connect(self.openFileDialog)

        # addWidget (*Widget, row, column, rowspan, colspan)
        layout.addWidget(widget1, 0, 0, 1, 2)
        layout.addWidget(widget2, 0, 1, 1, 1)
        layout.addWidget(btn, 1, 1, 1, 1)
        self.setLayout(layout)
        
    
    def openFileDialog(self):
        # Open a file dialog to select an Excel file
        global fname
        fname = QFileDialog.getOpenFileName(self, "Open Excel File", "${HOME}", "*.xlsx")

        if fname: 
            # Read the selected Excel file using pandas
            fname = ''.join(fname)
            print(fname)
            parts = fname.split('*')
            path = parts[0]
            df = pd.read_excel(path)
            print(df.head())


    def index_changed(self, i): # i is an int
        global n_plate
        n_plate = i
        print(n_plate)
        # read the number of the plates, remember python count the index from 0, so the number is index + 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Create a Qt widget as a window
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


'''
End of GUI
Start to transfer excel
'''
'''
# Get the RGB code of the background in the excel for the primers
import sys
from openpyxl import load_workbook
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QVBoxLayout, 
    QPushButton, 
    QFileDialog, 
    QTableWidget, 
    QTableWidgetItem, 
    QMessageBox
    )


class ExcelColorSelector(QWidget): 
    def __init__(self, fname):
        super().__init__()
        self.filePath = fname
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Excel Cell Color Selector')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Table widget to display Excel data
        self.tableWidget = QTableWidget(self)
        layout.addWidget(self.tableWidget)

        # Button to get the RGB colors of selected cells
        self.colorButton = QPushButton('Get RGB Colors of Selected Cells', self)
        self.colorButton.clicked.connect(self.getSelectedCellColors)
        layout.addWidget(self.colorButton)

        # Set the layout
        self.setLayout(layout)
        
        # Load the Excel data into the table
        self.loadExcelData()


def loadExcelData(self):
        # Read the Excel file into a pandas DataFrame
        self.df = pd.read_excel(self.filePath)
        
        # Set the table dimensions
        self.tableWidget.setRowCount(self.df.shape[0])
        self.tableWidget.setColumnCount(self.df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(self.df.columns)
        
        # Populate the table with data from the DataFrame
        for i in range(self.df.shape[0]):
            for j in range(self.df.shape[1]):
                item = QTableWidgetItem(str(self.df.iat[i, j]))
                self.tableWidget.setItem(i, j, item)
        
        # Allow selecting cells
        self.tableWidget.setSelectionMode(QTableWidget.SelectionMode.MultiSelection)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectItems)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Provide the file path directly here
    file_path = 'your_file.xlsx'  # Replace with your actual Excel file path
    
    ex = ExcelColorSelector(file_path)
    ex.show()
    sys.exit(app.exec())
'''