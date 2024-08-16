from PyQt5.QtWidgets import QLabel, QSlider, QWidget, QHBoxLayout
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import Qt, pyqtSignal
from Signals import Signals


class Slider(QWidget):

    """
      Slider is a custom widget that combines a slider with an icon and a label to display the current value.

      The widget emits a signal whenever the slider's value changes, and the label is updated to reflect
      the current value using a customizable format string.

      Attributes:
      ----------
      _signal : pyqtSignal
          The signal to be emitted when the slider value changes.
      _layout : QHBoxLayout
          The horizontal layout that contains the icon, slider, and label.
      _svg : QSvgWidget
          A widget that displays an SVG icon.
      _slider : QSlider
          The slider component that allows the user to select a value within a specified range.
      _label_format : str
          The format string used to display the slider's value in the label.
      _label : QLabel
          A label that displays the slider's current value.

      Methods:
      -------
      __init__(icon_path: str, signal: pyqtSignal, tooltip: str = "",
               min_value: int = 0, max_value: int = 100, step: int = 1,
               label_format: str = "f'{value}'", parent: QWidget | None = None):
          Initializes the Slider widget with an icon, signal, and other optional parameters.

    
      _value_changed():
          Slot that is triggered when the slider's value changes. Updates the label and emits the signal.

      _update_label():
          Updates the label text based on the slider's current value and the specified label format.
      """

    def __init__(self, icon_path: str, signal: pyqtSignal, tooltip: str = "",
                 min_value: int = 0, max_value: int = 100,
                 step: int = 1, label_format: str = "f'{value}'",
                 parent: QWidget | None = None):
        super().__init__(parent)
        self._signal = signal
        self._layout = QHBoxLayout(self)
        self._svg = QSvgWidget(icon_path)
        self._svg.setFixedSize(35, 35)
        self.setToolTip(tooltip)
        self._slider = QSlider(Qt.Orientation.Horizontal)
        self._slider.setRange(min_value, max_value)
        self._slider.setSingleStep(step)
        self._slider.valueChanged.connect(self._value_changed)
        self._label_format = label_format
        self._label = QLabel()      
        self._update_label(self._slider.value())
        self._layout.addWidget(self._svg)
        self._layout.addWidget(self._slider)
        self._layout.addWidget(self._label)    

    def _value_changed(self):
        """
        Slot that is triggered when the slider's value changes.
        Updates the label and emits the signal.
        """
        value = self._slider.value()
        self._update_label(value)
        self._signal.emit(value)
        
    def _update_label(self, value : int): 
        """
        Updates the label text based on the slider's current value and the specified label format.

        Parameters:
        ----------
        value : int
            The current value of the slider.
        """       
        try:
            # Evalúa el formato del f-string
            label_text = eval(self._label_format)
        except Exception as e:
            label_text = str(e)
        self._label.setText(label_text)

    def set_value(self, value: int):
        self._slider.setValue(value)
        self._update_label(value)
    def value(self) -> int:
        return self._slider.value()
        
    