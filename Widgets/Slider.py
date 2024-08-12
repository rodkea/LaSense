from PyQt5.QtWidgets import QLabel, QSlider, QWidget, QHBoxLayout
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, pyqtSignal
from Signals import Signals

class Slider(QWidget):
  
  def __init__(self, icon_path : str, signal : pyqtSignal, tooltip : str = "",
               min_value : int = 0, max_value : int = 100,
               step : int = 1, label_format: str = "f'{value}'",
               parent : QWidget | None = None):
    super().__init__(parent)
    self._signal = signal
    self._layout = QHBoxLayout(self)
    self._svg = QSvgWidget(icon_path)
    self._svg.setFixedSize(35, 35)
    self.setToolTip(tooltip)
    self._slider = QSlider(Qt.Orientation.Horizontal)
    self._slider.setRange(min_value, max_value)
    self._slider.setSingleStep(step)
    self._slider.valueChanged.connect(self.value_changed)
    self._label_format = label_format
    self._label = QLabel()
    self._label_format = label_format
    self._update_label()    
    self._layout.addWidget(self._svg)
    self._layout.addWidget(self._slider)
    self._layout.addWidget(self._label)
    
  def set_value(self, value : int):
    self._slider.setValue(value)
    self._label.setText(self._label_format.format(value=self._slider.value())) 
    
  def value_changed(self):
    self._update_label() 
    
  def _update_label(self):
      value = self._slider.value()
      try:
          # Evalúa el formato del f-string
          label_text = eval(self._label_format)
      except Exception as e:
          label_text = str(e)
      self._label.setText(label_text)
      self._signal.emit(value)
    
    
    