from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QWidget, QSizePolicy
from PyQt5.QtCore import Qt
from Components import ButtonsMenu
from Signals import Signals
from Camera import Camera, CameraPreview, Resolution
from .ConfigPopup import ConfigPopup
from .AnalizeWindow import AnalizeWindow
from config import ConfigType, read_config, USER_CONFIG_PATH

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
        self._signals.on_analyze_windwow_open.connect(self._on_analyze)
        self._signals.on_analyze_window_close.connect(self._on_analyze_done)
        self._signals.on_config_signal.connect(self._on_config)
        self._signals.on_config_signal_done.connect(self._on_config_done)
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
        self._analyze_window = AnalizeWindow(signals=self._signals)
        self._layout.addWidget(self._analyze_window)
        # POPUPS
        self._config_popup = ConfigPopup(signals=self._signals, parent=self)
        
        # WINDOW SETUP
        self.setWindowTitle("LaSense")
        self.setCentralWidget(self._central_widget)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Produces a borderless window.
        self._camera.start()
        self._load_config(USER_CONFIG_PATH)

    def _on_config(self):
        self._config_popup.show()
        
    def _on_config_done(self):
        self._config_popup.hide()
        
    def _on_analyze(self):
        self._prev_cam_widget.hide()
        self._analyze_window.show()
    
    def _on_analyze_done(self):
        self._analyze_window.hide()
        self._prev_cam_widget.show()
        
    def _load_config(self, user_config_path : str) :
        user_config = read_config(user_config_path)
        self._signals.on_set_user_settings.emit(user_config)


        