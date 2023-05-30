from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow, QPushButton
from ui.info import InfoWidget
from ui.ui_pyside_base.ui_main_window import Ui_MainWindow
from data_management.info_file_handler import InfoFilesHandler
from configuration import load_config


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load data
        self.config = load_config()
        # Design init
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Widgets list
        self.info_widgets = {}
        # Connections to buttons
        self.ui.ProjectsButton.clicked.connect(self.open_info_widget)
        self.ui.MeasurersButton.clicked.connect(self.open_info_widget)
        self.ui.ArchitectsButton.clicked.connect(self.open_info_widget)
        self.ui.VolumeButton.clicked.connect(self.open_info_widget)

    @Slot()
    def open_info_widget(self):
        """ Open an info window """
        # Receive pushed button object
        button_obj: QPushButton = self.sender()
        button_name = button_obj.objectName()
        self.info_widgets[button_name] = InfoWidget()
        # Load info
        files_manager = InfoFilesHandler(file_path=self.config.paths.data,
                                         info_file_name=self.config.button_links_dict[button_name])
        info_text = files_manager.read_info_from_file()
        self.info_widgets[button_name].ui.textEdit.setText(info_text)
        self.info_widgets[button_name].setWindowTitle(button_obj.text())
        # Show info window
        self.info_widgets[button_name].show()
