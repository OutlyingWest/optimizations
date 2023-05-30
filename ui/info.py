from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont
from ui.ui_pyside_base.ui_info import Ui_InfoWidget


class InfoWidget(QWidget):
    """ Class of note plate in scrolling area in main window """
    delete = Signal(int)

    def __init__(self):
        super().__init__()
        # Design init
        self.ui = Ui_InfoWidget()
        self.ui.setupUi(self)
        # Set font
        monospace_font = QFont("Consolas")  # Указываем имя моноширинного шрифта
        self.ui.textEdit.setFont(monospace_font)
        tab_width = 4  # Ширина табуляции в пробелах
        tab_stop_distance = monospace_font.pixelSize() * tab_width  # Вычисляем фактическую ширину табуляции в пикселях
        self.ui.textEdit.setTabStopDistance(tab_stop_distance)

