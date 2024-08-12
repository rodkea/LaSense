from PySide6.QtWidgets import QButtonGroup, QLineEdit, QDialog, QGroupBox, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from Widgets import Slider, LineEdit


class ConfigPopup(QDialog):
  
  def __init__(self, parent : QWidget | None = None):
    super().__init__(parent)
    # WINDOW SETUP
    self.resize(600,300)
    self.setWindowTitle("Configuracón")
    self.setModal(True)    
    self.setWindowFlag(Qt.BypassWindowManagerHint)
    self.setWindowFlag(Qt.WindowType.WindowSystemMenuHint)
    self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
    self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint)
    self._layout = QVBoxLayout()
    self.setLayout(self._layout)
    # LINE EDIT
    self._basename_le = LineEdit(text="Nombre base")
    self._layout.addWidget(self._basename_le)
    # SLIDERS
    # SLIDERS -> BRIGHTNESS
    self._brightness_slider = Slider(
      icon_path="Assets/svg/brightness.svg",
      tooltip="Brillo",
      label_format="f'{value} %'"
      )
    self._layout.addWidget(self._brightness_slider)
    # SLIDERS -> CONTRAST
    self._contrast_slider = Slider(
      icon_path="Assets/svg/contrast.svg",
      tooltip="Contraste",
      max_value=320,
      label_format="f'{value / 10}'"
      )
    self._layout.addWidget(self._contrast_slider)
    # SLIDERS -> SATURATION
    self._saturation_slider = Slider(
      icon_path="Assets/svg/saturation.svg",
      tooltip="Saturación",
      max_value=320,
      label_format="f'{value / 10}'"
      )
    self._layout.addWidget(self._saturation_slider)
    # SLIDERS -> ISO
    self._iso_slider = Slider(
      icon_path="Assets/svg/iso.svg",
      tooltip="ISO",
      max_value=106,
      label_format="f'{value / 10}'"
      )
    self._layout.addWidget(self._iso_slider)
    # SLIDERS -> SHARPNESS
    self._sharpness_slider = Slider(
      icon_path="Assets/svg/sharpness.svg",
      tooltip="Sharpness",
      max_value=160,
      label_format="f'{value / 10}'"
      )
    self._layout.addWidget(self._sharpness_slider)
    # NOISE SELECT
    self._noise_reduction_select = NoiseReductionSelect()
    self._layout.addWidget(self._noise_reduction_select)
    # BUTTONS
    self._ok_btn = QPushButton("Ok")
    self._ok_btn.clicked.connect(self._on_ok)
    self._layout.addWidget(self._ok_btn)
    self._cancel_btn = QPushButton("Cancel")
    self._cancel_btn.clicked.connect(self._on_cancel)
    self._layout.addWidget(self._cancel_btn)    
    
  def _on_ok(self):
    self.close()
    
  def _on_cancel(self):
    self.close()
    
    
    
class NoiseReductionSelect(QGroupBox):
  
  def __init__(self, parent : QWidget | None = None):
    super().__init__(title="Reducción de ruido", parent=parent)
    self._layout = QHBoxLayout()
    self.setLayout(self._layout)
    self._btn_group = QButtonGroup(self)
    self._rbtn_none = QRadioButton("Desactivada", self)
    self._layout.addWidget(self._rbtn_none)
    self._rbtn_fast = QRadioButton("Rápida", self)
    self._layout.addWidget(self._rbtn_fast)
    self._rbtn_hq = QRadioButton("Alta Calidad", self)
    self._layout.addWidget(self._rbtn_hq)
    self._btn_group.addButton(self._rbtn_none, 0)
    self._btn_group.addButton(self._rbtn_fast, 1)
    self._btn_group.addButton(self._rbtn_hq, 2)
    self.setLayout(self._layout)
    
    
    
    