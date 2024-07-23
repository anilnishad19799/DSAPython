from Filename import FileSystem

class Directory(FileSystem):
    def __init__(self, name):
        self.directory_name = name
        self.file_system_list = []

    def add(self, file_system_obj):
        self.file_system_list.append(file_system_obj)

    def ls(self):
        print("Directory name", self.directory_name)
        for file_system_obj in self.file_system_list:
            # print("filesysem obj", file_system_obj)
            file_system_obj.ls()
