from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSizePolicy, QSpacerItem
from Widgets import Button
from Signals import Signals

class AnalyzeButtonsMenu(QWidget):
  
  def __init__(self, signals : Signals, parent: QWidget | None = None):
    super().__init__(parent)
    self._layout = QHBoxLayout()
    self._layout.setSpacing(20)
    self.setLayout(self._layout)
    # SIGNALS
    self._signals = signals
    self._signals.on_analyze_signal.connect(self._on_analyze)
    self._signals.on_analyze_signal_done.connect(self._on_analyze_done)
    # SPACER
    self._layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding))
    # ANALYZE ITEM
    self._analyze_btn = Button(
      icon_path="Assets/svg/process_frame.svg",
      icon_path_hover="Assets/svg/process_frame-hover.svg",
      icon_path_disabled="Assets/svg/process_frame-disabled.svg",
      width=50,
      height=50,
      signal=self._signals.on_analyze_signal   
    )
    self._layout.addWidget(self._analyze_btn)
    # DELETE BUTTON
    self._delete_btn = Button(
      icon_path="Assets/svg/delete.svg",
      icon_path_hover="Assets/svg/delete-hover.svg",
      icon_path_disabled="Assets/svg/delete-disabled.svg",
      width=50,
      height=50,
      signal=self._signals.on_delete_file      
    )
    self._layout.addWidget(self._delete_btn)
    # CANCEL BUTTON
    self._cancel_btn = Button(
      icon_path="Assets/svg/cancel.svg",
      icon_path_hover="Assets/svg/cancel-hover.svg",
      icon_path_disabled="Assets/svg/cancel-disabled.svg",
      width=50,
      height=50,
      signal= self._signals.on_analyze_window_close 
    )
    self._layout.addWidget(self._cancel_btn)
    # SPACER
    self._layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding))
    
    self.setSizePolicy(
      QSizePolicy.Policy.Minimum,
      QSizePolicy.Policy.Fixed
    )
  
  def _on_analyze(self):
    self._delete_btn.set_disabled()
    self._cancel_btn.set_disabled()
    self._analyze_btn.set_disabled()
  
  def _on_analyze_done(self):
    self._delete_btn.set_enabled()
    self._cancel_btn.set_enabled()
    self._analyze_btn.set_enabled()
    