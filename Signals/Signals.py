from PyQt5.QtCore import QObject, pyqtSignal
from config import ConfigType

class Signals(QObject):  
  
  
  on_analyze_windwow_open = pyqtSignal()
  on_analyze_window_close = pyqtSignal()
  on_recording_signal = pyqtSignal()
  on_config_signal = pyqtSignal()
  on_config_signal_done = pyqtSignal()
  on_stop_recording_signal = pyqtSignal()
  on_exit_signal = pyqtSignal()
  on_change_brightness = pyqtSignal(int)
  on_change_contrast = pyqtSignal(int)
  on_change_iso = pyqtSignal(int)
  on_change_sharpness = pyqtSignal(int)
  on_change_saturation = pyqtSignal(int)
  on_change_noise_reduction = pyqtSignal(int)
  on_set_user_settings = pyqtSignal(dict)
  # ANALYZE WINDOW
  on_analyze_signal = pyqtSignal()
  on_delete_file = pyqtSignal()
  on_analyze_signal_done = pyqtSignal()
  