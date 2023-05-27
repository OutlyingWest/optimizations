import os
import sys
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from configuration import load_config


def main():
    load_config()
    app = QApplication()
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
