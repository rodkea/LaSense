import sys
import os
from Windows import MainWindow, SplashScreen
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication

if __name__ == "__main__":
  # os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard" ##PROBAR CON TOUCH
  app = QApplication(sys.argv)
  QGuiApplication.inputMethod()  
  splash = SplashScreen()
  splash.show()
  w = MainWindow()
  w.showMaximized()
  splash.finish(w)
  sys.exit(app.exec())