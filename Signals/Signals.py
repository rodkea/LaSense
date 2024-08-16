from PyQt5.QtCore import QObject, pyqtSignal
from config import ConfigType

class Signals(QObject):  
  
  
  on_analize_signal = pyqtSignal()
  on_analize_signal_done = pyqtSignal()
  on_record_signal = pyqtSignal()
  on_config_signal = pyqtSignal()
  on_stop_signal = pyqtSignal()
  on_exit_signal = pyqtSignal()
  on_change_brightness = pyqtSignal(int)
  on_change_contrast = pyqtSignal(int)
  on_change_iso = pyqtSignal(int)
  on_change_sharpness = pyqtSignal(int)
  on_change_saturation = pyqtSignal(int)
  on_change_noise_reduction = pyqtSignal(int)
  on_set_user_settings = pyqtSignal(ConfigType)
  