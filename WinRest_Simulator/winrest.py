import sys
from PyQt6.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt6.QtGui import QFont, QPalette, QColor
import random


class TableWindow(QMainWindow):                           # <===
    def __init__(self, table_number):
        super().__init__()
        self.setWindowTitle("Table " + str(table_number))
        self.setFixedSize(1920, 1080)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setFixedSize(1920, 1080)
        
    def style_button(self, button, is_table_button=False):
        # Set the button properties
        button.setFixedHeight(100)
        if is_table_button:
            button.setStyleSheet("background-color:rgb(93, 148, 193); \
                font-size: 18px; \
                    font-weight: bold; \
                        color: white; \
                            border-radius: 15px; \
                                margin-left: 30px;\
                                    margin-right: 30px;")
        else:
            button.setStyleSheet("background-color:rgb(93, 148, 193); \
                font-size: 18px; \
                    font-weight: bold; \
                        color: white; \
                            border-radius: 15px;")
            
    
    def create_left_layout(self, layout):
        divisoes = ['Balcão', 'Bar', 'Sala', 'Delivery']
        left_layout = QVBoxLayout()
        
        # Create the list widget
        lista_de_divisoes = QListWidget()
        for div in divisoes:
            lista_de_divisoes.addItem(div)
        left_layout.addWidget(lista_de_divisoes, 8)
        
        buttons_layout = QHBoxLayout()
        despacho_button = QPushButton('Despacho')
        consumo_button = QPushButton('Consumo Próprio')
        self.style_button(despacho_button)
        self.style_button(consumo_button)
        
        buttons_layout.addWidget(despacho_button)
        buttons_layout.addWidget(consumo_button)
        
        left_layout.addLayout(buttons_layout, 4)
        
        layout.addLayout(left_layout)
        
    def create_tables_layout(self, layout):
        # Create a grid layout with 6 rows and 6 columns
        tables_layout = QGridLayout()
        # Create a button for each grid cell
        for i in range(4):
            for j in range(4):
                button = QPushButton(f"{random.randrange(100)}")
                self.style_button(button, True)
                button.clicked.connect(self.buttonClicked)
                tables_layout.addWidget(button, i, j)
        layout.addLayout(tables_layout, 5)


    def initUI(self):
        
        self.setWindowTitle('WinRest Simulator')
        
        # Create a vertical box layout to hold the list and the grid
        layout = QHBoxLayout()
        
        self.create_left_layout(layout)
        self.create_tables_layout(layout)

        # Set the layout and window properties
        self.setLayout(layout)
        
        self.showMaximized()
        
    def openNewWindow(self, table_number):
        self.w = TableWindow(table_number)
        self.w.show()
    
    def buttonClicked(self):
            # Get the sender button's text and display it
            button = self.sender()
            print(f"Button clicked: {button.text()}")
            self.openNewWindow(button.text())
        
    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

            event.accept()
        else:

            event.ignore()



def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    #window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()