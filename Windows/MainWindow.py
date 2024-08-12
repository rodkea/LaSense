from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget
from PySide6.QtCore import Qt
from Components import ButtonsMenu
from Signals import Signals
from .ConfigPopup import ConfigPopup
from .AnalizeWindow import AnalizeWindow
class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        # CENTRAL WIDGET
        self._central_widget = QWidget(self)
        self._layout = QHBoxLayout()
        # SIGNALS
        self._signals = Signals()
        self._signals.on_exit_signal.connect(self.close)
        self._signals.on_analize_signal.connect(self._on_analyze)
        # WIDGETS
        self._button_menu = ButtonsMenu(signals=self._signals, parent=self._central_widget)
        self._layout.addWidget(self._button_menu)
        self._central_widget.setLayout(self._layout)
        # WINDOWS
        self._analyze_window = AnalizeWindow()
        self._layout.addWidget(self._analyze_window)
        # POPUPS
        self._config_popup = ConfigPopup(parent=self)
        self._signals.on_config_signal.connect(self.on_config)
        # WINDOW SETUP
        self.setWindowTitle("LaSense")
        self.setCentralWidget(self._central_widget)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Produces a borderless window.

    def on_config(self):
        self._config_popup.show()
        
    def _on_analyze(self):
        self._analyze_window.show()
        