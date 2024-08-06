import sys
from Windows import MainWindow
from PySide2.QtWidgets import QApplication

if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = MainWindow()
  w.showMaximized()
  sys.exit(app.exec_())