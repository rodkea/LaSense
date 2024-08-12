from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from Widgets import Button
from Signals import Signals
class ButtonsMenu(QWidget):
  
  def __init__(self, signals : Signals, parent: QWidget | None = None):
        
    super().__init__(parent)
    self._layout = QVBoxLayout()
    self._layout.setSpacing(20)
    # SIGNALS
    self._signals = signals
    # RECORD BUTTON
    self._record_btn = Button(
      icon_path="Assets/svg/record.svg",
      icon_path_hover="Assets/svg/record-hover.svg",
      icon_path_disabled="Assets/svg/record-disabled.svg"
    )
    self._layout.addWidget(self._record_btn)
    # ANALIZE BUTTON
    self._analyze_btn = Button(
      icon_path="Assets/svg/ml.svg",
      icon_path_hover="Assets/svg/ml-hover.svg",
      icon_path_disabled="Assets/svg/ml-disabled.svg",
      signal=self._signals.on_analize_signal  
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