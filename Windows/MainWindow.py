from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QWidget, QSizePolicy
from PyQt5.QtCore import Qt
from Components import ButtonsMenu
from Signals import Signals
from Camera import Camera, CameraPreview, Resolution
from .ConfigPopup import ConfigPopup
from .AnalizeWindow import AnalizeWindow

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs) 
        # CENTRAL WIDGET
        self._central_widget = QWidget(self)
        self._layout = QHBoxLayout()
        self._central_widget.setLayout(self._layout)

        # SIGNALS
        self._signals = Signals()
        self._signals.on_exit_signal.connect(self.close)
        self._signals.on_analize_signal.connect(self._on_analyze)
        # CAMERA 
        self._camera = Camera(Resolution.FHD, signals=self._signals)
        # WIDGETS
        self._button_menu = ButtonsMenu(signals=self._signals)
        self._layout.addWidget(self._button_menu)
        # PREVIEW
        self._prev_cam_widget = None
        self._prev_cam_widget = CameraPreview(
            self._camera,
            width=Resolution.FHD.width,
            height=Resolution.FHD.height,
            keep_ar=True
        )
        self._prev_cam_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._layout.addWidget(self._prev_cam_widget)
        # WINDOWS
        self._analyze_window = AnalizeWindow()
        self._layout.addWidget(self._analyze_window)
        # POPUPS
        self._config_popup = ConfigPopup(signals=self._signals, parent=self)
        self._signals.on_config_signal.connect(self.on_config)
        # WINDOW SETUP
        self.setWindowTitle("LaSense")
        self.setCentralWidget(self._central_widget)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Produces a borderless window.
        self._camera.start()

    def on_config(self):
        self._config_popup.show()
        
    def _on_analyze(self):
        self._analyze_window.show()

        