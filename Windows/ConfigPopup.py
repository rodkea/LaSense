from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtCore import Qt

class ConfigPopup(QDialog):
  
  def __init__(self, parent : QWidget | None = None):
    super().__init__(parent)
    self.resize(600,300)
    self.setWindowTitle("Configuracón")
    self.setModal(True)
    self.setWindowFlag(Qt.WindowType.Widget) 
    self.setWindowFlag(Qt.BypassWindowManagerHint)
    
    