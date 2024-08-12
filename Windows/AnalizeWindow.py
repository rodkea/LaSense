from PySide6.QtWidgets import QFileSystemModel, QHBoxLayout, QListView, QPushButton, QSizePolicy, QStyledItemDelegate, QVBoxLayout, QWidget
from PySide6.QtCore import QDir, QSize

class MyDelegate(QStyledItemDelegate):
  def sizeHint(self, option, index):
    size = super().sizeHint(option, index)
    return QSize(size.width(), 100)

class AnalizeWindow(QWidget):
  
  def __init__(self, parent : QWidget | None = None):
    super().__init__(parent)
    self.hide()
    self._layout = QHBoxLayout()
    # FILE MODEL
    self._file_model = QFileSystemModel(parent=self)
    self._file_model.setFilter(QDir.Filter.NoDotAndDotDot | QDir.Filter.Files)
    # LIST VIEW
    self._lv = QListView()
    self._lv.setModel(self._file_model)
    self._lv.setRootIndex(self._file_model.setRootPath("outputs/"))
    self._lv.setItemDelegate(MyDelegate())
    self._lv.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    self._layout.addWidget(self._lv)
    # RIGHT MENU 
    self._right_layout = QVBoxLayout()
    # SALIR BUTTON
    self._btn_cancel = QPushButton("SALIR")
    self._btn_cancel.clicked.connect(self.close)
    self._layout.addWidget(self._btn_cancel)
    # ANALYZE BUTTON
    self._btn_analyze = QPushButton("ANALIZAR")
    self._btn_analyze.clicked.connect(self._on_analize)
    self._layout.addWidget(self._btn_analyze)
    # LAYOUT
    self._layout.addLayout(self._right_layout)
    self.setLayout(self._layout)
    self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    
    
  def _on_analize(self):
    print("ANALYZE")    