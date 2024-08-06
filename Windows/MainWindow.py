from PySide2.QtWidgets import QHBoxLayout, QMainWindow, QWidget
from PySide2.QtCore import Qt
from Widgets import Button

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        # CENTRAL WIDGET
        self._central_widget = QWidget(self)
        self._layout = QHBoxLayout()
        self._button = Button(
            icon_path="Assets/svg/config.svg",
            icon_path_hover="Assets/svg/config-hover.svg",
            icon_path_disabled="Assets/svg/config-disabled.svg"
            
            )
        self._layout.addWidget(self._button)
        self._central_widget.setLayout(self._layout)

        # WINDOW SETUP
        self.setWindowTitle("LaSense")
        self.setCentralWidget(self._central_widget)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Produces a borderless window.
