from PyQt5.QtWidgets import QFileSystemModel, QHBoxLayout, QListView, QPushButton, QSizePolicy, QStyledItemDelegate, QVBoxLayout, QWidget
from PyQt5.QtCore import QDir, QSize


class MyDelegate(QStyledItemDelegate):
    """
    MyDelegate is a custom item delegate that adjusts the size of items in a QListView.

    Methods:
    -------
    sizeHint(option, index):
        Returns the size hint for each item, setting a custom height.
      """

    def sizeHint(self, option, index):
        """
        Returns the size hint for each item, setting a custom height.

        Parameters:
        ----------
        option : QStyleOptionViewItem
            Provides style options for the item.
        index : QModelIndex
            The index of the item in the model.

        Returns:
        -------
        QSize
            The width remains the same as the default, but the height is set to 100 pixels.
        """
        size = super().sizeHint(option, index)
        return QSize(size.width(), 100)


class AnalizeWindow(QWidget):
    """
    AnalizeWindow is a custom QWidget that provides a user interface for selecting files
    from a directory and analyzing them.

    The window includes a QListView to display files from a specified directory and
    buttons for exiting and initiating the analysis process.

    Attributes:
    ----------
    _layout : QHBoxLayout
        The main horizontal layout of the window.
    _file_model : QFileSystemModel
        The model that holds the files in the specified directory.
    _lv : QListView
        The list view that displays the files.
    _right_layout : QVBoxLayout
        The layout that holds the buttons on the right side of the window.
    _btn_cancel : QPushButton
        A button to close the window.
    _btn_analyze : QPushButton
        A button to start the analysis process.

    Methods:
    -------
    __init__(parent: QWidget | None = None):
        Initializes the AnalizeWindow with a file list view and action buttons.
    _on_analize():
        Applies a custom algorithm to video to compute a score.
    """

    def __init__(self, parent: QWidget | None = None):
      super().__init__(parent)
      self.hide()
      self._layout = QHBoxLayout()
      # FILE MODEL
      self._file_model = QFileSystemModel(parent=self)
      self._file_model.setFilter(
          QDir.Filter.NoDotAndDotDot | QDir.Filter.Files)
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
      """
      Applies a custom algorithm to the selected video files to compute a biological activity score.

      The score is used to evaluate the level of biological activity in the sample.
      Once the analysis is complete, the score is typically used to determine the presence and intensity
      of biological processes in the video data.

      This method is a placeholder for the actual implementation of the analysis algorithm.
      Currently, it only prints 'ANALYZE' to the console.
      """
      print("ANALYZE")
