from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget


class LineEdit(QWidget):

    """
      LineEdit is a custom widget that combines a QLabel and a QLineEdit in a horizontal layout.

      The QLabel displays a static text label, and the QLineEdit allows the user to input or edit text.

      Attributes:
      ----------
      _layout : QHBoxLayout
          The horizontal layout that contains the QLabel and QLineEdit.
      _label : QLabel
          A label that displays static text next to the QLineEdit.
      _le : QLineEdit
          The line edit widget where the user can input text.

      Methods:
      -------
      __init__(text: str = "", parent: QWidget | None = None):
          Initializes the LineEdit widget with an optional label text and parent widget.

      set_text(text: str):
          Sets the text in the QLineEdit.

      text() -> str:
          Returns the current text in the QLineEdit.
      """

    def __init__(self, text: str = "", parent: QWidget | None = None):
        super().__init__(parent)
        self._layout = QHBoxLayout()
        self.setLayout(self._layout)
        # TEXT
        self._label = QLabel(text=text, parent=self)
        self._layout.addWidget(self._label)
        # LINE EDIT
        self._le = QLineEdit(self)
        self._layout.addWidget(self._le)

    def set_text(self, text: str):
        self._le.setText(text)

    def text(self) -> str:
        return self._le.text()
