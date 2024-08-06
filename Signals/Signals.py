from PySide6.QtCore import QObject, Signal

class Signals(QObject):  
  
  on_analize_signal = Signal()
  on_analize_signal_done = Signal()
  on_record_signal = Signal()
  on_config_signal = Signal()
  on_stop_signal = Signal()
  
  