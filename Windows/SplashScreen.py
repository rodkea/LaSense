from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class SplashScreen(QSplashScreen):
  """
    SplashScreen is a custom splash screen class that displays a frameless window
    with a specified image when the application starts.

    Attributes:
    ----------
    _pixmap : QPixmap
        A QPixmap object that holds the splash screen image.

    Methods:
    -------
    __init__():
        Initializes the splash screen, sets it to be borderless, loads the image,
        and scales it to the desired dimensions.
  """
  def __init__(self):    
    super().__init__()
    self.setWindowFlag(Qt.FramelessWindowHint)  # Produces a borderless window.
    self._pixmap = QPixmap("Assets/jpg/LABI.jpg")
    self._pixmap = self._pixmap.scaled(800, 450)
    self.setPixmap(self._pixmap)