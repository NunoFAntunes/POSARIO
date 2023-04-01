import sys
from PyQt6.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt6.QtGui import QFont, QPalette, QColor
import random


class TableWindow(QMainWindow):                           # <===
    def __init__(self, table_number):
        super().__init__()
        self.setWindowTitle("Table " + str(table_number))
        self.setFixedSize(1920, 1080)