from dataclasses import dataclass
from PySide6.QtWidgets import QWidget


@dataclass
class StylePaths:
    path: str


class StylerQss:
    def __init__(self, q_object: QWidget, style_name: str):
        self.style = {}
        self._style_load(style_name)
        self._style_set_properties(q_object)

    def _style_load(self, style_name):
        with open(f'ui/styles/qss/{style_name}.qss', 'r') as style:
            for line in style:
                key, value = line.split(': ')
                self.style.update({key: value.rstrip(';\n')})

    def _style_set_properties(self, q_object: QWidget):
        style_string = ''.join(f'{key}: {value}; ' for key, value in self.style.items())
        q_object.setStyleSheet(style_string)


class StylerPalette:
    pass
