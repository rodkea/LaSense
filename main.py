import sys
import os
from Windows import MainWindow, SplashScreen
from PyQt5.QtWidgets import QApplication
  
if __name__ == "__main__":
  app = QApplication(sys.argv)
  
  splash = SplashScreen()
  splash.show()
  w = MainWindow()
  w.showMaximized()
  splash.finish(w)
  sys.exit(app.exec())