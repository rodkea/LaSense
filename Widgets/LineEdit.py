from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget

class LineEdit(QWidget):
  
  def __init__(self, text : str = "", parent : QWidget | None = None):
    super().__init__(parent)
    self._layout = QHBoxLayout()
    self.setLayout(self._layout)
    # TEXT
    self._label = QLabel(text=text, parent=self)
    self._layout.addWidget(self._label)
    # LINE EDIT
    self._le = QLineEdit(self)
    self._layout.addWidget(self._le)
    
  def set_text(self, text : str):
    self._le.setText()
    
  def text(self) -> str:
    return self._le.text()
    
    