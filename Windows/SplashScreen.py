from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class SplashScreen(QSplashScreen):
  
  def __init__(self):
    super().__init__()
    self.setWindowFlag(Qt.FramelessWindowHint)  # Produces a borderless window.
    self._pixmap = QPixmap("Assets/jpg/LABI.jpg")
    self._pixmap = self._pixmap.scaled(800, 450)
    self.setPixmap(self._pixmap)