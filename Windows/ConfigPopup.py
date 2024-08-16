from PyQt5.QtWidgets import QButtonGroup, QLineEdit, QDialog, QGroupBox, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, pyqtSignal
from Widgets import Slider, LineEdit
from Signals import Signals
from config import ConfigType, read_config, write_config, USER_CONFIG_PATH


class ConfigPopup(QDialog):
    """
    ConfigPopup is a custom dialog window that provides a user interface for configuring
    various camera settings such as brightness, contrast, saturation, ISO, and sharpness.
    It also includes options for noise reduction.

    Attributes:
    ----------
    _layout : QVBoxLayout
        The main layout of the dialog.
    _basename_le : LineEdit
        A line edit widget for entering the base name.
    _brightness_slider : Slider
        A slider to adjust brightness.
    _contrast_slider : Slider
        A slider to adjust contrast.
    _saturation_slider : Slider
        A slider to adjust saturation.
    _iso_slider : Slider
        A slider to adjust ISO.
    _sharpness_slider : Slider
        A slider to adjust sharpness.
    _noise_reduction_select : NoiseReductionSelect
        A group of radio buttons to select the noise reduction level.
    _ok_btn : QPushButton
        A button to confirm the settings and close the dialog.
    _cancel_btn : QPushButton
        A button to cancel the settings and close the dialog.

    Methods:
    -------
    __init__(signals : Signals, parent : QWidget | None = None):
        Initializes the ConfigPopup dialog with various sliders and noise reduction options.
    _on_ok():
        Closes the dialog when the OK button is clicked.
    _on_cancel():
        Closes the dialog when the Cancel button is clicked.
    """

    def __init__(self, signals: Signals, parent: QWidget | None = None, ):
        """
         Initializes the ConfigPopup class.

         This method sets up the configuration dialog window with the following features:
         - A vertical layout to organize the widgets.
         - A line edit for entering a base name.
         - Multiple sliders for adjusting brightness, contrast, saturation, ISO, and sharpness.
         - A noise reduction selection group with three radio buttons.
         - OK and Cancel buttons to close the dialog.
         """
        super().__init__(parent)
        # WINDOW SETUP
        self.resize(600, 300)
        self.setWindowTitle("Configuracón")
        self.setModal(True)
        self.setWindowFlag(Qt.BypassWindowManagerHint)
        self.setWindowFlag(Qt.WindowType.WindowSystemMenuHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.WindowType.WindowCloseButtonHint)
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        # SIGNALS
        signals.on_set_user_settings.connect(self._on_load_settings)
        self._signals = signals
        # LINE EDIT
        self._basename_le = LineEdit(text="Nombre base")
        self._layout.addWidget(self._basename_le)
        # SLIDERS
        # SLIDERS -> BRIGHTNESS
        self._brightness_slider = Slider(
            signal=signals.on_change_brightness,
            icon_path="Assets/svg/brightness.svg",
            tooltip="Brillo",
            label_format="f'{value} %'"
        )
        self._layout.addWidget(self._brightness_slider)
        # SLIDERS -> CONTRAST
        self._contrast_slider = Slider(
            signal=signals.on_change_contrast,
            icon_path="Assets/svg/contrast.svg",
            tooltip="Contraste",
            max_value=320,
            label_format="f'{value / 10}'"
        )
        self._layout.addWidget(self._contrast_slider)
        # SLIDERS -> SATURATION
        self._saturation_slider = Slider(
            signal=signals.on_change_saturation,
            icon_path="Assets/svg/saturation.svg",
            tooltip="Saturación",
            max_value=320,
            label_format="f'{value / 10}'"
        )
        self._layout.addWidget(self._saturation_slider)
        # SLIDERS -> ISO
        self._iso_slider = Slider(
            signal=signals.on_change_iso,
            icon_path="Assets/svg/iso.svg",
            tooltip="ISO",
            max_value=106,
            label_format="f'{value / 10}'"
        )
        self._layout.addWidget(self._iso_slider)
        # SLIDERS -> SHARPNESS
        self._sharpness_slider = Slider(
            signal=signals.on_change_sharpness,
            icon_path="Assets/svg/sharpness.svg",
            tooltip="Sharpness",
            max_value=160,
            label_format="f'{value / 10}'"
        )
        self._layout.addWidget(self._sharpness_slider)
        # NOISE SELECT
        self._noise_reduction_select = NoiseReductionSelect(signal=signals.on_change_noise_reduction)
        self._layout.addWidget(self._noise_reduction_select)
        # BUTTONS
        self._ok_btn = QPushButton("Ok")
        self._ok_btn.clicked.connect(self._on_ok)
        self._layout.addWidget(self._ok_btn)
        self._cancel_btn = QPushButton("Cancel")
        self._cancel_btn.clicked.connect(self._on_cancel)
        self._layout.addWidget(self._cancel_btn)

    def _on_ok(self):  
        config = ConfigType(
            Brightness= (self._brightness_slider.value() - 50 ) / 100.0,
            Contrast=self._contrast_slider.value() / 10.0,
            NoiseReductionMode=self._noise_reduction_select.value(),
            AnalogueGain=self._iso_slider.value() / 10.0,
            Sharpness=self._sharpness_slider.value() / 10.0,
            Saturation=self._saturation_slider.value() / 10.0,
            BaseName=self._basename_le.text()
        )      
        write_config(USER_CONFIG_PATH, config)
        self._signals.on_config_signal_done.emit()
        self.close()

    def _on_cancel(self):
        user_setings = read_config(USER_CONFIG_PATH)
        self._signals.on_set_user_settings.emit(user_setings)
        self._signals.on_config_signal_done.emit()
        self.close()

    def _on_load_settings(self, config : ConfigType):
        self._iso_slider.set_value(int(config["AnalogueGain"] * 10) )
        self._basename_le.set_text(config["BaseName"])
        self._brightness_slider.set_value(int(config["Brightness"] * 50) + 50)
        self._contrast_slider.set_value(int(config['Contrast'] * 10))
        self._saturation_slider.set_value(int(config['Saturation'] * 10))
        self._sharpness_slider.set_value(int(config['Sharpness'] * 10))
        if config['NoiseReductionMode'] == 2:
            self._noise_reduction_select.set_mode_hq()
        elif config['NoiseReductionMode'] == 1:
            self._noise_reduction_select.set_mode_fast()
        else:
            self._noise_reduction_select.set_mode_none()
        
        
