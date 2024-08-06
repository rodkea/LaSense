from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget
from PySide6.QtCore import Qt
from Components import ButtonsMenu

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        # CENTRAL WIDGET
        self._central_widget = QWidget(self)
        self._layout = QHBoxLayout()
        self._button_menu = ButtonsMenu(parent=self._central_widget)
        self._layout.addWidget(self._button_menu)
        self._central_widget.setLayout(self._layout)

        # WINDOW SETUP
        self.setWindowTitle("LaSense")
        self.setCentralWidget(self._central_widget)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Produces a borderless window.
