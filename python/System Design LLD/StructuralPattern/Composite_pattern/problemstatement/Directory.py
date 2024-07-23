from File import File

class Directory:
    def __init__(self, name):
        self.directory_name = name
        self.object_list = []

    def add(self, obj):
        self.object_list.append(obj)

    def ls(self):
        print(f"Directory Name: {self.directory_name}")
        for obj in self.object_list:
            if isinstance(obj, File):
                obj.ls()
            elif isinstance(obj, Directory):
                obj.ls()
