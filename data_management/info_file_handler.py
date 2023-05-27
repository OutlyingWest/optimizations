import os
from dataclasses import dataclass


@dataclass
class DataPaths:
    info_file_path: str


class InfoFilesHandler:
    def __init__(self, info_file_name: str, note_body_text=None):
        self.path = DataPaths.info_file_path
        self.name = info_file_name
        self.text = note_body_text

    def read_info_from_file(self):
        with open(file=f'{self.path}{self.name}.txt', mode="r") as info:
            rode_info_text = info.read()
        return rode_info_text





