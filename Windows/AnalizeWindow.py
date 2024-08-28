import os
from PyQt5.QtWidgets import QFileSystemModel, QSpacerItem, QHBoxLayout, QListView, QMessageBox, QSizePolicy, QStyledItemDelegate, QVBoxLayout, QWidget
from PyQt5.QtCore import QDir, QSize, Qt, QThread
from Signals import Signals
from descriptors import d_fuzzy
from Components import AnalyzeButtonsMenu
from numpy import median, mean
from Widgets import MplCanvas, ValueBox

class Worker(QThread):
    

    def __init__(self, path, canva : MplCanvas, mean_vb : ValueBox, median_vb : ValueBox, parent=None):
        super().__init__(parent)
        self._canva = canva
        self._path = path
        self._mean_vb = mean_vb
        self._median_vb = median_vb

    def run(self):
        self._mean_vb.clear_value()
        self._median_vb.clear_value()
        if self._canva. cb:
            self._canva.cb.remove()
        result = d_fuzzy(self._path, 1920, 1080)
        self._mean_vb.set_value(mean(result))
        self._median_vb.set_value(median(result))
        cax = self._canva.axes.imshow(result, cmap='viridis')
        self._canva.cb = self._canva.figure.colorbar(cax, ax=self._canva.axes)
        self._canva.draw()
        

class MyDelegate(QStyledItemDelegate):
    """
    MyDelegate is a custom item delegate that adjusts the size of items in a QListView.

    Methods:
    -------
    sizeHint(option, index):
        Returns the size hint for each item, setting a custom height.
      """

    def sizeHint(self, option, index):
        """-
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

    def __init__(self, signals = Signals, parent: QWidget | None = None):
      super().__init__(parent)
      self.hide()
      self._layout = QHBoxLayout()
      # SIGNALS
      self._signals = signals      
      self._signals.on_analyze_signal.connect(self._on_analize)
      self._signals.on_delete_file.connect(self._on_delete)
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
     # CANVAS
      self._canvas = MplCanvas()
      self._right_layout.addWidget(self._canvas)
      # STATS
      self._stats_layout = QHBoxLayout()
      self._mean_vb = ValueBox("MEDIA") 
      self._stats_layout.addWidget(self._mean_vb)
      self._median_vb = ValueBox("MEDIANA")
      self._stats_layout.addWidget(self._median_vb)
      self._right_layout.addLayout(self._stats_layout)
      # SPACER
      self._right_layout.addSpacerItem(QSpacerItem(20, 20,vPolicy= QSizePolicy.Policy.MinimumExpanding))    
      # BUTTONS MENU
      self._buttons_menu = AnalyzeButtonsMenu(signals=signals)
      self._right_layout.addWidget(self._buttons_menu)      
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
        indexes = self._lv.selectedIndexes()
        if indexes:
            index = indexes[0]
            item_text = self._file_model.data(index, Qt.DisplayRole)
            # WORKER
            
            path = f'outputs/{item_text}'
            self._worker = Worker(path, self._canvas, self._mean_vb, self._median_vb)
            self._worker.finished.connect(self._on_analyze_done)
            self._worker.start() 

    def _on_analyze_done(self):
        self._signals.on_analyze_signal_done.emit()
            
    def _on_delete(self):
        """
        Deletes the selected file from the list view and the filesystem.
        """
        indexes = self._lv.selectedIndexes()
        if indexes:
            index = indexes[0]
            item_text = self._file_model.data(index, Qt.DisplayRole)
            path = f'outputs/{item_text}'
            reply = QMessageBox.question(self, 'Borrar Archivo', f'¿Estas seguro de eliminar "{item_text}"?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                try:
                    os.remove(path)
                    self._file_model.remove(index)
                except Exception as e:
                    QMessageBox.critical(self, 'Error', f'Failed to delete file: {str(e)}')

