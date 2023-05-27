

class InfoFilesHandler:
    def __init__(self, file_path: str, info_file_name: str, text=None, ):
        self.path = file_path
        self.name = info_file_name
        self.text = text

    def read_info_from_file(self):
        with open(file=f'{self.path}{self.name}.txt', mode="r") as info:
            rode_info_text = info.read()
        return rode_info_text





