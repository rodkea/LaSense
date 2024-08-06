from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import  Qt
from PySide6.QtGui import QCursor


class Button(QSvgWidget):
    # signal: Signal,
    def __init__(self, icon_path: str, 
                 icon_path_hover: str | None = None,
                 icon_path_disabled: str | None = None,
                 enabled: bool = True,
                 width: int = 25, height: int = 25,
                 parent: QWidget | None = None):
        """Creates a Button with an SVG icon.
        Args:
            signal (Signal): _description_
            icon_path (str): Path to the default svg image            
            icon_path_hover (str | None, optional): Path to the hover svg image. Defaults to None.
            icon_path_disabled (str | None, optional): Path to the disabled svg image. Defaults to None.
            width (int, optional): width in pixels of the button. Defaults to 25.
            height (int, optional): heigh in pixels of the button. Defaults to 25.
            parent (QWidget | None, optional): Defaults to None.
        """
        super().__init__(parent)
        self.setFixedSize(width, height)
        self._is_enabled = enabled
        #self._signal = signal
        # ICON PATHS
        self._icon_path = icon_path
        if icon_path_hover:
          self._icon_path_hover = icon_path_hover
        else:
          self._icon_path_hover = icon_path
        if icon_path_disabled:
          self._icon_path_disabled = icon_path_disabled
        else:
          self._icon_path_disabled = icon_path        
        # SET ICON
        if self.is_enabled:        
          self.load(self._icon_path)
        else:
          self.load(self._icon_path_disabled)          

    @property
    def is_enabled(self):
      return self._is_enabled
    
    def enterEvent(self, event):
        # Cambiar el cursor cuando el mouse entra al widget
        self.setCursor(QCursor(Qt.PointingHandCursor))
        if self.is_enabled:
          self.load(self._icon_path_hover)  # CAMBIA EL SVG AL AZUL
        super().enterEvent(event)

    def leaveEvent(self, event):
        # Restaurar el cursor cuando el mouse sale del widget
        self.setCursor(QCursor(Qt.ArrowCursor))
        if self.is_enabled:
          self.load(self._icon_path)  # CAMBIA EL SVG AL DEFAULT
        else:
          self.load(self._icon_path_disabled) 
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        # Manejar el evento de click
        if event.button() == Qt.LeftButton:
            if self.is_enabled:
              self.set_disabled()
              #self._signal.emit()
        super().mousePressEvent(event)

    def set_enabled(self):
      self._is_enabled = True
      self.load(self._icon_path)
    
    def set_disabled(self):
      self._is_enabled = False
      if self._icon_path_disabled:
        self.load(self._icon_path_disabled)
      else:
        self.load(self._icon_path)