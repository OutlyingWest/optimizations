from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QWidget
from ui.ui_pyside_base.ui_info import Ui_InfoWidget


class InfoWidget(QWidget):
    """ Class of note plate in scrolling area in main window """
    delete = Signal(int)

    def __init__(self):
        super().__init__()
        # Design init
        self.ui = Ui_InfoWidget()
        self.ui.setupUi(self)
