class File:
    def __init__(self, name):
        self.file_name = name

    def ls(self):
        print(f"file name {self.file_name}")
