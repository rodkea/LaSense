from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class ValueBox(QWidget):
  
  def __init__(self, label: str, 
               value : float | int | None = None,
               parent: QWidget | None = None):
    super().__init__(parent=parent)
    # LAYOUT
    self._layout = QVBoxLayout()
    self._layout.setAlignment(Qt.AlignHCenter) 
    self.setLayout(self._layout)
    
    # LABEL
    self._label = QLabel(text=label)
    self._label.setAlignment(Qt.AlignHCenter)
    self._layout.addWidget(self._label)
    # VALUE
    self._value = QLabel()
    self._layout.addWidget(self._value)
    self._value.setAlignment(Qt.AlignHCenter)
    if value:
      self._value.setText(str(value))
    else:
      self._value.setText("-")
  
  def set_value(self, value : float | int):
    self._value.setText(f"{value:.3f}")
    
  def clear_value(self):
    self._value.setText("-")
    
    
    