from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from Widgets import Button
from Signals import Signals
class ButtonsMenu(QWidget):
  
  def __init__(self, signals : Signals, parent: QWidget | None = None):
        
    super().__init__(parent)
    self._layout = QVBoxLayout()
    self._layout.setSpacing(20)
    # SIGNALS
    self._signals = signals
    self._signals.on_config_signal.connect(self._on_config)
    self._signals.on_config_signal_done.connect(self._on_config_done)
    self._signals.on_analyze_signal.connect(self._on_analyze)
    self._signals.on_analyze_signal_done.connect(self._on_analyze_done)
    self._signals.on_recording_signal.connect(self._on_recording)
    self._signals.on_stop_recording_signal.connect(self._on_stop_recording)
    # RECORD BUTTON
    self._record_btn = Button(
      icon_path="Assets/svg/record.svg",
      icon_path_hover="Assets/svg/record-hover.svg",
      icon_path_disabled="Assets/svg/record-disabled.svg",
      signal=self._signals.on_recording_signal
    )
    self._layout.addWidget(self._record_btn)
    # STOP RECORD BUTTON 
    self._stop_record_btn = Button(
      icon_path="Assets/svg/stop.svg",
      icon_path_hover="Assets/svg/stop-hover.svg",
      signal=self._signals.on_stop_recording_signal
    )
    self._stop_record_btn.hide()
    self._layout.addWidget(self._stop_record_btn)
    # ANALIZE BUTTON
    self._analyze_btn = Button(
      icon_path="Assets/svg/ml.svg",
      icon_path_hover="Assets/svg/ml-hover.svg",
      icon_path_disabled="Assets/svg/ml-disabled.svg",
      signal=self._signals.on_analyze_signal  
    )
    self._layout.addWidget(self._analyze_btn)
    # CONFIG BUTTON
    self._config_btn = Button(
      icon_path="Assets/svg/config.svg",
      icon_path_hover="Assets/svg/config-hover.svg",
      icon_path_disabled="Assets/svg/config-disabled.svg",
      signal=self._signals.on_config_signal    
    )
    self._layout.addWidget(self._config_btn)
    # EXIT BUTTON
    self._exit_btn = Button(
      icon_path="Assets/svg/exit.svg",
      icon_path_hover="Assets/svg/exit-hover.svg",
      icon_path_disabled="Assets/svg/exit-disabled.svg",
      signal=self._signals.on_exit_signal    
    )
    self._layout.addWidget(self._exit_btn)
    # LAYOUT
    self.setLayout(self._layout)
    self.setSizePolicy(
      QSizePolicy.Policy.Minimum,
      QSizePolicy.Policy.Fixed
    )

  def _on_config(self):
    self._analyze_btn.set_disabled()
    self._record_btn.set_disabled()
    self._exit_btn.set_disabled()

  def _on_config_done(self):
    self._analyze_btn.set_enabled()
    self._record_btn.set_enabled()
    self._exit_btn.set_enabled()

  def _on_analyze(self):
    self._config_btn.set_disabled()
    self._record_btn.set_disabled()
    self._exit_btn.set_disabled()

  def _on_analyze_done(self):
    self._config_btn.set_enabled()
    self._record_btn.set_enabled()
    self._exit_btn.set_enabled()

  def _on_recording(self):
    self._config_btn.set_disabled()
    self._analyze_btn.set_disabled()
    self._exit_btn.set_disabled()
    self._record_btn.set_disabled()
    self._record_btn.hide()
    self._stop_record_btn.show()

  def _on_stop_recording(self):
    self._config_btn.set_enabled()
    self._analyze_btn.set_enabled()
    self._exit_btn.set_enabled()
    self._record_btn.set_enabled()
    self._stop_record_btn.hide()
    
    self._record_btn.show()
    
  
