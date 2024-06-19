""" calling all file from this main class """

from shapefactory import ShapeFactory
class MainClass:
    def main(self):
        ShapeFactoryobj = ShapeFactory()
        shapeobj = ShapeFactoryobj.get_shape("circle")
        shapeobj.draw()


mainclassobj = MainClass()
mainclassobj.main()