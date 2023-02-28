import sys
from functools import cached_property

from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Try")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        lay = QVBoxLayout(central_widget)
        lay.addWidget(self.lineedit)

        lay.addWidget(self.stacked_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        maps = [
            {"A": (0, 0), "B": (0, 1), "C": (1, 0), "D": (1, 1)},  # first page
            {"E": (0, 0), "F": (0, 1), "G": (1, 0), "H": (1, 1)},  # second page
        ]

        for m in maps:
            page = self.create_page(m)
            self.stacked_widget.addWidget(page)

    @cached_property
    def stacked_widget(self):
        return QStackedWidget()

    @cached_property
    def lineedit(self):
        le = QLineEdit()
        le.setFixedHeight(35)
        return le

    def create_page(self, map_letters):
        page = QWidget()
        grid_layout = QGridLayout(page)
        for name, pos in map_letters.items():
            button = QPushButton(name)
            button.setFixedSize(20, 20)
            grid_layout.addWidget(button, *pos)
        return page


class Menu:
    def __init__(self, MainWindow):
        super().__init__()
        self.view = MainWindow
        self.menuBar = QMenuBar()
        self.menuBar.setGeometry(QRect(0, 0, 277, 22))
        self.view.setMenuBar(self.menuBar)
        self.open = QMenu(self.menuBar)
        self.open.setTitle("Open")
        self.menuBar.addAction(self.open.menuAction())
        self.this = QAction(self.menuBar)
        self.this.setText("This")
        self.this.setCheckable(True)
        self.open.addAction(self.this)

        self.this.triggered.connect(self.show_new_window)

    def show_new_window(self, checked):
        self.view.stacked_widget.setCurrentIndex(1 if checked else 0)


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    m = Menu(w)
    w.show()
    app.exec()


if __name__ == "__main__":
    main()