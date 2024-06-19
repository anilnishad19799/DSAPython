from circle import Circle
from rectangle import Rectangle

class ShapeFactory:
    @staticmethod
    def get_shape(input_str):
        shapes = {
            "circle": Circle,
            "rectangle": Rectangle
        }
        shape_class = shapes.get(input_str.lower())
        if shape_class:
            return shape_class()
        else:
            return None