class NoiseReductionSelect(QGroupBox):
    """
    NoiseReductionSelect is a custom QGroupBox that provides options for selecting
    the level of noise reduction in a camera or image processing application.

    This widget includes three radio buttons for choosing between no noise reduction,
    fast noise reduction, and high-quality noise reduction.

    Attributes:
    ----------
    _layout : QHBoxLayout
        The horizontal layout that organizes the radio buttons within the group box.
    _btn_group : QButtonGroup
        A button group that manages the radio buttons, ensuring that only one can be selected at a time.
    _rbtn_none : QRadioButton
        A radio button for disabling noise reduction.
    _rbtn_fast : QRadioButton
        A radio button for enabling fast noise reduction.
    _rbtn_hq : QRadioButton
        A radio button for enabling high-quality noise reduction.

    Methods:
    -------
    __init__(parent: QWidget | None = None):
        Initializes the NoiseReductionSelect group box with three radio buttons and adds them
        to a horizontal layout. The radio buttons are grouped together, so only one can be selected
        at a time.
    """

    def __init__(self, signal: pyqtSignal | None = None, parent: QWidget | None = None):
        """
        Initializes the NoiseReductionSelect class.

        Parameters:
        ----------
        parent : QWidget | None, optional
            The parent widget for the group box, if any (default is None).

        This method sets up the noise reduction selection with three options:
        - 'Desactivada': Disables noise reduction.
        - 'Rápida': Enables fast noise reduction.
        - 'Alta Calidad': Enables high-quality noise reduction.

        The radio buttons are added to a horizontal layout and managed by a button group.
        """
        super().__init__(title="Reducción de ruido", parent=parent)
        self._layout = QHBoxLayout()
        self.setLayout(self._layout)
        # SIGNAL
        self._signal = signal
        # BUTTON GROUP
        self._btn_group = QButtonGroup(self)
        self._btn_group.buttonClicked.connect(self._on_select)
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
        
    def set_mode_none(self):
        """
        Sets the None radio buttons a checked
        """
        self._rbtn_none.setChecked(True)
    
    def set_mode_fast(self):
        """
        Sets the Fast radio button as checked
        """
        self._rbtn_fast.setChecked(True)
        
    def set_mode_hq(self):
        """
        Sets the High Quality radio button as checked
        """
        self._rbtn_hq.setChecked(True)

    def _on_select(self, btn : QWidget):
      self._signal.emit(self._btn_group.id(btn))
    
    def value(self) -> int:
        for button in self._btn_group.findChildren(QRadioButton):
            if button.isChecked():
                return self._btn_group.id(button)
        return 0